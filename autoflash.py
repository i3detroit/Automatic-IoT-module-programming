#!/usr/bin/env python3
import os
import sys
import argparse;
from copy import deepcopy
from subprocess import call
from random import randint
import json
import re
import paho.mqtt.client as mqtt
import datetime


parser = argparse.ArgumentParser(description='Compile and flash ESPs')

parser.add_argument('-m', '--mode', dest='flashMode',
                    action='store', choices=('wifi', 'serial'),
                    default='serial',
                    help='set flash mode')
parser.add_argument('--no-online-check', dest='onlineCheck', action='store_false',
                     help='Don\'t check if it comes online')
parser.add_argument('--pause', dest='pauseBeforeFlash', action='store_true',
                     help='Ask for input before flashing')
parser.add_argument('-p', '--port', dest='serialPort', action='store',
                     default='/dev/ttyUSB0', help='Specify serial port to flash from')
parser.add_argument('-v', '--verbose', dest='verbosity', action='count',
                     default=0, help='Add verbosity')

# settings
logfile = "output.tsv"
dev_defs = "flash.json"
site_defs = "sites.json"
tasmotadir = "../Sonoff-Tasmota"
arduinoDir = "../esp-arduino";

# hardcodings
autoflashdir = os.path.dirname(os.path.abspath(__file__))
tasmotadir = autoflashdir + "/" + tasmotadir;
user_config_override =  tasmotadir + "/sonoff/user_config_override.h" #hardcoded from tasmota dir
buildDir = "/tmp/pio_custom_build";

waiting = True
status5Waiting = True


def on_message(mqclient, userdata, msg):
    global waiting
    global status5Waiting
    if(waiting and msg.topic.endswith('INFO2')):
        print("Device is back online after reboot.")
        waiting = False
    try:
        status = json.loads(msg.payload)
        if (status5Waiting and 'StatusNET' in status or ('Mac' in status and 'IPAddress' in status)):
            if('StatusNET' in status):
                deviceStatus="{userdata}, {ip}, {mac}".format(userdata=userdata,
                                                              ip=status['StatusNET']['IPAddress'],
                                                              mac=status['StatusNET']['Mac'])
            else:
                deviceStatus="{userdata}, {ip}, {mac}".format(userdata=userdata,
                                                              ip=status['IPAddress'],
                                                              mac=status['Mac']);
            print(deviceStatus);
            with open(autoflashdir + "/" + logfile, 'a') as output:
                    output.write("{}\n".format(deviceStatus));
            status5Waiting = False
    except ValueError:
        pass
    #else:
        #print("%s %s" % (msg.topic, msg.payload))


def site_pick(siteName, siteConfig):
    site = siteConfig[siteName]
    site['site_name'] = siteName;

    if not site:
        print("Error: Site not found in" + site_defs)
        exit()
    if not site['wifi_ssid']:
        print("Error: No wifi_ssid defined for site " + site["name"])
        exit()
    return site;


def list_gpios(request):
    lines=[]
    append=False
    with open(tasmotadir + "/sonoff/sonoff_template.h","r") as f:
        for line in f:
            if append==True:
                split = line.split("//")[0]
                subbed = re.sub("[\\s+,;}]","", split)
                lines.append(subbed)
            if "UserSelectablePins" in line:
                append=True
            if "}" in line:
                append=False
    gpios={}
    for num, gpio in enumerate(lines):
        gpios[gpio] = num
    return(gpios[request])


