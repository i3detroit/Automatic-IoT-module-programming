# A script for autoprogramming a bunch of sonoffs

Setup: On McClellan, copy /home/mkfink/pio to your home directory. Or clone the repo and copy /home/mkfink/pio/Sonoff-Tasmota alongside it. This uses a slightly modified version of Sonoff-Tasmota, changes detailed below. /home/mkfink/pio contains a python venv specifically set up to run with this script and PlatformIO. platformio.ini and user_config_override.h are provided here as examples, but they should also be in the correct place.

Device specific information is located in tasmota.yaml. Modules are flashed based on IP. All tasmota devices should have static IPs when on the IoT VLAN (10.13.107.x). Use mqtt_query_ip.py to verify all device IPs, in case some devices have have failed over to the normal LAN.

Copy the devices you want to flash to flash.yaml and run autoflash.py. Script will compile and OTA flash the device. If any post-flash commands are defined, it will watch MQTT for the device to come back online after flashing and then run the post-flash commands. Then it will move on to the next device.

## Tasmota settings which are changed - set in user_config_override.h
* `CFG_HOLDER`
* `MODULE`
* `MQTT_GRPTOPIC`
* `MQTT_FULLTOPIC`
* `MQTT_TOPIC`
* `FRIENDLY_NAME`
* `APP_POWERON_STATE`
* Extra tasmota settings like sensors

### Based on device location (i3, mike's house, mark's house, etc.)
* `MQTT_HOST`
* `STA_SSID1`
* `STA_PASS1`
* `STA_SSID2`
* `STA_PASS2`
* `MQTT_HOST`
* `NTP_SERVER1` "10.13.0.1" or "nl.pool.ntp.org"

## same for all - changed in user_config.h
* `SAVE_STATE` set to 0
* `WIFI_CONFIG_TOOL` set to `WIFI_RETRY` to not bounce device on wifi fail. Lights were flickering.
* `MQTT_USER`              ''
* `MQTT_PASS`              ''
* `TIME_DST_HEMISPHERE`    North
* `TIME_DST_WEEK`          Second
* `TIME_DST_DAY`           Sun
* `TIME_DST_MONTH`         Mar
* `TIME_DST_HOUR`          2
* `TIME_DST_OFFSET`        -240
* `TIME_STD_HEMISPHERE`    North
* `TIME_STD_WEEK`          First
* `TIME_STD_DAY`           Sun
* `TIME_STD_MONTH`         Nov
* `TIME_STD_HOUR`          3
* `TIME_STD_OFFSET`        -300
* `LATITUDE`               42.453725
* `LONGITUDE`              -83.113690
* `APP_TIMEZONE`           99

### Undefine
* Almost all of the extra options. Enable per device based on tasmota.yaml.
