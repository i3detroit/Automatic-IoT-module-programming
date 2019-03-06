# A script for autoprogramming a bunch of sonoffs

Setup:

```
pip install -r requirements.txt
```

This requires git@github.com:i3detroit/Sonoff-Tasmota.git on branch `newi3` right now, will probably be `i3` soon.
It needs a hardcoded path in autoflash.py, this will be changed.

Device specific information is located in tasmota.yaml. Modules are flashed based on IP. All tasmota devices should have static IPs when on the IoT VLAN (10.13.107.x).
Use `mqtt_query_ip.py` to verify all device IPs, in case some devices have have failed over to the normal LAN.

Copy the devices you want to flash to flash.yaml and run autoflash.py.
Script will compile and OTA flash the device. If any post-flash commands are defined, it will watch MQTT for the device to come back online after flashing and then run the post-flash commands.
Then it will move on to the next device.


`blank_defines.h` undefines all of tasmotas config and lets us set what we want.
It's processed by python's .format to insert some specific settings near the bottom.


# To program custom devices
look at the `custom-devices` branch.