# returns bool success, err message
def handleMQTT(mqclient, dev, mqtt_host, onlineCheck):
    global waiting
    global status5Waiting

    topic = "{base}/{topic}".format(base=dev['mqtt']['base_topic'],
                                     topic=dev['mqtt']['topic'])
    subscribe_topics = ["stat/{topic}/+".format(topic=topic),
                        "tele/{topic}/+".format(topic=topic)]

    print("Waiting for {name} to reboot...".format(name=dev['name']))
    waiting = True
    status5Waiting = True
    mqclient.reinitialise()
    mqclient.on_message = on_message
    mqclient.connect(mqtt_host)
    for subscribe_topic in subscribe_topics:
        print("Watching for {subscribe_topic}".format(subscribe_topic=subscribe_topic))
        mqclient.subscribe(subscribe_topic)
    mqclient.user_data_set(dev['name']);
    starttime = datetime.datetime.now()
    while waiting and (datetime.datetime.now() - starttime).total_seconds() < 45:
        mqclient.loop(timeout=1.0)
    if waiting: # it didn't come online
        return False, "device {name} failed to come online in 45 seconds".format(name=dev['name'])
    else: #it did come online
        command_topic_base = "cmnd/{topic}/".format(topic=topic)
        print('it came online, trying to send commands');

        if(onlineCheck and status5Waiting):
            print('sending status5 command');
            statusCommand = command_topic_base + 'status'
            mqclient.publish(statusCommand, payload='5')
            mqclient.loop(timeout=1.0)
        else:
            status5Waiting = False

        if(dev['commands'] is not None):
            if(dev['software'] != 'tasmota'):
                print('trying to send commands to non-tasmota device. Please code this');
                sys.exit(1);
            # publish a list of commands with the Backlog command
            # see https://github.com/arendst/Sonoff-Tasmota/wiki/Commands#using-backlog
            backlogCommand = command_topic_base + 'Backlog'
            # join all commands with semicolons for backlog
            commands = []
            for c in dev['commands']:
                if 'GPIO' in c['command'] and 'GPIO' in c['payload']:
                    commands.append("{} {}".format(c['command'], list_gpios(c['payload'])))
                else:
                    commands.append("{} {}".format(c['command'], c['payload']))
            payload = '; '.join(commands)
            print("Publishing commands...")
            mqclient.publish(backlogCommand, payload=payload)
            mqclient.loop(timeout=1.0)

        # wait for status 5 response
        starttime = datetime.datetime.now()
        while status5Waiting and (datetime.datetime.now() - starttime).total_seconds() < 10:
            mqclient.loop(timeout=1.0)
        if status5Waiting: # didn't see responses
            return False, "device {devname} failed to report status".format(devname=dev['name'])

        mqclient.disconnect()

        return True, "Build, upload, came online success"

def programCustom(dev, site, args):
    topic = "{baseTop}/{topic}".format(baseTop=dev['mqtt']['base_topic'],
                                     topic=dev['mqtt']['topic'])
    buildFlags = ("-DWIFI_SSID=\\\\\\\"{ssid}\\\\\\\" "
                  "-DWIFI_PASSWORD=\\\\\\\"{passw}\\\\\\\" "
                  "-DNAME=\\\\\\\"{name}\\\\\\\" "
                  "-DTOPIC=\\\\\\\"{top}\\\\\\\"").format(ssid=site['wifi_ssid'],
                                                          passw=site['wifi_pass'],
                                                          name=dev['name'],
                                                          top=topic)
    #TODO: add build flags if there are any
    #if build_flags is not None:
    #    for flag in build_flags:
    #        buildFlags += "#define " + flag + "\n"
    codeDir = "../custom-mqtt-programs/{software}".format(software=dev['software'])


    if(args.flashMode == "serial"):
        options="--project-option=\"targets=upload\" --project-option=\"upload_port={serialPort}\"".format(serialPort=args.serialPort);
    elif(args.flashMode == "wifi"):
        options="--project-option=\"targets=upload\" --project-option=\"upload_protocol=espota\" --project-option=\"upload_port={serialPort}\"".format(serialPort=dev['hardware']['ip_addr']);

    else:
        print("no flash mode set, try again?")
        sys.exit(1)

    files="{codeDir}/thermostat.* {codeDir}/pins.h {codeDir}/doControl.* {codeDir}/i3Logo.h".format(codeDir=codeDir)

    command = ("PLATFORMIO_LIB_DIR=/home/mark/projects/esp/lib pio ci --project-option=\"build_flags = {buildFlags} "
               "-Wno-overflow -Wno-narrowing\" --board {board} {files} {options} --keep-build-dir "
               " ").format(buildFlags=buildFlags,
                                               files=files,
                                               options=options,
                                               board=dev['hardware']['board'],
                                               buildDir=buildDir)
    print(command);

    if(args.pauseBeforeFlash):
        os.system('bash -c "read -s -n 1 -p \'Press the any key to start flashing {name}...\'"'.format(name=dev['name']));
    return call(command, shell=True)


