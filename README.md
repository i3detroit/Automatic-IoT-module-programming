# A script for autoprogramming a bunch of sonoffs

Setup:

```
Install raspbian
enable ssh, set hostname

sudo apt-get install git
sudo apt-get install curl
git clone https://github.com/i3detroit/Automatic-IoT-module-programming.git
sudo apt-get install python3.7
sudo apt-get install python3-pip

(update espq.py to use 5.0.0)

cd Automatic-IoT-module-programming
pip3 install -r requirements.txt
cd ..
wget https://github.com/arendst/Tasmota/archive/v8.4.0.zip
unzip v8.4.0.zip
mv Tasmota-8.4.0 Tasmota

edit Tasmota/pio/espupload.py to be #!/bin/python3 instead of #!/bin/python (may be able to be removed in a future revision)
create/update config/sites.json from config/sites.json.example
create site-specific json file for devices

python3 -c "$(curl -fsSL https://raw.githubusercontent.com/platformio/platformio/master/scripts/get-platformio.py)"

add pio path to PATH

sudo apt-get install mosquitto
./provision...
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
    - Each device can be a single device or many identical devices which only differ by a few properties (name, topic, etc.).
2. Run `./provision.py flash [-m {wifi|serial}] [-p SERIALPORT] config/your_devices.json` (defaults to serial and /dev/ttyUSB0)

`blank_defines.h` undefines all of tasmota's config and lets us include just the features we need for each device (see _tasmota_defines_ below).
It's processed by python's .format to insert some specific settings near the bottom.
A version of `platformio_override.ini` is provided here to be used with tasmota. The flashing script copies it to the correct location as needed.

# To program custom devices
1. Create a device configuration file for your custom device(s) as in custom.json. Software should be the parent folder. Module should be the name of the program itself. (i.e. you would have your program stored as `./software/module/module.ino`). As above, `%id%` can be used for identical devices.
2. Run `./provision.py flash [-m {wifi|serial}] [-p SERIALPORT] config/your_devices.json` (defaults to serial and /dev/ttyUSB0)

# Other Stuff
- Query tasmota device statuses (IP, MAC, tasmota version, esp core version) with `ip_query.py config/your_devices.json`.
- Home Assistant configuration yaml files can be generated via `./provision.py hass config/your_devices.json` for any type of device with a template in `hass_templates`. This generally creates a yaml file for the device (i.e. `living_room_lamp_light.yaml`) as well as a sensor file (i.e. `living_room_lamp_sensor.yaml`) with template sensors for all the telemetry Tasmota publishes. The latter is not required to use the device in Home Assistant (unless it's a just a sensor). Remember to copy the yaml files to your Home Assistant config directory (i.e. all `*_light.yaml` should go in `.homeassistant/lights`, and `light: !include_dir_merge_list lights` should be added to your `configuration.yaml`)
- Run the setup commands from a device's config with `./provision.py cmds config/your_devices.json`

# Device configuration file explanation
## name
Friendly name of device.

## software
What to program the device with. Can be 'tasmota' or a custom program's directory.

## site
Site name from sites.json, which should include location specific options (wifi info, etc.)

## module
For tasmota, should be one of the [supported hardware modules](https://github.com/arendst/Tasmota/blob/development/tasmota/tasmota_template.h#L799)
such as SONOFF_BASIC, SONOFF_TOUCH, WEMOS. As of Tasmota 8.4.0, USER_MODULE should be used when defining a custom template (see _tasmota_defines_ below). For custom programs, see instructions.

## type
(Optional, defaults to module) Type of device for categorization purposes. With Tasmota, the module is USER_MODULE when supplying _any_ USER_TEMPLATE, and that may refer to many different types of devices. This is mostly a user-facing value and can be whatever you want, however the list of devices in `config/your_devices.json` does get sorted by type prior to compiling and flashing.

## board
Type of esp board. esp01_1m for tasmota. Usually d1_mini, nodemcuv2, etc. for custom.

## ip_addr
(Optional, mostly) The IP address of the device on your network, for OTA flashing. If this value is not set, the script will query it with `cmnd/topic/status 5`, which works for devices running Tasmota and as long as you aren't changing the device's topic. Not required for serial flashing. *Strongly recommended* if you provide an IP, make sure your devices have static IPs on your network so you don't accidentally turn a light switch into a thermostat (has happened!). Running `ip_query.py` should return the IPs of all the tasmota devices in your config file.

## hass_template
(Optional) Which template file to use from ./hass_templates (light, light_rgb, sonoff_pow, generic, etc.)

## hass_domain
(Optional) Type of devive in home assistant: light, sensor, switch, etc.

## topic, base_topic (optional), group_topic (optional)
* The MQTT topic will be `%prefix%/{topic}` by default
* If `base_topic` is defined, the topic will be `%prefix%/{base_topic}/{topic}`
* If `group_topic` is defined, the group topic will be either `%prefix%/{group_topic}` or `%prefix%/{base_topic}/{group_topic}` depending on whether `base_topic` is defined.

## poweron_state
(Tasmota specific) Sets what the device does when it is powered up, if it has any relay(s). See https://tasmota.github.io/docs/PowerOnState/ for details.
* 0 / OFF = keep relay(s) OFF after power up
* 1 / ON = turn relay(s) ON after power up
* 2 / TOGGLE = toggle relay(s) from last saved state
* 3 = switch relay(s) to their last saved state (default)
* 4 = turn relay(s) ON and disable further relay control
* 5 = after a PulseTime period turn relay(s) ON (acts as inverted PulseTime mode)


## pio_build_flags
(Optional)
List of flags to pass when compiling custom programs. Example: `"-DTOPIC_0_TOPIC=\\\"i3/inside/light\\\"`

