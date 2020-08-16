# 3-way tasmota switch and metadata
# Use for tuya-based 3-way switch like:
#  - https://templates.blakadder.com/moes-SS01-1.html
#  - https://templates.blakadder.com/treatlife_SS01S.html
# If both 3-way switches in a pair are running tasmota,
# only one needs to be loaded in Home Assistant,
# though the second one can be as well to track its metadata

import generic

switch = """- platform: mqtt
  name: '{f_name}'
  state_topic: 'stat/{topic}/POWER1'
  command_topic: 'cmnd/{topic}/EVENT'
  json_attributes_topic: 'tele/{topic}/STATE'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'
  payload_on: 'ON'
  payload_off: 'OFF'
"""

sensor = generic.generic_telemetry + """    {name}_power:
      friendly_name: '{f_name} Power'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.POWER }}}}'
"""

components = {
                'switch': switch,
                'sensor': sensor
             }