def programTasmota(dev, site, tasmota_blank_defines, args):
    site_info = ('#define MQTT_HOST "{}"\n#define SITE "{}"\n'
                 '#define STA_SSID1 "{}"\n#define STA_PASS1 "{}"').format(
                 site["mqtt_host"], site['site_name'],
                 site["wifi_ssid"], site["wifi_pass"])
    if 'wifi_ssid_alt' in site and 'wifi_pass_alt' in site:
        site_info = site_info + '\n#define STA_SSID1 "{}"\n#define STA_PASS1 "{}"'.format(
            site["wifi_ssid_alt"], site["wifi_pass_alt"])
    if 'ntp' in site:
        site_info = site_info + '\n#define NTP_SERVER1 "{}"'.format(site["ntp"])
    if "latitude" in site and "longitude" in site:
        site_info = site_info + '\n#define LATITUDE {}\n#define LONGITUDE {}'.format(
            site["latitude"], site["longitude"])

    # randomize the thing that tells tasmota to update the whole device config
    cfg_holder = str(randint(1, 32000))

    poweron_state = dev['tasmota']['poweron_state']


    full_topic = "%prefix%/{basetop}/%topic%/".format(basetop=dev['mqtt']['base_topic'])

    build_flags_text = ''
    if dev['build_flags'] is not None:
        for flag in dev['build_flags']:
            build_flags_text += "#define " + flag + "\n"

    device_name = re.sub(" ", "_", dev['name'])#apparently this might contain spaces?
    tasmota_defines = tasmota_blank_defines.format(device_name,
                                        str(datetime.datetime.now()),
                                        cfg_holder, dev['hardware']['module'], dev['mqtt']['group_topic'], full_topic,
                                        dev['mqtt']['topic'], dev['name'], poweron_state,
                                        site_info, build_flags_text)
    with open(user_config_override, "w") as defs_file:
        defs_file.write(tasmota_defines)


    # somehow flash shit
    if(args.flashMode == "serial"):
        port=args.serialPort
        pioEnv="sonoff-serial"
    elif(args.flashMode == "wifi"):
        port="{}/u2".format(dev['hardware']['ip_addr'])
        pioEnv="sonoff-wifi"
    else:
        print("no flash mode set, try again?")
        sys.exit(1)


    os.chdir(tasmotadir)
    build_result = call("pio run -e {}".format(pioEnv), shell=True)
    if(build_result != 0):
        print("failed to build");
        return build_result;
    if(args.pauseBeforeFlash):
        os.system('bash -c "read -s -n 1 -p \'Press the any key to start flashing {name}...\'"'.format(name=dev['name']));

    pio_call = "platformio run -e {} -t upload --upload-port {}".format(pioEnv, port)
    print("pio call: {}".format(pio_call))
    flash_result = call(pio_call, shell=True)
    return flash_result;

