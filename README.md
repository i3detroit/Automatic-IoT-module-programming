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

# Device configuration file explanation
## name
Friendly name of device.

## software
What to program the device with. Can be 'tasmota' or a custom program's directory.

## site
Site name from sites.json, which should include location specific options (wifi info, etc.)

## module
For tasmota, should be one of the supported hardware modules (https://github.com/arendst/Sonoff-Tasmota/blob/development/sonoff/sonoff_template.h
##L328) such as SONOFF_BASIC, SONOFF_TOUCH, WEMOS. For custom programs, see instructions

## board
Type of esp board. esp01_1m for tasmota. Usually d1_mini, nodemcuv2, etc. for custom.

## hass_template
(Optional) Which template file to use from ./hass_templates (light, light_rgb, generic, etc.) 

## hass_domain
(Optional) Type of devive in home assistant: light, sensor, switch, etc.

## base_topic, topic
The full MQTT topic will be `%prefix%/{base_topic}/{topic}`

## group_topic
(Optional) The full MQTT group topic will be `%prefix%/{base_topic}/{group_topic}`

## poweron_state
0 - Leave the relay off when device is plugged in
1 - Switch the relay on when device is plugged in

## build_flags
(Optional) List of flags to pass when compiling. Useful for enabling tasmota features (i.e. `"USE_RULES"`) or passing other options/defines to custom programs (i.e. `"-DTOPIC_0_TOPIC=\\\"i3/inside/light\\\"`)

## commands
(Optional) List of command/payload pairs. MQTT commands to be executed when the device comes online after flashing. Useful for setting tasmota options (i.e. `{"command": "GPIO2", "payload": "GPIO_SWT1"}`)

## ids
(Optional) List of json objects containing 'id' and other parameters. Useful for when many devices are identical except for name (i.e. Light 001, Light 002 or Light East, Light West). The string '%id%' may be used in device parameters (such as name & topic) and duplicates of the device will be created for all ids listed. Other parameters such as group_topic can be included in the id object. For example `{"name": "light %id%", "topic": "lights/%id%", "ids": [{"id": "001", "ip_addr": "10.13.107.133", "group_topic": "lights/row1"}, {"id": "006", "ip_addr": "10.13.107.135", "group_topic": "lights/row2"}]}`