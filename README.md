# A script for autoprogramming a bunch of sonoffs

Setup:

```
pip install -r requirements.txt
```

Make sure local directories and tasmota version are set correctly at the top of espq.py
This is written expecting a directoy setup like:
.
./Automatic-IoT-module-programming
./Sonoff-Tasmota
./Sonoff-Tasmota/sonoff
./custom-mqtt-programs
./custom-mqtt-programs/name-of-program

# To program tasmota devices
1. Create a device configuration file for your device(s) as in tasmota.json.
    - Each device can be a single device or many identical devices which only differ by some %id% string.
2. Run flash.py.

`blank_defines.h` undefines all of tasmota's config and lets us set what we want.
It's processed by python's .format to insert some specific settings near the bottom.
A version of 'platformio.ini' is provided here to be used with tasmota. The flashing script copies it to the correct location as needed.

# To program custom devices
1. Create a device configuration file for your custom device(s) as in custom.json. Software should be the parent folder. Module should be the name of the program itself. (i.e. you would have your program stored as ./software/module/module.ino). As above, %id% can be used for identical devices.
2. Run flash.py.

# Other Stuff
- Query tasmota device status (IP, MAC, tasmota version, core version) with ip_query.py.
- Write user_config_override.h for a tasmota device with config_tas.py.
- Home assistant configuration files can be generated via espq.write_hass_config().