def programDevice(dev, siteConfig, tasmota_blank_defines, mqclient, args, id=None):
    #counter += 1


    # replace %id% with id number for devices with id
    if id:
        dev['name'] = re.sub("%id%", id['id'], dev['name'])
        dev['mqtt']['topic'] = re.sub("%id%", id['id'], dev['mqtt']['topic'])
        if 'ip_addr' in id:
            dev['hardware']['ip_addr'] = id['ip_addr'];
        if 'mac_addr' in id:
            dev['hardware']['mac_addr'] = id['mac_addr'];


    # Set the terminal title so you know what device is building
    #sys.stdout.write("\x1b]2({}/{}) - {}\x07".format(counter, len(deviceList), dev['name']))
    #print("({}/{}) - processing {})".format(counter, len(deviceList), dev['name']))
    print("({}/{}) - processing {})".format(42, 42, dev['name']))


    site = site_pick(dev['site'], siteConfig)


    flash_result = -1;
    if dev['software'] == 'tasmota':
        flash_result = programTasmota(dev, site, tasmota_blank_defines, args)
    else:
        flash_result = programCustom(dev, site, args)

    if flash_result == 0:
        #TODO: check if it comes online even if no commands

        # After flashing, if there are post flash commands,
        # wait until the device comes online and then send the commands
        if dev['commands'] is not None or args.onlineCheck:
            success, message = handleMQTT(mqclient, dev, site["mqtt_host"], args.onlineCheck)
            return success, dev['name'], message;
        else:
            return True, dev['name'], "Build and upload success with result code " + str(flash_result)


        print(dev['name'] + " done\n")
    # if build or upload failed, stop processing this device and move on
    else:
        return False, dev['name'], "Build or upload failure for {name} with result code {result}".format(name=dev['name'], result=str(flash_result))



def startFlashing(args):
    # populate siteConfig
    with open(autoflashdir + "/" + site_defs, "r") as f:
        siteConfig = json.load(f)

    # lists to store devices that fail or succeed at flashing
    failed = []
    passed = []

    mqclient = mqtt.Client(clean_session=True, client_id="autoflasher")

    # read in the devices yaml file and sort it by module for more efficient building
    with open(autoflashdir + "/" + dev_defs, "r") as f:
        deviceList = sorted(json.load(f), key=lambda k: k['hardware']['board'])
    tasmota_blank_defines = None;

    if any(filter(lambda dev: dev['software'] == 'tasmota', deviceList)):
        print('some device is tasmota');

        # check if platformio.ini is correct
        correctPIO=autoflashdir + "/platformio.ini";
        tasmotaPIO=tasmotadir + "/platformio.ini";
        os.system("bash -c 'cmp --silent {} {} || cp {} {}'".format(correctPIO, tasmotaPIO, correctPIO, tasmotaPIO))

        with open(autoflashdir + '/blank_defines.h','r') as f:
            tasmota_blank_defines = f.read()
    # end some device is tasmota

    if any(filter(lambda dev: dev['software'] != 'tasmota', deviceList)):
        print('some device is not custom');
        os.system("mkdir {buildDir}".format(buildDir=buildDir))





    #counter = 0
    for dev in deviceList:
        if 'ids' in dev:
            for id in dev['ids']:
                success, device, msg = programDevice(deepcopy(dev), siteConfig, tasmota_blank_defines, mqclient, args, id);
                print(msg);
                if success:
                    passed.append(device);
                else:
                    failed.append(device);
        else:
            success, device, msg = programDevice(dev, siteConfig, tasmota_blank_defines, mqclient, args);
            print(msg);
            if success:
                passed.append(device);
            else:
                failed.append(device);
    #end device loop

    if len(failed) > 0:
        with open(autoflashdir + "/error.log", "w+") as errorlog:
            errorlog.write(str(datetime.datetime.now()))
            errorlog.write("\nDevices did not flash:\n")
            errorlog.write("\n".join(failed))
            errorlog.write("\n");
    with open(autoflashdir + "/flashed.log", "w+") as flashlog:
        flashlog.write(str(datetime.datetime.now()))
        flashlog.write("\nDevices successfully flashed:\n")
        flashlog.write("\n".join(passed))
        flashlog.write("\n");

    print("Done with all devices. " + str(len(passed)) + " devices passed. " +
          str(len(failed)) + " errors detected")



if __name__ == "__main__":
    args = parser.parse_args()
    print(args);
    os.system('bash -c "read -s -n 1 -p \'Press the any key to continue if the settings look good\'"');
    #mqclient = mqtt.Client(clean_session=True)
    #dev = {
    #        "name": "light 052",
    #        "mqtt": {
    #            "base_topic": "i3/inside",
    #            "topic": "lights/052"
    #            },
    #        "commands": None,
    #        };
    #success, message = handleMQTT(mqclient, dev, '10.13.0.22', args.onlineCheck)
    #print(message);

    startFlashing(args)
