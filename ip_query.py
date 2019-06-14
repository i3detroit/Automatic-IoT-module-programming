#!/usr/bin/env python3
import argparse
import espq
from re import sub

parser = argparse.ArgumentParser(description='Query status of tasmota devices',
                                 formatter_class=argparse.RawTextHelpFormatter,)
parser.add_argument('deviceFile', metavar='deviceFile',
                     help='What file to load device defs from')
parser.add_argument('-f','--filter',
                    dest='filter',
                    choices=('update', 'offline', 'online', 'badip', 'badcore'),
                    action='store',
                    help=('Optional list of filters:'
                          '  update  - old version, needs update'
                          '  offline - device does not respond'
                          '  online  - devices does respond'
                          '  badip   - device not at expected IP'
                          '  badcore - device flashed with wrong esp arduino version'))
args = parser.parse_args()

current_version = '6.5.0(sonoff)'
good_core = '2_3_0'  # desired version of esp arduino library

RED = '\033[1;31m'
GREEN = '\033[1;32m'
NOCOLOR = '\033[0m'

d=espq.import_devices(args.deviceFile)

name_len = max([len(dev.name) for dev in d])

for device in d:
    device.query_tas_status(espq.network_attr)
    device.query_tas_status(espq.firmware_attr)
    if args.filter == 'update' and (device.tas_version == current_version or device.tas_version == ''):
        continue
    elif args.filter == 'offline' and device.reported_ip != '':
        continue
    elif args.filter == 'online' and device.reported_ip == '':
        continue
    elif args.filter == 'badip' and (device.reported_ip == device.ip_addr or device.reported_ip == ''):
        continue
    elif args.filter == 'badcore' and (device.core_version == good_core or device.core_version == ''):
        continue
    output = [RED if device.reported_ip == '' else GREEN,
              device.name,
              NOCOLOR if device.reported_ip == device.ip_addr else RED,
              '\t'.expandtabs(name_len + 1 - len(device.name)),
              device.reported_ip,
              NOCOLOR if device.reported_ip != device.ip_addr else '',
              '\t'.expandtabs(17 - len(device.reported_ip)),
              device.reported_mac,
              '   ',
              RED if device.tas_version != current_version else '',
              sub('\(sonoff\)', '', device.tas_version),
              NOCOLOR,
              '   ',
              RED if device.core_version != good_core else '',
              device.core_version,
              NOCOLOR]
    print(''.join(output))
