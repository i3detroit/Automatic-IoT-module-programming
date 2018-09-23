#!usr/bin/env python
# Uses MQTT queries to get IP addresses of devies running sonoff-tasmota firmware
# Requires a yaml-formatted list of devies and their mqtt topics.
# topics are separated into base_topic (general) and topic (device specific)
import re
import yaml
import json
import datetime
import paho.mqtt.client as mqtt

loop_time, wait_time = 1.0, 1.0

RED = '\033[1;31m'
GREEN = '\033[1;32m'
NOCOLOR = '\033[0m'

def on_message(mqclient, userdata, msg):
    # The callback for when a PUBLISH message is received from the server.
    global ip_addr
    global mac_addr
    ip_addr = json.loads(msg.payload)['StatusNET']['IPAddress']
    mac_addr = json.loads(msg.payload)['StatusNET']['Mac']

def mqtt_ip_query(cmnd_topic, stat_topic, mqtt_host):
    global ip_addr, mac_addr
    mqclient = mqtt.Client(clean_session=True, client_id="ip_query")
    mqclient.reinitialise()
    mqclient.on_message = on_message
    mqclient.connect(mqtt_host)
    mqclient.subscribe(stat_topic)
    starttime = datetime.datetime.now()
    mqclient.publish(cmnd_topic, '5')
    while mac_addr == '' and (datetime.datetime.now() - starttime).total_seconds() < wait_time:
        mqclient.loop(timeout=loop_time)
    mqclient.disconnect()
    return ip_addr, mac_addr

def mqtt_list_ips(yamlf, mqtt_host):
    color=NOCOLOR
    global ip_addr, mac_addr
    found, not_found = 0, 0
    with open(yamlf, 'r') as yamlfile:
        devicelist = yaml.load(yamlfile)
    logf = open('ip.log', 'w')
    for dev in devicelist:
        if 'id' in dev:
            dev_topic = re.sub("%id%", dev['id'], dev['mqtt']['topic'])
            dev_name = re.sub("%id%", dev['id'], dev['name'])
        else:
            dev_topic = dev['mqtt']['topic']
            dev_name = dev['name']
        topic = dev['mqtt']['base_topic'] + '/' + dev_topic
        cmnd_topic = '{}/{}/{}'.format('cmnd', topic, 'status')
        stat_topic = '{}/{}/{}'.format('stat', topic, 'STATUS5')

        ip_addr, mac_addr = '', ''
        ip_addr, mac_addr = mqtt_ip_query(cmnd_topic, stat_topic, mqtt_host)

        if '10.13.107' not in ip_addr:
            found += 1
            output = (RED + dev_name + '\t' + ip_addr).expandtabs(37) + NOCOLOR + '\t' + mac_addr
        elif ip_addr and mac_addr:
            found += 1
            output = (dev_name + '\t' + GREEN + ip_addr).expandtabs(30) + '\t' + NOCOLOR + mac_addr
        else:
            not_found += 1
            output = RED + dev_name + NOCOLOR
        print(output)
        logf.write(output + '\n')
    logf.close()
    print("{} devices found. {} devices not found.".format(found, not_found))

if __name__ == "__main__":
    yamlf = 'tasmota.yaml'
    mqtt_list_ips(yamlf, "localhost")
