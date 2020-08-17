#!/usr/bin/env python3

'''
    Query and print the status of tasmota devices
    User should set parameters current_version and good_core below
    for the desired versions of tasmota and esp arduino library.

'''


import argparse
import espq
from re import sub

# current version of tasmota, formatted as it is reported
current_version = '8.4.0(tasmota)'
# desired version of esp arduino library
good_core = ['2_7_2_1']

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
                          'badcore - device flashed with wrong '
                          'esp arduino version'))
args = parser.parse_args()

RED = '\033[1;31m'
GREEN = '\033[1;32m'
NOCOLOR = '\033[0m'

d = espq.import_devices(args.deviceFile)

name_len = max([len(dev.name) for dev in d])

for device in d:
    response = device.query_tas_status()
    offline = False
    if not bool(response):
        offline = True
    if "ip_addr" not in device:
        device.ip_addr = '';

    # Skip printing if the device does not meet filter requirements
    if args.filter == 'update' and (response['tas_version'] == current_version \
                                    or response['tas_version'] == ''):
        continue
    elif args.filter == 'offline' and response['ip'] != '':
        continue
    elif args.filter == 'online' and response['ip'] == '':
        continue
    elif args.filter == 'badip' and (response['ip'] == device.ip_addr or \
                                     response['ip'] == ''):
        continue
    elif args.filter == 'badcore' and (response['core_version'] in good_core \
                                       or response['core_version'] == ''):
        continue

    # Build formatted output lines one element at a time, 
    # Result should be someting like 'device_name      IP   MAC   6.5.0   2_3_0'
    # This is just super hard to work with
    # TODO: literally anything else
    if offline:
        print(RED + "{name}".format(name=device.name).ljust(name_len + 1)
              + "Offline{NOCOLOR}".format(NOCOLOR=NOCOLOR))
        continue

    if 'ip_addr' in device and response['ip'] == device.ip_addr:
        ip_color = NOCOLOR
    else:
        ip_color = RED

    tas_version_str = sub('\(tasmota\)|\(sonoff\)', '',
                          response['tas_version']).ljust(7)
    output_line = (GREEN
                   + device.name.ljust(name_len+1)
                   + ip_color
                   + response['ip'].ljust(16)
                   + NOCOLOR
                   + response['mac'].ljust(19)
                   + (RED if response['tas_version'] != current_version else '')
                   + tas_version_str
                   + NOCOLOR
                   + (RED if response['core_version'] not in good_core else '')
                   + response['core_version']
                   + NOCOLOR)
    print(output_line)
