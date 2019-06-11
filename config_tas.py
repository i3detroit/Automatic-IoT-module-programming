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
    lines = (' '.join(justifyList[i:i + cols])
             for i in range(0, len(justifyList), cols))
    print("\n".join(lines))


def take_input():
    choice=input()
    if choice.isdigit() and int(choice) in range(len(devices)):
        return devices[int(choice)]
    else:
        print("Device number not found. Try again.")
        return take_input()

parser = argparse.ArgumentParser(description='Write user_config_override.h for tasmota device')
parser.add_argument('deviceFile', metavar='deviceFile',
                    help='JSON file to load device defs from')
args = parser.parse_args()

devices = espq.import_devices(args.deviceFile)

if not args.deviceFile:
    print("Device file required as an argument")
    exit()

print("Devices in {device_file}: ".format(device_file=args.deviceFile))
fmtcols(["{GREEN}{num:>3}{NOCOLOR} {d}".format(**colors, num=n, d=dev.name) for n, dev in enumerate(devices)], 3)

print('------------------------------------------')
print('Choose a device. Enter the number or name.')

found = take_input()
print("Writing config for {}".format(found.f_name))
found.write_tasmota_config()
