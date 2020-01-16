import os
import re
import sys
import json
import datetime as dt
from time import sleep
from filecmp import cmp
from copy import deepcopy
from random import randint
from shutil import copyfile
from subprocess import call
import paho.mqtt.client as mqtt
from PyInquirer import style_from_dict, Token, prompt, Separator

###########################################################
# Make sure these are set correctly for your environment:

site_config = os.path.join('config', 'sites.json')
blank_defines = 'blank_defines.h'

espqdir = os.path.dirname(os.path.abspath(__file__))

current_tasmota_version = '0x08010000' # v8.1.0
tasmota_dir = os.path.join(espqdir, '..', 'Tasmota')
custom_dir = os.path.join(espqdir, '..', 'custom-mqtt-programs/')

###########################################################


hass_template_dir = os.path.join(espqdir, 'hass_templates')
hass_output_dir = os.path.join(espqdir, 'hass_output')

loop_time = 1 # passed to mqtt.loop timeout
wait_time = 45.0 # how long to wait for device to come online after flash
waitForStatus = 3 # how long to wait for a status before giving up

colors = {"RED": '\033[1;31m',
          "GREEN": '\033[1;32m',
          "BLUE": '\033[94m',
          "NC": '\033[0m'}

tasmota_status_query = {
        '11': {'ssid': ['StatusSTS', 'Wifi', 'SSId'],
               'bssid': ['StatusSTS', 'Wifi', 'BSSId'],
               'channel': ['StatusSTS', 'Wifi', 'Channel'],
               'rssi': ['StatusSTS', 'Wifi', 'RSSI'],
               'power': ['StatusSTS', 'POWER']},
         '5': {'ip': ['StatusNET', 'IPAddress'],
               'mac': ['StatusNET', 'Mac'],
               'wificonfig':['StatusNET', 'WifiConfig']},
         '2': {'tas_version': ['StatusFWR', 'Version'],
              'core_version': ['StatusFWR', 'Core']}
        }

# too_old will return true if the time is more than seconds ago
def too_old(time, seconds):
    return (dt.datetime.now() - time).total_seconds() > seconds

