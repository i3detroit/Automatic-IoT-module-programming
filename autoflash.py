#!/usr/bin/env python
import os
import sys
from subprocess import call
from random import randint
import yaml
import re
import paho.mqtt.client as mqtt
import datetime

autoflashdir = os.path.dirname(os.path.abspath(__file__))
dev_defs = "flash.yaml"
site_defs = "sites.yaml"
tasmotadir = "../Sonoff-Tasmota"
tas_defs = tasmotadir + "/sonoff/user_config_override.h"

def on_message(mqclient, obj, msg):
    global waiting
    print("Device is back online after reboot.")
    waiting = False


def site_pick(sitename, site_defs=site_defs):
    with open(site_defs, "r") as siteyaml:
        siteslist = sorted(yaml.load(siteyaml))

    site = next((s for s in siteslist if s['name'] == sitename), None)

    if not site:
        print("Error: Site not found in" + site_defs)
        exit()
    if not site['wifi_ssid']:
        print("Error: No wifi_ssid defined for site " + site["name"])
        exit()
    site_info = ('#define MQTT_HOST "{}"\n#define SITE "{}"\n'
                 '#define STA_SSID1 "{}"\n#define STA_PASS1 "{}"').format(
                 site["mqtt_host"], site["name"],
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


mqclient = mqtt.Client(clean_session=True, client_id="autoflasher")

os.chdir(autoflashdir)
# read in the devices yaml file and sort it by module for more efficient building
with open(dev_defs, "r") as yamlfile:
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
    os.chdir(autoflashdir)
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

    mqtt_host, site_info = site_pick(site)

    defines_text = blank_defines.format(device_name, str(datetime.datetime.now()),
                                        cfg_holder, module, group_topic, full_topic,
                                        topic, friendly_name, poweron_state,
                                        site_info, build_flags_text)
    with open(tas_defs, "w") as defs_file:
        defs_file.write(defines_text)
    os.chdir(tasmotadir)
    pio_call = "platformio run -e sonoff -t upload --upload-port {}/u2".format(ip_addr)
    print("pio call: {}".format(pio_call))
    flash_result = call(pio_call, shell=True)

    if flash_result == 0:
        print("Build and upload success with result code " + str(flash_result))
        passed.append(device_name)

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

        print(device_name + " done\n")
    # if build or upload failed, stop processing this device and move on
    else:
        print("Build or upload failure for " + device_name +
              " with result code " + str(flash_result))
        failed.append(device_name)

if len(failed) > 0:
    with open("error.log", "w") as errorlog:
        errorlog.write(str(datetime.datetime.now()))
        errorlog.write("\nDevices did not flash:\n")
        errorlog.write("\n".join(failed))
with open("flashed.log", "w") as flashlog:
    flashlog.write(str(datetime.datetime.now()))
    flashlog.write("\nDevices successfully flashed:\n")
    flashlog.write("\n".join(passed))

print("Done with all devices. " + str(len(passed)) + " devices passed. " +
      str(len(failed)) + " errors detected")
