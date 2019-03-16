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
dev_defs = "flash.yaml"
site_defs = "sites.json"
tasmotadir = "../Sonoff-Tasmota.original"
pauseBeforeFlash = True;
flash_mode = "serial"
#flash_mode = "wifi"

# hardcodings
autoflashdir = os.path.dirname(os.path.abspath(__file__))
user_config_override = "./sonoff/user_config_override.h" #hardcoded from tasmota dir

global waiting;
waiting = True


def on_message(mqclient, obj, msg):
    print("Device is back online after reboot.")
    waiting = False


def site_pick(siteName, siteConfig):
    site = siteConfig[siteName];

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

def startFlashing():
    # populate siteConfig
    with open(autoflashdir + "/" + site_defs, "r") as f:
        siteConfig = json.load(f)

    os.chdir(tasmotadir)
    call("sed -i 's/build_flags *= ${core_active.build_flags}/build_flags = ${core_active.build_flags} -DUSE_CONFIG_OVERRIDE/' platformio.ini", shell=True);

    mqclient = mqtt.Client(clean_session=True, client_id="autoflasher")

    # read in the devices yaml file and sort it by module for more efficient building
    with open(autoflashdir + "/" + dev_defs, "r") as yamlfile:
        devicelist = sorted(yaml.load(yamlfile), key=lambda k: k['hardware']['module'])

    with open(autoflashdir + '/blank_defines.h','r') as f:
        blank_defines = f.read()

    # lists to store devices that fail or succeed at flashing
    failed = []
    passed = []


    # randomize the thing that tells tasmota to update the whole device config
    cfg_holder = str(randint(1, 32000))
    counter = 0
    for dev in devicelist:
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
        poweron_state = dev['tasmota']['poweron_state']

        # replace %id% with id number for devices with id
        if 'id' in dev:
            device_name = re.sub("%id%", dev['id'], device_name)
            topic = re.sub("%id%", dev['id'], topic)
            friendly_name = re.sub("%id%", dev['id'], friendly_name)
        device_name = re.sub(" ", "_", device_name)

        # Set the terminal title so you know what device is building
        sys.stdout.write("\x1b]2;({}/{}) - {}\x07".format(counter, len(devicelist), device_name))
        print("({}/{}) - processing {})".format(counter, len(devicelist), device_name))

        # generate topic of form tele/%device_topic%/INFO2
        subscribe_topic = re.sub('%topic%', topic,
                                 re.sub('%prefix%', 'tele', full_topic)) + 'INFO2'

        commands = dev['commands']

        build_flags_text = ''
        if dev['build_flags'] is not None:
            build_flags = dev['build_flags']
            for flag in build_flags:
                build_flags_text += "#define " + flag + "\n"

        mqtt_host, site_info = site_pick(site, siteConfig)

        defines_text = blank_defines.format(device_name, str(datetime.datetime.now()),
                                            cfg_holder, module, group_topic, full_topic,
                                            topic, friendly_name, poweron_state,
                                            site_info, build_flags_text)
        with open(user_config_override, "w") as defs_file:
            defs_file.write(defines_text)


        # somehow flash shit
        if(flash_mode == "serial"):
            port="/dev/ttyUSB0";
            call("sed -i 's/;env_default = sonoff$/env_default = sonoff/; s/^upload_port  .*/upload_port  = \/dev\/ttyUSB0/; s/^extra_scripts  .*/extra_scripts  = pio\/strip-floats.py/' platformio.ini", shell=True);
        elif(flash_mode == "wifi"):
            port="{}/u2".format(ip_addr);
            call("sed -i 's/;env_default = sonoff$/env_default = sonoff/; s/^upload_port  .*/upload_port  = \/dev\/ttyUSB0/; s/^extra_scripts  .*/extra_scripts  = pio\/strip-floats.py, pio\/http-uploader.py/' platformio.ini", shell=True);
        else:
            print("no flash mode set, try again?");
            sys.exit(1);


        if(pauseBeforeFlash):
            os.system('bash -c "read -s -n 1 -p \'Press the any key to start flashing...\'"');

        pio_call = "platformio run -e sonoff -t upload --upload-port {}".format(port)
        print("pio call: {}".format(pio_call))
        flash_result = call(pio_call, shell=True)

        if flash_result == 0:
            #TODO: check if it comes online even if no commands

            # After flashing, if there are post flash commands,
            # wait until the device comes online and then send the commands
            if commands is not None:
                print("Watching for " + subscribe_topic)
                print("Waiting for " + device_name + " to reboot...")
                starttime = datetime.datetime.now()
                waiting = True
                mqclient.reinitialise()
                mqclient.on_message = on_message
                mqclient.connect(mqtt_host)
                mqclient.subscribe(subscribe_topic)
                while waiting and (datetime.datetime.now() - starttime).total_seconds() < 45:
                    mqclient.loop(timeout=1.0)
                if waiting:
                    print("device " + device_name + " failed to come online");
                    failed.append(device_name)
                else:
                    # publish a list of commands with the Backlog command
                    # see https://github.com/arendst/Sonoff-Tasmota/wiki/Commands#using-backlog
                    command_topic = re.sub('%topic%', topic,
                                             re.sub('%prefix%', 'cmnd', full_topic)) + 'Backlog'
                    # join all commands with semicolons
                    payload = '; '.join(c['command']+' '+ c['payload'] for c in commands)
                    print("Publishing commands...")
                    mqclient.publish(command_topic, payload=payload)
                    mqclient.loop(timeout=1.0)
                    mqclient.disconnect()
                    print("Build and upload success with result code " + str(flash_result))
                    passed.append(device_name)
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
    startFlashing();
