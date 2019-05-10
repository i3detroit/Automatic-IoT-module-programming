#!/usr/bin/env python3
import argparse
import espq
from re import sub

parser = argparse.ArgumentParser(description='Query status of tasmota devices')
parser.add_argument('deviceFile', metavar='deviceFile',
                     help='What file to load device defs from')
args = parser.parse_args()


RED = '\033[1;31m'
GREEN = '\033[1;32m'
NOCOLOR = '\033[0m'

d=espq.import_devices(args.deviceFile)

name_len = max([len(dev.name) for dev in d])

for device in d:
    device.query_tas_status(espq.network_attr)
    device.query_tas_status(espq.firmware_attr)
    output = [GREEN if device.reported_ip == device.ip_addr else RED,
              device.name,
              NOCOLOR if device.reported_ip == device.ip_addr else '',
              '\t'.expandtabs(name_len + 1 - len(device.name)),
              device.reported_ip,
              NOCOLOR if device.reported_ip != device.ip_addr else '',
              '\t'.expandtabs(17 - len(device.reported_ip)),
              device.reported_mac,
              '   ',
              sub('\(sonoff\)', '', device.tas_version),
              '   ',
              device.core_version]
    print(''.join(output))
