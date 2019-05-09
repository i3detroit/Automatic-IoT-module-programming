#!/usr/bin/env python3
from espq import *

RED = '\033[1;31m'
GREEN = '\033[1;32m'
NOCOLOR = '\033[0m'

d=import_devices()
for device in d:
    device.query_status5()
    if '10.13.107' in device.reported_ip:
        print(('{GREEN}{name}{NOCOLOR}\t{reported_ip}\t'
               '{reported_mac}'.format(GREEN=GREEN,
                                       NOCOLOR=NOCOLOR,
                                       **device)))
    else:
        print(('{RED}{name}\t{reported_ip}{NOCOLOR}\t'
               '{reported_mac}'.format(RED=RED,
                                       NOCOLOR=NOCOLOR,
                                       **device)))
