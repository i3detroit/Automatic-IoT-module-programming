#!/usr/bin/env python3
import os
import sys
from subprocess import call
from random import randint
import yaml
import json
import re
import paho.mqtt.client as mqtt
import datetime

# settings
pauseBeforeFlash = True
onlineCheck = True
flash_mode = "serial"
#flash_mode = "wifi"

dev_defs = "flash.json"
site_defs = "sites.json"
tasmotadir = "../Sonoff-Tasmota.original"

# hardcodings
autoflashdir = os.path.dirname(os.path.abspath(__file__))
tasmotadir = autoflashdir + "/" + tasmotadir;
user_config_override =  tasmotadir + "/sonoff/user_config_override.h" #hardcoded from tasmota dir

waiting = True
status5Waiting = True


def on_message(mqclient, userdata, msg):
    global waiting
    global status5Waiting
    if(msg.topic.endswith('INFO2')):
        print("Device is back online after reboot.")
        waiting = False
    elif (msg.topic.endswith('STATUS5')):
        status = json.loads(msg.payload);
        #print(status['StatusNET']['IPAddress']);
        #print(status['StatusNET']['Mac']);
        print("{}, {}, {}".format(userdata, status['StatusNET']['IPAddress'], status['StatusNET']['Mac']));
        status5Waiting = False
    #else:
        #print("%s %s" % (msg.topic, msg.payload))


def site_pick(siteName, siteConfig):
    site = siteConfig[siteName]

    if not site:
        print("Error: Site not found in" + site_defs)
        exit()
    if not site['wifi_ssid']:
        print("Error: No wifi_ssid defined for site " + site["name"])
        exit()
    site_info = ('#define MQTT_HOST "{}"\n#define SITE "{}"\n'
                 '#define STA_SSID1 "{}"\n#define STA_PASS1 "{}"').format(
                 site["mqtt_host"], siteName,
                 site["wifi_ssid"], site["wifi_pass"])
    if 'wifi_ssid_alt' in site and 'wifi_pass_alt' in site:
        site_info = site_info + '\n#define STA_SSID1 "{}"\n#define STA_PASS1 "{}"'.format(
            site["wifi_ssid_alt"], site["wifi_pass_alt"])
    if 'ntp' in site:
        site_info = site_info + '\n#define NTP_SERVER1 "{}"'.format(site["ntp"])
    if "latitude" in site and "longitude" in site:
        site_info = site_info + '\n#define LATITUDE {}\n#define LONGITUDE {}'.format(
            site["latitude"], site["longitude"])
    return site["mqtt_host"], site_info

# returns bool success, err message
def handleMQTT(mqclient, device_name, commands, mqtt_host, topic, full_topic, onlineCheck):
    global waiting
    global status5Waiting

    # generate topic of form tele/%device_topic%/INFO2
    subscribe_topic = re.sub('%topic%', topic,
                             re.sub('%prefix%', '+', full_topic)) + '+'

    print("Watching for " + subscribe_topic)
    print("Waiting for " + device_name + " to reboot...")
    waiting = True
    mqclient.reinitialise()
    mqclient.on_message = on_message
    mqclient.connect(mqtt_host)
    mqclient.subscribe(subscribe_topic)
    mqclient.user_data_set(device_name);
    starttime = datetime.datetime.now()
    while waiting and (datetime.datetime.now() - starttime).total_seconds() < 45:
        mqclient.loop(timeout=1.0)
    if waiting: # it didn't come online
        return False, "device " + device_name + " failed to come online in 45 seconds"
    else: #it did come online
        # publish a list of commands with the Backlog command
        # see https://github.com/arendst/Sonoff-Tasmota/wiki/Commands#using-backlog
        command_topic_base = re.sub('%topic%', topic,
                re.sub('%prefix%', 'cmnd', full_topic))
        print('it came online, trying to send commands');

        if(onlineCheck):
            print('sending status5 command');
            status5Waiting = True
            statusCommand = command_topic_base + 'status'
            mqclient.publish(statusCommand, payload='5')
            mqclient.loop(timeout=1.0)
        else:
            status5Waiting = False

        if(commands is not None):
            backlogCommand = command_topic_base + 'Backlog'
            # join all commands with semicolons
            payload = ' '.join(c['command']+' '+ c['payload'] for c in commands)
            print("Publishing commands...")
            mqclient.publish(backlogCommand, payload=payload)
            mqclient.loop(timeout=1.0)

        # wait for status 5 response
        starttime = datetime.datetime.now()
        while status5Waiting and (datetime.datetime.now() - starttime).total_seconds() < 10:
            mqclient.loop(timeout=1.0)
        if status5Waiting: # didn't see responses
            return False, "device " + device_name + " failed to report status"

        mqclient.disconnect()

        return True, "Build, upload, came online success"
