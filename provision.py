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
    maxwidth = max([len(x) for x in mylist])
    justifyList = [x.ljust(maxwidth) for x in mylist]
    lines = (' '.join(justifyList[i:i + cols])
             for i in range(0, len(justifyList), cols))
    return("\n".join(lines))


def progress_report(devices):
    """
    Print a list of devices and their flashing status
    """
    formatted_status = fmtcols(["[{status}] {d}".format(status = 'X' if \
        (dev.flashed and dev.online) else ' ', d=dev.name) \
        for dev in devices], 3)
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

parser = argparse.ArgumentParser(description='Queue up flashing or other '
                                             'operations on ESP8266 devices '
                                             'described in deviceFile.json')
parser.add_argument(dest='operation',
                    action='store',
                    choices=('flash', 'cmds', 'hass'),
                    default='flash',
                    help=('Operation performed (flash device(s), run setup '
                        'commands, or write home assistant configs)'))
parser.add_argument('deviceFile', metavar='deviceFile',
                    help='JSON file to load device configs from')
parser.add_argument('-m', '--mode',
                    dest='flashMode',
                    action='store',
                    choices=('wifi', 'serial'),
                    default='serial',
                    help='Set flash mode (serial or wifi OTA)')
parser.add_argument('--pause',
                    dest='pauseBeforeFlash',
                    action='store_true',
                    help='Pause and require input before flashing each device')
parser.add_argument('-p', '--port',
                    dest='serialPort',
                    action='store',
                    default=None,
                    help='Specify serial port to flash from')
parser.add_argument('-q', '--query',
                    dest='query',
                    action='store_true',
                    help='Query and display device version numbers before running the operation')
parser.add_argument('-a', '--all',
                    dest='process_all',
                    action='store_true',
                    help='Skip device selection & use all devices in file')
parser.add_argument('-r', '--retry',
                    dest='retry',
                    action='store_true',
                    help='Add optional retry after failed flash')

args = parser.parse_args()

espq.test_pio_version()

devices = espq.import_devices(args.deviceFile)
if args.process_all:
    selected_devices = devices
else:
    selected_devices = espq.choose_devices(devices, query=args.query)
if len(selected_devices) == 0:
    print('No devices selected. Exiting.')
    exit()

print(args)
print('Selected devices:')
progress_report(selected_devices)

if args.operation == 'hass':
    input('Ready to write home assistant configs to {dir}.\nPress Enter '
          'to continue...'.format(dir=espq.hass_output_dir))
    for dev in selected_devices:
        print("Writing {hass_template} config for {f_name}".format(**dev))
        dev.write_hass_config()

elif args.operation == 'cmds':
    input('Ready to run device setup commands.\nPress Enter to continue...')
    for dev in selected_devices:
        print("Running setup commands for {f_name}".format(**dev))
        dev.run_setup_commands()

elif args.operation == 'flash':
    input('Ready to flash devices. Press Enter to continue...')
    for count, dev in enumerate(selected_devices, start=1):
        device_words = {"count": count, "total": len(selected_devices),
                        "name": dev.f_name}
        # set terminal title to show progress
        sys.stdout.write(('\x1b]2Processing device {count}/{total} - {name}'
                          '\x07').format(**device_words))

        if hasattr(dev, 'flash_warning'):
            print('Ready to process device {count}/{total} - '
                  '{name}'.format(**device_words))
            print('{RED}WARNING: {flash_warning}'
                  '{NOCOLOR}'.format(flash_warning=dev.flash_warning,
                                     **colors))
            input('Press Enter to ignore the warning and continue...')

        elif args.pauseBeforeFlash:
            print('Ready to process device {count}/{total} - '
                  '{name}'.format(**device_words))
            input('Press Enter to continue...')

        else:
            print('Processing device {count}/{total} - '
                  '{name}'.format(**device_words))
        dev.flash(args.flashMode, args.serialPort)
        while args.retry is True and dev.flashed is False:
            retry = input('{name} flash failed. Retry (y/n)?'.format(**device_words))
            if retry == 'y' or retry == 'Y':
                dev.flash(args.flashMode, args.serialPort)
            elif retry == 'n' or retry == 'N':
                break
            else:
                print('Invalid input. Enter "y" or "n".')

        # reset terminal title to something useful like hostname
        sys.stdout.write('\x1b]2{hostname}\x07'.format(hostname=os.uname()[1]))
    print("\nResult report:")
    progress_report(selected_devices)

print("Done.")
