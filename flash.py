#!/usr/bin/env python3
import argparse
import espq
import sys
import os
import re

def fmtcols(mylist, cols):
    """
        Prints a list in a number of columns.
        From https://stackoverflow.com/a/24876899
    """
    maxwidth = max(list(map(lambda x: len(x), mylist)))
    justifyList = list(map(lambda x: x.ljust(maxwidth), mylist))
    lines = (' '.join(justifyList[i:i + cols])
             for i in range(0, len(justifyList), cols))
    return("\n".join(lines))


def progress_report(devices):
    """ Print a list of devices and their flashing status """
    formatted_status = fmtcols(["[{status}] {d}".format(status = 'X' if dev.flashed == True else ' ', d=dev.name) for dev in devices], 3)
    print(re.sub('\[X\]', '[\033[1;32mX\033[0m]', formatted_status))
    print('=' * cols)

colors = {"RED": '\033[1;31m',
          "GREEN": '\033[1;32m',
          "NOCOLOR": '\033[0m'}

# get terminal window size for pretty printing
try:
    cols, rows = os.get_terminal_size()
except:
    cols = 80
    rows = 40

parser = argparse.ArgumentParser(description='Compile and flash ESPs')
parser.add_argument('-m', '--mode',
                    dest='flashMode',
                    action='store',
                    choices=('wifi', 'serial'),
                    default='serial',
                    help='set flash mode')
parser.add_argument('--no-online-check',
                    dest='onlineCheck',
                    action='store_false',
                    help='Don\'t check if it comes online')
parser.add_argument('--pause',
                    dest='pauseBeforeFlash',
                    action='store_true',
                    help='Ask for input before flashing')
parser.add_argument('-p', '--port',
                    dest='serialPort',
                    action='store',
                    default='/dev/ttyUSB0',
                    help='Specify serial port to flash from')
parser.add_argument('-v', '--verbose',
                    dest='verbosity',
                    action='count',
                    default=0,
                    help='Add verbosity')
parser.add_argument('deviceFile', metavar='deviceFile',
                    help='What file to load device defs from')
args = parser.parse_args()

devices = espq.import_devices(args.deviceFile)
selected_devices = espq.choose_devices(devices)

if len(selected_devices) == 0:
    print('No devices selected. Exiting.')
    exit()

print(args)
print('Devices to be flashed')
progress_report(selected_devices)
input('Press Enter to continue...')

# Do the flashing
for count, dev in enumerate(selected_devices, start=1):
    print("\nProgress report:")
    progress_report(selected_devices)
    # set terminal title to show progress
    sys.stdout.write(('\x1b]2Processing device {count}/{total} - {name}'
                      '\x07').format(count=count, total=len(selected_devices),
                                     name=dev.name))
    
    if hasattr(dev, 'flash_warning'):
        print('Ready to process device {count}/{total} - {name}'.format(count=count,
                                                                        total=len(selected_devices),
                                                                        name=dev.name))
        print('{RED}WARNING: {flash_warning}{NOCOLOR}'.format(flash_warning=dev.flash_warning, **colors))
        input('Press Enter to ignore the warning and continue...')
    elif args.pauseBeforeFlash == True:
        print('Ready to process device {count}/{total} - {name}'.format(count=count,
                                                                  total=len(selected_devices),
                                                                  name=dev.name))
        input('Press Enter to continue...')
    else:
        print('Processing device {count}/{total} - {name}'.format(count=count,
                                                                  total=len(selected_devices),
                                                                  name=dev.name))
    dev.flash(args.flashMode, args.serialPort)
    # reset terminal title to something useful like hostname
    sys.stdout.write('\x1b]2{hostname}\x07'.format(hostname=os.uname()[1]))

print("\nResult report:")
progress_report(selected_devices)
print("Done.")
