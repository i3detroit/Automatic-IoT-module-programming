#!/usr/bin/env python3
import espq

RED = '\033[1;31m'
GREEN = '\033[1;32m'
NOCOLOR = '\033[0m'

d=espq.import_devices('tasmota.json')
for device in d:
    device.query_tas_status(espq.network_attr)
    if device.reported_ip == device.ip_addr:
        print(('{GREEN}{name}{NOCOLOR}\t{reported_ip}\t'
               '{reported_mac}'.format(GREEN=GREEN,
                                       NOCOLOR=NOCOLOR,
                                       **device)))
    else:
        print(('{RED}{name}\t{reported_ip}{NOCOLOR}\t'
               '{reported_mac}'.format(RED=RED,
                                       NOCOLOR=NOCOLOR,
                                       **device)))