## tasmota_defines
(Optional)
Defines to put in the tasmota user config.
It's an array that can contain [device specific options](https://github.com/arendst/Tasmota/blob/development/tasmota/my_user_config.h) as a list of strings and optionally a USER_TEMPLATE JSON object. These options and the template get added as `#define`s in `user_config_override.h` which gets compiled into Tasmota.
You can get USER_TEMPLATEs from https://templates.blakadder.com/ it's really just ways to bake into the firmware what GPIO does what for different devices.
```
"tasmota_defines": [
    "KEY_ONLY_SINGLE_PRESS 1",
    {"USER_TEMPLATE": {
        "NAME":"TL SS01 3-Way",
        "GPIO":[0,0,0,0,21,158,0,0,22,18,9,0,0],
        "FLAG":0,
        "BASE":18
    }}
],
```

## commands
(Optional) List of command/payload pairs. MQTT commands to be executed when the device comes online after flashing. Useful for setting tasmota options (i.e. Tasmota rules or [anything else](https://tasmota.github.io/docs/Commands/)). Commands (such as tasmota rules) which are long lists can be broken up over multiple lines in an array by using `concat` instead of `payload` (i.e. `{"command": "rule1", "concat": ["ON A do B ENDON", "ON X do Y ENDON"]}`)

## instances
(Optional) List of json objects which are all instances of a parent device. Useful for when many devices are identical except for name (i.e. Light 001, Light 002 or Light East, Light West). Each instance can optionally have an `id` parameter. It will be filled in in place of `%id%` if that is present in other device parameters. Other parameters such as group_topic can be included in the id object. For example `{"name": "light %id%", "module": "SONOFF_BASIC", "topic": "lights/%id%", "instances": [{"id": "001", "ip_addr": "10.13.107.133", "group_topic": "lights/row1"}, {"id": "006", "ip_addr": "10.13.107.135", "group_topic": "lights/row2"}]}` In general, if a parameter is defined in both the parent device and an instance, the value in the instance will override. However, commands and tasmota_defines in an instance will be appended to any defined in the parent device.

## flash_warning
(Optional) Warning text to be displayed before flashing a device. Forces pause and user interaction before compiling and flashing. Can be used as a failsafe for devices you should take care when flashing, like things people might be using (in our case laser cutters) or devices that might lose calibration settings (i.e. sonoff pows)

# Tasmota setup/update
* `blank_defines.h` undefines everything in `Tasmota/tasmota/my_user_config.h`, and then enables only certain things.
  * Look at the top for how to generate a new list of `#undefs`
* Look at `my_user_config` section 1 and put that in `blank_defines.h`.
* A few things in section 2 are also important.
* Update tasmota version string in `espq.py` from `tasmota/tasmota_version.h`
