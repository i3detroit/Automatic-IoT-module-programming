# Autoprogramming a bunch of sonoffs

Find the list you hate
```
sudo nmap -sP 10.13.0.0-255 | grep -v "Host" | tail -n +3 | tr '\n' ' ' | sed 's|Nmap|\nNmap|g' |  grep "MAC Address" | perl -pe 's/.*report for (?:([^ ]*) \()?((?:[0-9]{1,3}\.?){4})\)? MAC Address: ([A-Z0-9:]*).*/$1 $2 $3/'
```

## Tasmota settings to change
* `MODULE` in `sonoff.ino`
* `MQTT_FULLTOPIC` in `user_config.h`
* `MQTT_TOPIC` in `user_config.h`
* `MQTT_GRPTOPIC` in `user_config.h`
* `FRIENDLY_NAME` in `user_config.h`
* `MQTT_GRPTOPIC` in `user_config.h`
* `APP_POWERON_STATE` in `user_config.h`, [PowerOnState] Power On Relay state (0 = Off, 1 = On, 2 = Toggle Saved state, 3 = Saved state)
