# A script for autoprogramming a bunch of sonoffs

Setup:

```
pip3 install -r requirements.txt
pip2 install pycurl
```

Make sure local directories and tasmota version are set correctly at the top of `espq.py`
This is written expecting a directoy setup like:
```
.
../Tasmota
../custom-mqtt-programs
../custom-mqtt-programs/name-of-program
```

Tasmota should be checked out to the tag or hash referenced in esqp.py where `current_tasmota_version` is defined.

Create a `config/sites.json` file for your location based on `config/sites.json.example`

# To program tasmota devices
1. Create a device configuration file for your device(s) as in tasmota.json.
    - Each device can be a single device or many identical devices which only differ by some %id% string.
2. Run `./provision.py flash [-m {wifi|serial}] [-p SERIALPORT] config/your_devices.json` (defaults to serial and /dev/ttyUSB0)

`blank_defines.h` undefines all of tasmota's config and lets us set what we want.
It's processed by python's .format to insert some specific settings near the bottom.
A version of `platformio_override.ini` is provided here to be used with tasmota. The flashing script copies it to the correct location as needed.

# To program custom devices
1. Create a device configuration file for your custom device(s) as in custom.json. Software should be the parent folder. Module should be the name of the program itself. (i.e. you would have your program stored as `./software/module/module.ino`). As above, `%id%` can be used for identical devices.
2. Run `./provision.py flash [-m {wifi|serial}] [-p SERIALPORT] config/your_devices.json` (defaults to serial and /dev/ttyUSB0)

# Other Stuff
- Query tasmota device status (IP, MAC, tasmota version, esp core version) with ip_query.py.
- Home assistant configuration files can be generated via `./provision.py hass config/your_devices.json`
- Run the setup commands from a device's config with `./provision.py cmds config/your_devices.json`

# Device configuration file explanation
## name
Friendly name of device.

## software
What to program the device with. Can be 'tasmota' or a custom program's directory.

## site
Site name from sites.json, which should include location specific options (wifi info, etc.)

## module
For tasmota, should be one of the [supported hardware modules](https://github.com/arendst/Tasmota/blob/development/tasmota/tasmota_template.h#L339)
such as SONOFF_BASIC, SONOFF_TOUCH, WEMOS. For custom programs, see instructions

## type
(Optional, defaults to module) Type of device for categorization purposes. With Tasmota, the module is USER_MODULE when supplying _any_ USER_TEMPLATE, and that may refer to many different types of devices.

## board
Type of esp board. esp01_1m for tasmota. Usually d1_mini, nodemcuv2, etc. for custom.

## ip_addr
(Optional, mostly) The IP address of the device on your network, for OTA flashing. If it's not set, the script will query it with `cmnd/topic/status 5`, which works for devices running Tasmota and as long as you aren't changing the device's topic. Not required for serial flashing.

## hass_template
(Optional) Which template file to use from ./hass_templates (light, light_rgb, generic, etc.)

## hass_domain
(Optional) Type of devive in home assistant: light, sensor, switch, etc.

## topic, base_topic (optional), group_topic (optional)
* The MQTT topic will be `%prefix%/{topic}` by default
* If `base_topic` is defined, the topic will be `%prefix%/{base_topic}/{topic}`
* If `group_topic` is defined, the group topic will be either `%prefix%/{group_topic}` or `%prefix%/{base_topic}/{group_topic}` depending on whether `base_topic` is defined.


## poweron_state
* 0 - Leave the relay off when device is plugged in
* 1 - Switch the relay on when device is plugged in

## build_flags
(Optional) List of flags to pass when compiling. Useful for enabling tasmota features (i.e. `"USE_RULES"`) or passing other options/defines to custom programs (i.e. `"-DTOPIC_0_TOPIC=\\\"i3/inside/light\\\"`)

## commands
(Optional) List of command/payload pairs. MQTT commands to be executed when the device comes online after flashing. Useful for setting tasmota options (i.e. `{"command": "GPIO2", "payload": "GPIO_SWT1"}`). Commands (such as tasmota rules) which are long lists can be broken up over multiple lines in an array by using `concat` instead of `payload` (i.e. `{"command": "rule1", "concat": ["on A do B endon", "on X do Y endon"]}`)

## instances
(Optional) List of json objects which are all instances of a parent device. Useful for when many devices are identical except for name (i.e. Light 001, Light 002 or Light East, Light West). Each instance can optionally have an `id` parameter. It will be filled in in place of `%id%` if it is present in other device parameters. Other parameters such as group_topic can be included in the id object. For example `{"name": "light %id%", "module": "SONOFF_BASIC", "topic": "lights/%id%", "instances": [{"id": "001", "ip_addr": "10.13.107.133", "group_topic": "lights/row1"}, {"id": "006", "ip_addr": "10.13.107.135", "group_topic": "lights/row2"}]}` In general, if a parameter is defined in both the parent device and an instance, the value in the instance will override. However, commands and build flags in an instance will be appended after any defined in the parent device.

## flash_warning
(Optional) Warning text to be displayed before flashing a device. Forces pause and user interaction before compiling and flashing. Can be used as a failsafe for devices you should care when flashing, like things people might be using (in our case laser cutters) or devices that might lose calibration settings (i.e. sonoff pows)

# Tasmota setup/update
* `blank_defines.h` undefines everything in `Tasmota/tasmota/my_user_config.h`, and then enables only certain things.
  * Look at the top for how to generate a new list of `#undefs`
* Look at `my_user_config` section 1 and put that in `blank_defines.h`.
* Like two things in section 2 are also important.
* Update tasmota version string in `espq.py` from `tasmota/tasmota_version.h`
