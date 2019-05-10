# A script for autoprogramming a bunch of sonoffs

Setup:

```
pip install -r requirements.txt
```


`blank_defines.h` undefines all of tasmota's config and lets us set what we want.
It's processed by python's .format to insert some specific settings near the bottom.

# To program tasmota devices
1. Create a device configuration file for your device(s) as in tasmota.json.
  - Each device can be a single device or many identical devices which only differ by some %id% string.
2. Create a sites.json file with your wifi/location information.
3. Run flash.py

# To program custom devices
Implement that

# Other Stuff
- Query tasmota device status (IP, MAC, tasmota version, core version) with ip_query.py
- Write user_config_override.h for a tasmota device with config_tas.py