class device(dict):
    """
    Structure to store the details of each hardware device
    """
    def __init__(self, device):
        for key in device:
            # Each devices doesn't need to know about the other IDs
            if key != 'ids':
                # Convert all other keys to device attributes
                # Sanitize attributes so missing ones are '' instead of None
                if device[key] is not None:
                    setattr(self, key, device[key])
                else:
                    setattr(self, key, '')

        self.base_topic = self.base_topic.lower()
        self.full_topic = '%prefix%/{base_topic}/%topic%'.format(**self)
        self.topic = self.topic.lower()
        topic_str = re.sub("%topic%", self.topic, self.full_topic)
        self.c_topic = re.sub('%prefix%','cmnd', topic_str)
        self.s_topic = re.sub('%prefix%','stat', topic_str)
        self.t_topic = re.sub('%prefix%','tele', topic_str)
        # Friendly name
        self.f_name = re.sub('_', ' ', re.sub('\/|-', ' ', self.name))
        # Unfriendly name
        self.name =   re.sub(' ', '_', re.sub('\/|-', '_', self.name))

        # home assistant doesn't like upper case letters in sensor names
        self.name = self.name.lower()

        # Insert site information as device attributes
        with open(site_config, 'r') as f:
            sites = json.load(f)
        for key in sites[self.site]:
            # Sanitize attributes so missing ones are '' instead of None
            if sites[self.site][key] is not None:
                setattr(self, key, sites[self.site][key])
            else:
                setattr(self, key, '')
        # Format the device's build flags
        # This is still a little hacky--tasmota and custom build flags are
        # handled entirely differently. The latter way is probably better since
        # it's the general case
        if self.software == 'tasmota' and self.build_flags != '':
            self.build_flags = '\n'.join(['#define {}'.format(flag) for flag \
                                          in self.build_flags])
        elif self.software == 'custom-mqtt-programs':
            bf_str = ('-DWIFI_SSID=\\"{wifi_ssid}\\" '
                      '-DWIFI_PASSWORD=\\"{wifi_pass}\\" '
                      '-DNAME=\\"{name}\\" '
                      '-DMQTT_SERVER=\\"{mqtt_host}\\" '
                      '-DTOPIC=\\"{base_topic}/{topic}\\"')
            self.build_flags += bf_str.format(**self)
        self.mqtt = mqtt.Client(clean_session=True,
                                client_id="espq_{name}".format(**self))
        self.mqtt.reinitialise()
        self.mqtt.on_message = self._on_message
        self.flashed = False
        self.online = False
        self.reported = {}

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError('No such attribute: ' + name)

    def __setattr__(self, name, value):
            self[name] = value

    def __repr__(self):
        return('\n'.join('{}: {}'.format(k, str(v)) for k, v \
                                         in self.items() if v != ''))

    def __del__(self):
        if 'mqtt' in self:
            self.mqtt.disconnect()

    def _on_message(self, mqtt, userdata, msg):
        print(msg.topic + ' ' + msg.payload)

    def flash(self, flash_mode, serial_port):
        """
        Flash device, watch for it to come online,
        and run setup commads
        """
        self.flash_mode = flash_mode
        if serial_port != '':
            self.serial_port = serial_port

        # Flash the right software.
        if self.software == 'tasmota':
            self.flashed = self.flash_tasmota()
        else:
            self.flashed = self.flash_custom()
        # If it flashed correctly, watch for it to come online.
        online = False
        if self.flashed:
            print(('{GREEN}{f_name} flashed successfully. Waiting for it to '
                   'come back online...{NC}'.format(**colors, **self)))
            sleep(1)
            online = self.online_check()
        else:
            self._handle_result(1)

        if not online and self.flashed:
            self._handle_result(2)
        # If it came back online, run any setup commands,
        # and watch for it to come online again.
        elif self.flashed and online:
            # Skip commands if there are none.
            if not hasattr(self, 'commands') or not self.commands:
                self._handle_result(0)
                return(0)
            else:
                print(('{GREEN}{f_name} is online after flashing. Running '
                       'setup commands...{NC}'.format(**colors, **self)))
                sleep(1)
                for c in self.commands:
                    self.mqtt.connect(self.mqtt_host)
                    command = "{c_topic}/{cmnd}".format(**self, 
                                                        cmnd=c['command'])
                    print("Sending {c} {p}".format(c=command, p=c['payload']))
                    self.mqtt.publish(command, c['payload'])
                    self.mqtt.disconnect()
                    sleep(1)
                    if "restart" in c and c['restart'] == 1:
                        self.online_check()

            if online:
                self._handle_result(0)
                return(0)
            else:
                self._handle_result(3)
        return(1)

    def _handle_result(self, result_code):
        """
        Display output based on the result from flash()
        """
        now = str(dt.datetime.now())
        if result_code == 0:
            result = ('{time}\t{GREEN}{f_name} flashed successfully.'
                      '{NC}').format(time=now, **colors, **self)
            with open(os.path.join(espqdir,
                                   'flash_success.log'), 'a+') as flashlog:
                flashlog.write(result + '\n')
                print(result)
            return()
        elif result_code == 1:
            result = ('{time}\t{RED}{f_name}{NC} failed '
                     'to flash.').format(time=now, **colors, **self)
        elif result_code == 2:
            result = ('{time}\t{RED}{f_name} did not come back online after'
                      'flashing.{NC}'.format(time=now, **colors, **self))
        elif result_code == 3:
            result = ('{time}\t{RED}{f_name} did not come back online after '
                      'setup commands.{NC}'.format(time=now, **colors, **self))
        else:
            result = ('{time}\t{RED}{f_name} WTF? Shit\'s broken.'
                      '{NC}').format(time=now, **colors, **self)
        with open(os.path.join(espqdir, 'flash_error.log'), 'a+') as errorlog:
            errorlog.write(result + '\n')
            print('{RED}{result}{NC}'.format(**colors, result=result))
        return()

    def write_tasmota_config(self):
        """
        Fills tasmota device parameters into blank_defines.h and writes it
        to {tasmota_dir}/tasmota/user_config_override.h
        """
        with open(blank_defines, 'r') as f:
            defines = f.read()
        # Every device attribute is passed to the string formatter
        defines = defines.format(**self, datetime=dt.datetime.now(),
                                 cfg_holder=str(randint(1, 32000)))
        # Write the config file
        with open(os.path.join(tasmota_dir, 'tasmota',
                               'user_config_override.h'), 'w') as f:
            f.write(defines)

    def flash_tasmota(self):
        """
        Flash the device with tasmota
        """
        # Make sure device is tasmota
        if self.software != 'tasmota':
            print('{f_name} is {software}, not tasmota'.format(**self))
            return(False)
        if current_tasmota_version != get_tasmota_version():
            print('{RED}Error: Tasmota version mismatch{NC}'.format(**colors))
            return(False)
        self.write_tasmota_config()

        correctPIO = os.path.join(espqdir, 'platformio_override.ini')
        tasmotaPIO = os.path.join(tasmota_dir, 'platformio_override.ini')
        if not os.path.exists(tasmotaPIO) or not cmp(correctPIO, tasmotaPIO):
            copyfile(correctPIO, tasmotaPIO)

        ip_missing = not 'ip_addr' in self or not self.ip_addr
        if self.flash_mode == 'wifi' and ip_missing:
            print('No IP address for this device in the config.'
                  'Querying device...')
            self.query_tas_status()
            if 'ip' in self.reported:
                print('{name} is online at {ip}'.format(name=self.f_name,
                                                        ip=self.reported['ip']))
                self.ip_addr = self.reported['ip']
            else:
                print('{f_name} did not respond at {c_topic}. IP address '
                      'unavailable. Skipping device...'.format(**self))
                return(False)

        os.chdir(tasmota_dir)
        pio_call = 'platformio run -e {env} -t upload --upload-port {port}'
        if self.flash_mode == 'wifi':
            pio_call = pio_call.format(env='tasmota-wifi',
                                       port=(self.ip_addr + '/u2'))
            print(('{BLUE}Now flashing {module} {f_name} with {software} via '
                '{flash_mode} at {ip_addr}{NC}'.format(**colors, **self)))
        elif self.flash_mode == 'serial':
            pio_call = pio_call.format(env='tasmota-serial',
                                       port=self.serial_port)
            print(('{BLUE}Now flashing {module} {f_name} with {software} via '
                '{flash_mode} at {serial_port}{NC}'.format(**colors, **self)))
        print('{BLUE}{f_name}\'s MQTT topic is {base_topic}/'
              '{topic}{NC}'.format(**colors, **self))
        print(pio_call)
        flash_result = call(pio_call, shell=True)
        os.chdir(espqdir)
        return(True if flash_result == 0 else False)

    def flash_custom(self):
        """
        Flash the device with custom firmware
        """
        src_dir = os.path.join(custom_dir, self.module)
        os.environ['PLATFORMIO_SRC_DIR']=src_dir
        os.environ['PLATFORMIO_BUILD_FLAGS']=self.build_flags
        print("PLATFORMIO_SRC_DIR:", os.environ['PLATFORMIO_SRC_DIR'])
        print("PLATFORMIO_BUILD_FLAGS:", os.environ['PLATFORMIO_BUILD_FLAGS'])
        os.chdir(custom_dir)
        pio_call = ('platformio run -e {board}-{flash_mode} -t upload '
                    '--upload-port {port}')
        if self.flash_mode == 'wifi':
            pio_call = pio_call.format(port=self.ip_addr, **self)
            print(('{BLUE}Now flashing {module} {f_name} in {software} via '
                '{flash_mode} at {ip_addr}{NC}'.format(**colors, **self)))
        elif self.flash_mode == 'serial':
            pio_call = pio_call.format(port=self.serial_port, **self)
            print(('{BLUE}Now flashing {module} {f_name} in {software} via '
                '{flash_mode} at {serial_port}{NC}'.format(**colors, **self)))
        else:
            print("no flash mode set, try again?")
            return(False)

        print(pio_call)
        flash_result = call(pio_call, shell=True)

        os.environ['PLATFORMIO_SRC_DIR']=''
        os.environ['PLATFORMIO_BUILD_FLAGS']=''
        os.chdir(espqdir)
        return(True if flash_result == 0 else False)

    def online_check(self):
        """
        Connect to MQTT and watch for the device to publish LWT Online
        Returns True if device is Online
        """
        self.online = False
        online_topic = '{t_topic}/INFO2'.format(**self)
        print('{BLUE}Watching for {}{NC}'.format(online_topic, **colors))
        self.mqtt.connect(self.mqtt_host)
        self.mqtt.message_callback_add(online_topic, lambda *args: \
                                                 setattr(self, 'online', True))
        self.mqtt.subscribe(online_topic)
        startTime = dt.datetime.now()
        while not self.online and not too_old(startTime, wait_time):
            self.mqtt.loop(timeout=loop_time)
        time_waited = (dt.datetime.now() - startTime).total_seconds()
        if not self.online:
            print('{RED}{f_name} did not come online within {wait_time} '
                  'seconds{NC}'.format(f_name=self.f_name,
                                       wait_time=str(wait_time),
                                       **colors))
        elif self.online:
            print('{GREEN}{f_name} came online in {time_waited} '
                  'seconds{NC}'.format(f_name=self.f_name,
                                       time_waited=time_waited,
                                       **colors))
        self.mqtt.unsubscribe(online_topic)
        self.mqtt.message_callback_remove(online_topic)
        self.mqtt.disconnect()
        return self.online

    def query_tas_status(self):
        """
        Query a tasmota device's status
        """
        response = {}
        def _tas_status_callback(mqtt, userdata, msg):
            if 'STATUS' in msg.topic[-8:]:
                stat_num=re.sub(r'.*STATUS([0-9]*)$', r'\1', msg.topic)
                msg = json.loads(msg.payload.decode('UTF-8'))
                for datum in tasmota_status_query[stat_num]:
                    datumPath=tasmota_status_query[stat_num][datum]
                    response[datum] = nested_get(msg, datumPath)
                response['status{num}'.format(num=stat_num)] = dt.datetime.now()
        s_topic = '{s_topic}/+'.format(**self)
        c_topic = '{c_topic}/status'.format(**self)
        self.mqtt.message_callback_add(s_topic, _tas_status_callback)
        self.mqtt.connect(self.mqtt_host)
        self.mqtt.subscribe(s_topic)

        #publish requests
        for status_number, ignored in tasmota_status_query.items():
            self.mqtt.publish(c_topic, status_number)

        # status numbers, converted to status2, etc
        def _status_words():
            return ['status{num}'.format(num=key) for key \
                    in tasmota_status_query.keys()]

        # while not all of the responses exist, 
        # and we aren't too old since the start time
        startTime = dt.datetime.now()
        done = False
        while(not done and not too_old(startTime, waitForStatus)):
            done = True
            for status in _status_words():
                done = done and status in response
            if not done:
                self.mqtt.loop(timeout=loop_time)

        self.mqtt.unsubscribe(s_topic)
        self.mqtt.message_callback_remove(s_topic)
        self.mqtt.disconnect()

        self.reported = response
        return response

    def write_hass_config(self):
        """
        Write yaml config files for Home Assistant.
        Templates should go in hass_template_dir, and
        outputs will go into hass_output_dir/{component_type}/
        (i.e. a sonoff basic on a light has the standard light component,
        plus many sensor components for its metadata)
        """
        if not os.path.isdir(hass_output_dir):
            os.mkdir(hass_output_dir)
        # Add the home assistant template dir to path
        # and import the device's domain
        try:
            sys.path.append(hass_template_dir)
            self.yaml_template = __import__(self.hass_template)
        except:
            print('Device {f_name} domain error, '
                  'cannot write hass config.'.format(**self))
            return()

        # Add sensors for custom AP names
        AP_str_1 = ("    {name}_wifi_ap:\n      friendly_name: '{f_name} "
                    "Wifi AP'\n      value_template: >-\n")
        AP_str_2 = ("        {{% if state_attr('{hass_domain}.{name}', 'Wifi')"
                    "['BSSId'] | string == '")
        AP_str_3 = ("        {{% elif state_attr('{hass_domain}.{name}', "
                    "'Wifi')['BSSId'] | string == '")
        AP_str_4 = ("{MAC}' %}}\n          {name}\n")
        AP_str_5 = ("        {{% else %}}\n          {{{{ state_attr('"
                    "{hass_domain}.{name}', 'Wifi')['BSSId'] }}}}\n        "
                    "{{% endif %}}")

        if hasattr(self, 'wifi_APs'):
            self.wifi_APs_string = AP_str_1.format(**self)
            for AP in self.wifi_APs[:1]:
                self.wifi_APs_string += AP_str_2.format(**self)
                self.wifi_APs_string += AP_str_4.format(**AP)
            for AP in self.wifi_APs[1:]:
                self.wifi_APs_string += AP_str_3.format(**self)
                self.wifi_APs_string += AP_str_4.format(**AP)
            self.wifi_APs_string += AP_str_5.format(**self)
        else:
            self.wifi_APs_string = ''
        # Go through all types of components for domain
        # (i.e. domain light has components light & sensor)
        for c in self.yaml_template.components:
            if not os.path.isdir(os.path.join(hass_output_dir, c)):
                os.mkdir(os.path.join(hass_output_dir, c))
            output_fn = os.path.join(hass_output_dir, c,
                                     '{name}_{c}.yaml'.format(c = c, **self))
            with open(output_fn, 'w') as yamlf:
                yamlf.write(self.yaml_template.components[c].format(**self))


