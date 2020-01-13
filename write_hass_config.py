#!/usr/bin/env python3
import argparse
import espq

parser = argparse.ArgumentParser(description='Parametrically generate home '
                                             'assistant config files')
parser.add_argument('deviceFile', metavar='deviceFile',
                    help='What file to load device definitionss from')
args = parser.parse_args()

devices = espq.import_devices(args.deviceFile)
# filter out devices that aren't configured
devices = [dev for dev in devices if hasattr(dev, 'hass_template')
                                     and hasattr(dev, 'hass_domain')]
devices = sorted(devices, key=lambda k: k.f_name.lower())
devices = sorted(devices, key=lambda k: k.module)

selected_devices = espq.choose_devices(devices)

if len(selected_devices) == 0:
    print('No devices selected. Exiting.')
    exit()

# Do the flashing
for dev in selected_devices:
    print("Writing {hass_template} config for {f_name}".format(**dev))
    dev.write_hass_config()
print("Done.")

