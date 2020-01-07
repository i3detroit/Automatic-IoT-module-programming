#!/usr/bin/env python3

'''
    Query and print the status of tasmota devices
    User should set parameters current_version and good_core below
    for the desired versions of tasmota and esp arduino library.

'''


import argparse
import espq
from re import sub

current_version = '8.1.0(tasmota)'  # current version of tasmota, formatted as it is reported
good_core = ['2_6_1']  # desired version of esp arduino library

parser = argparse.ArgumentParser(description='Query status of tasmota devices',
                                 formatter_class=argparse.RawTextHelpFormatter,)
parser.add_argument('deviceFile', metavar='deviceFile',
                     help='What file to load device defs from')
parser.add_argument('-f','--filter',
                    dest='filter',
                    choices=('update', 'offline', 'online', 'badip', 'badcore'),
                    action='store',
                    metavar='X',
                    help=('where X can be any of these:\n'
                          'update  - is old version, needs update\n'
                          'offline - device does not respond\n'
                          'online  - devices does respond\n'
                          'badip   - device not at expected IP\n'
                          'badcore - device flashed with wrong esp arduino version'))
args = parser.parse_args()

RED = '\033[1;31m'
GREEN = '\033[1;32m'
NOCOLOR = '\033[0m'

d = espq.import_devices(args.deviceFile)

name_len = max([len(dev.name) for dev in d])

for device in d:
    network_response = device.query_tas_status(espq.network_attr)
    firmware_response = device.query_tas_status(espq.firmware_attr)

    offline = False;
    if not bool(network_response) or not bool(firmware_response):
        offline = True;

    # Skip printing if the device does not meet filter requirements
    if args.filter == 'update' and (firmware_response['tas_version'] == current_version or firmware_response['tas_version'] == ''):
        continue
    elif args.filter == 'offline' and network_response['reported_ip'] != '':
        continue
    elif args.filter == 'online' and network_response['reported_ip'] == '':
        continue
    elif args.filter == 'badip' and (network_response['reported_ip'] == device.ip_addr or network_response['reported_ip'] == ''):
        continue
    elif args.filter == 'badcore' and (firmware_response['core_version'] in good_core or firmware_response['core_version'] == ''):
        continue

    # Build formatted output lines one element at a time, join into string when done
    # Result should be someting like 'device_name      IP   MAC   6.5.0   2_3_0'
    # This is just super hard to work with and does the same check multiple times
    # TODO: literally anything else
    if offline:
        print("{RED}{name} is offline{NOCOLOR}".format(name=device.name, RED=RED, NOCOLOR=NOCOLOR));
        continue;
    output = [RED if network_response['reported_ip'] == '' else GREEN,
              device.name,
              NOCOLOR if 'ip_addr' in device and network_response['reported_ip'] == device.ip_addr else RED,
              '\t'.expandtabs(name_len + 1 - len(device.name)),
              network_response['reported_ip'],
              NOCOLOR if 'ip_addr' in device and network_response['reported_ip'] != device.ip_addr else '',
              '\t'.expandtabs(17 - len(network_response['reported_ip'])),
              network_response['reported_mac'],
              '   ',
              RED if firmware_response['tas_version'] != current_version else '',
              sub('\(tasmota\)|\(sonoff\)', '', firmware_response['tas_version']),
              NOCOLOR,
              '   ',
              RED if firmware_response['core_version'] not in good_core else '',
              firmware_response['core_version'],
              NOCOLOR]
    print(''.join(output))