def import_devices(device_file):
    """
    Process JSON file of device configs, export a list of device objects.
    Keyword arguments:
    device_file -- JSON file of devices
    """
    with open(device_file, 'r') as f:
        device_import = json.load(f)
    devices=[]
    for dev in device_import:
        if 'ids' in dev:
            for id_info in dev['ids']:
                new_dev = deepcopy(dev)
                #if the device specific obj has an "id" field
                if 'id' in id_info:
                    #replace the "%id%" string in all string properties
                    for key in new_dev:
                        if isinstance(new_dev[key], str):
                            new_dev[key] = re.sub('%id%',
                                               id_info['id'],
                                               new_dev[key])
                        elif key == 'commands':
                            for c in new_dev['commands']:
                                c['command'] = re.sub('%id%',
                                                   id_info['id'],
                                                   c['command'])
                                c['payload'] = re.sub('%id%',
                                                   id_info['id'],
                                                   c['payload'])

                # just copy all the keys over
                for key in id_info:
                    new_dev[key] = id_info[key]
                devices.append(device(new_dev))
        else: # no ids field
            devices.append(device(dev))
    devices = sorted(devices, key=lambda k: k.module)
    return devices

def nested_get(input_dict, nested_key):
    """
    Retrieve the value of a nested dictionary key given the nested
    dictionary (input_dict) and the nested keys as a list (nested_key)
    """
    internal_dict_value = input_dict
    for k in nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return(None)
    return(internal_dict_value)

