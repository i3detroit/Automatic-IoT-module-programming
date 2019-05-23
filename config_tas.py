#!/usr/bin/env python3
"""
    Write the config file for a tasmota device with -d devicename
    or print a list of devices with --list
"""

import espq
import argparse

colors = {"RED": '\033[1;31m',
          "GREEN": '\033[1;32m',
          "NOCOLOR": '\033[0m'}

def fmtcols(mylist, cols):
    """
        Prints a list in a number of columns.
        From https://stackoverflow.com/a/24876899
    """
    maxwidth = max(list(map(lambda x: len(x), mylist)))
    justifyList = list(map(lambda x: x.ljust(maxwidth), mylist))
    lines = (' '.join(justifyList[i:i+cols])
             for i in range(0,len(justifyList),cols))
    print("\n".join(lines))

parser = argparse.ArgumentParser(description='Write user_config_override.h for tasmota device')
parser.add_argument('-n', '--device-name', dest='deviceName', action='store',
                    metavar='device_name', help='Device to write config from')
parser.add_argument('-l', '--list', dest='doList', action='store_true',
                     default=False, help='List available devices')
parser.add_argument('-d', '--device-file', dest='deviceFile', action='store',
                    metavar='device_file', help='JSON file with device definitions')
args = parser.parse_args()

devices = espq.import_devices(args.deviceFile)

if not args.deviceFile:
    print("Device file required with -d or --device-file")
    exit()

if args.doList == True:
    print("Device names in {device_file}".format(device_file=args.deviceFile))
    fmtcols(["{GREEN}{num:>3}{NOCOLOR} {d}".format(**colors, num=n, d=dev.name) for n, dev in enumerate(devices)], 3)

if not args.deviceName:
    print("\nChoose a device. Enter the number or name.")
    choice=input()
    if choice.isdigit():
        try:
            found = devices[int(choice)]
        except IndexError:
            print("Device number not found. Exiting.")
            exit()
    else:
        found = choice
else:
    for dev in devices:
        if args.deviceName == dev.name:
            found = dev
try:
    print("Writing config for {}".format(found.f_name))
    found.write_tasmota_config()
except:
    print("Device name was no found. Exiting.")
    exit()