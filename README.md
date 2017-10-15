# Autoprogramming a bunch of sonoffs

Find the list you hate
```
sudo nmap -sP 10.13.0.0-255 | grep -v "Host" | tail -n +3 | tr '\n' ' ' | sed 's|Nmap|\nNmap|g' |  grep "MAC Address" | perl -pe 's/.*report for (?:([^ ]*) \()?((?:[0-9]{1,3}\.?){4})\)? MAC Address: ([A-Z0-9:]*).*/$1 $2 $3/'
```

## Tasmota settings to change per device
* `MODULE` in `sonoff.ino` Can't be done in `user_config_override.h`, is defined after that's included.
* `CFG_HOLDER` Needs to be incremented or changed each program. If same, flash is not updated
* `MQTT_FULLTOPIC`
* `MQTT_TOPIC`
* `MQTT_GRPTOPIC`
* `FRIENDLY_NAME`
* `APP_POWERON_STATE` [PowerOnState] Power On Relay state (0 = Off, 1 = On, 2 = Toggle Saved state, 3 = Saved state)
* `WIFI_HOSTNAME` in sonoff.ino. Cannot contain `%`, or it will try to be passed the topic and the chip ID by `snprintf`. Set to `MQTT_TOPIC`, but replace / with -

## same for all
* `SAVE_STATE` [SetOption0] Save changed power state to Flash (0 = disable, 1 = enable)
* `STA_SSID1`
* `STA_PASS1`
* `STA_SSID2`
* `STA_PASS2`
* `WIFI_CONFIG_TOOL` `(WIFI_RESTART, WIFI_SMARTCONFIG, WIFI_MANAGER, WIFI_WPSCONFIG, WIFI_RETRY)`, set to `WIFI_RETRY` to not bounce device on wifi fail. Lights were flickering.
* `MQTT_HOST`
* `MQTT_USER`
* `MQTT_PASS`
* `TIME_DST` `Second, Sun, Mar, 2, -240`
* `TIME_STD` `First, Sun, Nov, 2, -300`
* `APP_TIMEZONE` `99`




### Undefine
* `MQTT_HOST_DISCOVERY`
* `USE_I2C`
* `USE_BH1750`
* `USE_BMP`
* `USE_HTU`
* `USE_SHT`
* `USE_IR_REMOTE`
* `USE_WS2812`
* `USE_WS2812_CTYPE`
