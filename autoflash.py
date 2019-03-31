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
    try:
        status = json.loads(msg.payload);
    except ValueError:
        pass

    if(waiting and msg.topic.endswith('INFO2')):
        print("Device is back online after reboot.")
        waiting = False

    if (status5Waiting and 'StatusNET' in status or ('Mac' in status and 'IPAddress' in status)):
        if('StatusNET' in status):
            print(f"{userdata}, {status['StatusNET']['IPAddress']}, {status['StatusNET']['Mac']}");
        else:
            print(f"{userdata}, {status['IPAddress']}, {status['Mac']}");
        status5Waiting = False
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

# returns bool success, err message
def handleMQTT(mqclient, dev, mqtt_host, onlineCheck):
    global waiting
    global status5Waiting

    topic = f"{dev['mqtt']['base_topic']}/{dev['mqtt']['topic']}"
    subscribe_topic = f"+/{topic}/+"

    print(f"Watching for {subscribe_topic}")
    print(f"Waiting for {dev['name']} to reboot...")
    waiting = True
    status5Waiting = True
    mqclient.reinitialise()
    mqclient.on_message = on_message
    mqclient.connect(mqtt_host)
    mqclient.subscribe(subscribe_topic)
    mqclient.user_data_set(dev['name']);
    starttime = datetime.datetime.now()
    while waiting and (datetime.datetime.now() - starttime).total_seconds() < 45:
        mqclient.loop(timeout=1.0)
    if waiting: # it didn't come online
        return False, f"device {dev['name']} failed to come online in 45 seconds"
    else: #it did come online
        command_topic_base = f"cmnd/{topic}/"
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
            return False, f"device {dev['name']} failed to report status"

        mqclient.disconnect()

        return True, "Build, upload, came online success"

def programCustom(dev, site):
    topic = f"{dev['mqtt']['base_topic']}/{dev['mqtt']['topic']}"
    buildFlags = f"-DWIFI_SSID=\\\\\\\"{site['wifi_ssid']}\\\\\\\" -DWIFI_PASSWORD=\\\\\\\"{site['wifi_pass']}\\\\\\\" -DNAME=\\\\\\\"{dev['name']}\\\\\\\" -DTOPIC=\\\\\\\"{topic}\\\\\\\"";
    print(buildFlags);
    #TODO: add build flags if there are any
    #if build_flags is not None:
    #    for flag in build_flags:
    #        buildFlags += "#define " + flag + "\n"
    codeDir = f"../custom-mqtt-programs/{dev['software']}";


    if(flash_mode == "serial"):
        options="--project-option=\"targets=upload\" --project-option=\"upload_port=/dev/ttyUSB0\""
    elif(flash_mode == "wifi"):
        options="--project-option=\"targets=upload\" --project-option=\"upload_protocol=espota\" --project-option=\"upload_port=10.13.5.3\""

    else:
        print("no flash mode set, try again?")
        sys.exit(1)

    files=f"{codeDir}/thermostat.* {codeDir}/pins.h {codeDir}/doControl.* {codeDir}/i3Logo.h"

    command = f"PLATFORMIO_LIB_DIR=/home/mark/projects/esp/lib pio ci --project-option=\"build_flags = {buildFlags} -Wno-overflow -Wno-narrowing\" --board {dev['hardware']['board']} {files} {options} --keep-build-dir --build-dir {buildDir}";
    print(command);

    if(pauseBeforeFlash):
        os.system('bash -c "read -s -n 1 -p \'Press the any key to start flashing...\'"')
    return call(command, shell=True)


def programTasmota(dev, site, tasmota_blank_defines):
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


    full_topic = f"%prefix%/{dev['mqtt']['base_topic']}/%topic%/"

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
    build_result = call("pio run -e {}".format(pioEnv), shell=True)
    if(build_result != 0):
        print("failed to build");
        return build_result;
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
        deviceList = sorted(json.load(f), key=lambda k: k['hardware']['board'])

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
        os.system(f"mkdir {buildDir}")



    # lists to store devices that fail or succeed at flashing
    failed = []
    passed = []


    counter = 0
    for dev in deviceList:
        counter += 1
        try:
            ip_addr = dev['hardware']['ip_addr']
            mac_addr = dev['hardware']['mac_addr']
        except ValueError:
            pass


        # replace %id% with id number for devices with id
        if 'id' in dev:
            dev['name'] = re.sub("%id%", dev['id'], dev['name'])
            dev['mqtt']['topic'] = re.sub("%id%", dev['id'], dev['mqtt']['topic'])


        # Set the terminal title so you know what device is building
        sys.stdout.write("\x1b]2({}/{}) - {}\x07".format(counter, len(deviceList), dev['name']))
        print("({}/{}) - processing {})".format(counter, len(deviceList), dev['name']))


        site = site_pick(dev['site'], siteConfig)


        flash_result = -1;
        if dev['software'] == 'tasmota':
            flash_result = programTasmota(dev, site, tasmota_blank_defines)
        else:
            flash_result = programCustom(dev, site)

        if flash_result == 0:
            #TODO: check if it comes online even if no commands

            # After flashing, if there are post flash commands,
            # wait until the device comes online and then send the commands
            if dev['commands'] is not None or onlineCheck:
                success, message = handleMQTT(mqclient, dev, site["mqtt_host"], onlineCheck)
                print(message)
                if(success):
                    passed.append(dev['name'])
                else:
                    failed.append(dev['name'])
            else:
                print("Build and upload success with result code " + str(flash_result))
                passed.append(dev['name'])


            print(dev['name'] + " done\n")
        # if build or upload failed, stop processing this device and move on
        else:
            print(f"Build or upload failure for {dev['name']}"
                  " with result code " + str(flash_result))
            failed.append(dev['name'])
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
    #mqclient = mqtt.Client(clean_session=True)
    #dev = {
    #        "name": "thermostat",
    #        "mqtt": {
    #            "base_topic": "i3/dev",
    #            "topic": "thermostat"
    #            },
    #        "commands": None,
    #        };
    #success, message = handleMQTT(mqclient, dev, '10.13.0.22', onlineCheck)
    #print(message);
    startFlashing()
