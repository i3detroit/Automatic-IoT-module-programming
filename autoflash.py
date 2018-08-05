import os
import sys
from subprocess import call
from random import randint
import yaml
import re
import paho.mqtt.client as mqtt
import datetime


def on_message(mqclient, obj, msg):
    global waiting
    print("Device is back online after reboot.")
    waiting = False


def site_pick(site):
    mqtt_host = ''
    site_info = ''
    if site == 'i3':
        mqtt_host = "10.13.0.22"
        site_info = '''#define STA_SSID1 "i3detroit-iot"
#define STA_PASS1 "securityrisk"
#define STA_SSID2 "i3detroit"
#define STA_PASS2 ""
#define MQTT_HOST "{}"
#define NTP_SERVER1 "10.13.0.1"
#define SITE "i3"'''.format(mqtt_host)
    elif site == 'mike':
        mqtt_host = "{}"
        site_info = '''#define STA_SSID1 "Pleiades"
#define STA_PASS1 "VolleyBall19APotassium514Larsen974"
#define STA_SSID2 "i3detroit"
#define STA_PASS2 ""
#define MQTT_HOST "192.168.1.107"
#define NTP_SERVER1 "nl.pool.ntp.org"
#define SITE "MIKE"'''.format(mqtt_host)
    if site == 'mark':
        mqtt_host = "{}"
        site_info = '''#define STA_SSID1 "node42"
#define STA_PASS1 "we do what we must, because we can"
#define STA_SSID2 "i3detroit"
#define STA_PASS2 ""
#define MQTT_HOST "192.168.1.4"
#define NTP_SERVER1 "nl.pool.ntp.org"
#define SITE "MARK"'''.format(mqtt_host)
    return mqtt_host, site_info


mqclient = mqtt.Client(clean_session=True, client_id="autoflasher")

autoflashdir = "/home/mkfink/pio/autoflash"
tasmotadir = "/home/mkfink/pio/Sonoff-Tasmota"

dev_defs = "flash.yaml"
os.chdir(autoflashdir)
# read in the devices yaml file and sort it by module for more efficient building
with open(dev_defs, "r") as yamlfile:
    devicelist = sorted(yaml.load(yamlfile), key=lambda k: k['hardware']['module'])

os.chdir(tasmotadir)
defs_fn = "sonoff/user_config_override.h"

blank_defines = '''//{} generated on {}
#ifndef _USER_CONFIG_OVERRIDE_H_
#define _USER_CONFIG_OVERRIDE_H_

// force the compiler to show a warning to confirm that this file is inlcuded
//#warning **** user_config_override.h: Using Settings from this File ****

#define CFG_HOLDER {}
#define MODULE {}
#define MQTT_GRPTOPIC "{}"
#define MQTT_FULLTOPIC "{}"
#define MQTT_TOPIC "{}"
#define FRIENDLY_NAME "{}"
#define APP_POWERON_STATE {}
{}
{}
#endif  // _USER_CONFIG_OVERRIDE_H_
'''

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

    ip_addr = dev['hardware']['ip_addr']
    mac_addr = dev['hardware']['mac_addr']

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
    print("({}/{}) - processing{})".format(counter, len(devicelist), device_name))

    # generate topic of form 'tele/%device_topic%/INFO2'
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
    with open(defs_fn, "w") as defs_file:
        defs_file.write(defines_text)

    pio_call = "platformio run -e sonoff --upload-port {}/u2".format(ip_addr)
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
            print("Publishing commands...")
            for c in commands:
                mqclient.publish(c['topic'], payload=c['payload'])
                print(c['topic'] + " " + c['payload'])
            mqclient.loop(timeout=1.0)
            mqclient.disconnect()
        print(device_name + " done")
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

# client.disconnect()
print("Done with all devices. " + str(len(passed)) + " devices passed. " +
      str(len(failed)) + " errors detected")