def programTasmota(device_name, module, group_topic, full_topic, topic, friendly_name, site_info, build_flags, tasmota_config, tasmota_blank_defines):

    # randomize the thing that tells tasmota to update the whole device config
    cfg_holder = str(randint(1, 32000))

    poweron_state = tasmota_config['poweron_state']

    build_flags_text = ''
    if build_flags is not None:
        for flag in build_flags:
            build_flags_text += "#define " + flag + "\n"
    tasmota_defines = tasmota_blank_defines.format(device_name,
                                        str(datetime.datetime.now()),
                                        cfg_holder, module, group_topic, full_topic,
                                        topic, friendly_name, poweron_state,
                                        site_info, build_flags_text)
    with open(user_config_override, "w") as defs_file:
        defs_file.write(tasmota_defines)


    # somehow flash shit
    if(flash_mode == "serial"):
        port="/dev/ttyUSB0"
        pioEnv="sonoff-serial"
    elif(flash_mode == "wifi"):
        port="{}/u2".format(ip_addr)
        pioEnv="sonoff-wifi"
    else:
        print("no flash mode set, try again?")
        sys.exit(1)


    os.chdir(tasmotadir)
    call("pio run -e {}".format(pioEnv), shell=True)
    if(pauseBeforeFlash):
        os.system('bash -c "read -s -n 1 -p \'Press the any key to start flashing...\'"')

    pio_call = "platformio run -e {} -t upload --upload-port {}".format(pioEnv, port)
    print("pio call: {}".format(pio_call))
    flash_result = call(pio_call, shell=True)
    return flash_result;

def startFlashing():
    # populate siteConfig
    with open(autoflashdir + "/" + site_defs, "r") as f:
        siteConfig = json.load(f)



    mqclient = mqtt.Client(clean_session=True, client_id="autoflasher")

    # read in the devices yaml file and sort it by module for more efficient building
    with open(autoflashdir + "/" + dev_defs, "r") as f:
        deviceList = sorted(json.load(f), key=lambda k: k['hardware']['module'])

    someTasmota = any(filter(lambda dev: dev['hardware']['type'] == 'tasmota', deviceList))
    if someTasmota:
        print('some device is tasmota');

        # check if platformio.ini is correct
        correctPIO=autoflashdir + "/platformio.ini";
        tasmotaPIO=tasmotadir + "/platformio.ini";
        os.system("bash -c 'cmp --silent {} {} || cp {} {}'".format(correctPIO, tasmotaPIO, correctPIO, tasmotaPIO))

        with open(autoflashdir + '/blank_defines.h','r') as f:
            tasmota_blank_defines = f.read()
    # end some device is tasmota



    # lists to store devices that fail or succeed at flashing
    failed = []
    passed = []


    counter = 0
    for dev in deviceList:
        counter += 1
        device_name = dev['name']
        devtype = dev['hardware']['type']
        site = dev['hardware']['site']
        module = dev['hardware']['module']
        board = dev['hardware']['board']
        try:
            ip_addr = dev['hardware']['ip_addr']
            mac_addr = dev['hardware']['mac_addr']
        except ValueError:
            pass
        group_topic = dev['mqtt']['group_topic']
        full_topic = '%prefix%/{}/%topic%/'.format(dev['mqtt']['base_topic'])
        topic = dev['mqtt']['topic']

        friendly_name = dev['name']

        # replace %id% with id number for devices with id
        if 'id' in dev:
            device_name = re.sub("%id%", dev['id'], device_name)
            topic = re.sub("%id%", dev['id'], topic)
            friendly_name = re.sub("%id%", dev['id'], friendly_name)
        device_name = re.sub(" ", "_", device_name)

        # Set the terminal title so you know what device is building
        sys.stdout.write("\x1b]2({}/{}) - {}\x07".format(counter, len(deviceList), device_name))
        print("({}/{}) - processing {})".format(counter, len(deviceList), device_name))


        mqtt_host, site_info = site_pick(site, siteConfig)


        flash_result = -1;
        if 'tasmota' in dev:
            flash_result = programTasmota(device_name, module, group_topic, full_topic, topic, friendly_name, site_info, dev['build_flags'], dev['tasmota'], tasmota_blank_defines)
        else:
            print("device is not tasmota. Please write support for that");
            sys.exit(501);

        if flash_result == 0:
            #TODO: check if it comes online even if no commands

            # After flashing, if there are post flash commands,
            # wait until the device comes online and then send the commands
            if dev['commands'] is not None or onlineCheck:
                success, message = handleMQTT(mqclient, device_name, dev['commands'], mqtt_host, topic, full_topic, onlineCheck)
                print(message)
                if(success):
                    passed.append(device_name)
                else:
                    failed.append(device_name)
            else:
                print("Build and upload success with result code " + str(flash_result))
                passed.append(device_name)


            print(device_name + " done\n")
        # if build or upload failed, stop processing this device and move on
        else:
            print("Build or upload failure for " + device_name +
                  " with result code " + str(flash_result))
            failed.append(device_name)
    #end device loop

    if len(failed) > 0:
        with open(autoflashdir + "/error.log", "w") as errorlog:
            errorlog.write(str(datetime.datetime.now()))
            errorlog.write("\nDevices did not flash:\n")
            errorlog.write("\n".join(failed))
    with open(autoflashdir + "/flashed.log", "w") as flashlog:
        flashlog.write(str(datetime.datetime.now()))
        flashlog.write("\nDevices successfully flashed:\n")
        flashlog.write("\n".join(passed))

    print("Done with all devices. " + str(len(passed)) + " devices passed. " +
          str(len(failed)) + " errors detected")


if __name__ == "__main__":
    #mqclient = mqtt.Client(clean_session=True, client_id="autoflasher")
    #success, message = handleMQTT(mqclient, 'devce_name', None, '10.13.0.22', 'lights/001', '%prefix%/mark/basement/%topic%/', True)
    #print(success)
    #print(message)
    startFlashing()