def get_tasmota_version():
    """
    Get the version number from tasmota repo
    """
    with open(os.path.join(tasmota_dir, "tasmota", 
                           "tasmota_version.h"), "r") as f:
        for line in f:
            match = re.match('.* VERSION = (0x[0-9A-Fa-f]+);', line)
            if match:
                return match.groups()[0];
    raise Exception('No tasmota version found.')

def choose_devices(devices, query=False):
    """
    Create list of menu choices from devices with category separators
    Optional param query: query and display device version numbers
    """
    # Style for selection interface
    style = style_from_dict({
        Token.Separator: '#FF00AA',
        Token.QuestionMark: '#00AAFF bold',
        Token.Selected: '#00AAFF',  # default
        Token.Pointer: '#00FF00 bold',
        Token.Instruction: '#FFAA00',  # default
        Token.Answer: '#00AAFF bold',
        Token.Question: '#FF00AA',
    })

    choice_list = []
    current_type = None
    name_len = max([len(dev.name) for dev in devices]) + 1

    if query:
        print('Querying all devices for version numbers. '
              'This may take a minute...')
        choice_list.append(Separator('Name'.center(name_len)
                                     + 'Firmware'.center(15)
                                     + 'Core'.center(7) + 'State'))
    for device in devices:
        if device['module'] != current_type:
            current_type = device['module']
            sep_str = ' {} '.format(current_type).center(name_len + 29, '=')
            choice_list.append(Separator(sep_str))
        if query and device.software == 'tasmota':
            device.query_tas_status()
            menu_text = device.f_name.ljust(name_len)
            if 'tas_version' in device.reported:
                menu_text += device.reported['tas_version'].ljust(15)
                menu_text += device.reported['core_version'].ljust(7)
                if device.reported['power'] is not None:
                    menu_text += device.reported['power']
            else:
                menu_text += 'Offline'
            choice_list.append({'name': menu_text, 'value': device['f_name']})
        else:
            choice_list.append({'name': device['f_name'],
                                'value': device['f_name']})

    # Ask the user to choose which devices to flash
    questions = [
        {
            'type': 'checkbox',
            'message': 'Select Devices',
            'name': 'device_selection',
            'choices': choice_list,
        }
    ]
    answers = prompt(questions, style=style)
    selected_devices = [device for device in devices if device['f_name'] \
                        in answers['device_selection']]
    return selected_devices

if __name__ == "__main__":
    print("Don't call espq directly")
    exit(1)
