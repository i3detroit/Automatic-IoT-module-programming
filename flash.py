#!/usr/bin/env python3
import argparse
import espq

parser = argparse.ArgumentParser(description='Compile and flash ESPs')

parser.add_argument('-m', '--mode', dest='flashMode',
                    action='store', choices=('wifi', 'serial'),
                    default='serial',
                    help='set flash mode')
parser.add_argument('--no-online-check', dest='onlineCheck', action='store_false',
                     help='Don\'t check if it comes online')
parser.add_argument('--pause', dest='pauseBeforeFlash', action='store_true',
                     help='Ask for input before flashing')
parser.add_argument('-p', '--port', dest='serialPort', action='store',
                     default='/dev/ttyUSB0', help='Specify serial port to flash from')
parser.add_argument('-v', '--verbose', dest='verbosity', action='count',
                     default=0, help='Add verbosity')
parser.add_argument('deviceFile', metavar='deviceFile',
                     help='What file to load device defs from')

args = parser.parse_args()
print(args);
input("Press Enter to continue...")

devices = espq.import_devices(args.deviceFile)

for dev in devices:
    dev.flash(args.flashMode, args.serialPort)
