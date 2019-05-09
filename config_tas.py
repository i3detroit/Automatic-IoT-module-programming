#!/usr/bin/env python3
"""
    Write the config file for a tasmota device with -d devicename
    or print a list of devices with --list
"""

from espq import *
import argparse

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
parser.add_argument('-d', '--device', dest='device_name', action='store',
                     help='Specify device to write config from')
parser.add_argument('-l', '--list', dest='do_list', action='store_true',
                     default=False, help='List available devices')
args = parser.parse_args()

devices = import_devices()

if args.do_list == True:
    fmtcols([dev.name for dev in devices], 3)
    exit()

for dev in devices:
    if args.device_name == dev.name or args.device_name == dev.f_name:
        found = dev
try:
    print("Writing config for {}".format(found.f_name))
    found.write_tasmota_config()
except:
    print("Device name was no found. Try running with --list")
