#!/usr/bin/env python3
import argparse
import espq
import os
from PyInquirer import style_from_dict, Token, prompt, Separator

# Style for selection interface
style = style_from_dict({
    Token.Separator: '#FF00AA',
    Token.QuestionMark: '#00AAFF bold',
    Token.Selected: '#00AAFF',  # default
    Token.Pointer: '#00FF00 bold',
    Token.Instruction: '#FFAA00',  # default
    Token.Answer: '#00AAFF bold',
    Token.Question: '#FF00AA',
})

colors = {"RED": '\033[1;31m',
          "GREEN": '\033[1;32m',
          "NOCOLOR": '\033[0m'}

# get terminal window size for pretty printing
try:
    cols, rows = os.get_terminal_size()
except:
    cols = 80
    rows = 40

parser = argparse.ArgumentParser(description='Parametrically generate home assistant config')
parser.add_argument('deviceFile', metavar='deviceFile',
                    help='What file to load device definitionss from')
args = parser.parse_args()

devices = espq.import_devices(args.deviceFile)
devices = sorted(devices, key=lambda k: k.f_name.lower())
devices = sorted(devices, key=lambda k: k.module)

selected_devices = espq.choose_devices(devices)

if len(selected_devices) == 0:
    print('No devices selected. Exiting.')
    exit()

# Do the flashing
for dev in selected_devices:
    # try:
        print("Writing {hass_template} config for {f_name}".format(**dev))
        dev.write_hass_config()
    # except KeyError:
    #     print('{f_name} has no hass template defined. Skipping.'.format(**dev))
print("Done.")

