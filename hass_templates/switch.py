# Simple tasmota switch and metadata
# Use for sonoff basic, touch, TH

import generic

switch = """- platform: mqtt
  name: '{f_name}'
  state_topic: 'stat/{topic}/POWER'
  command_topic: 'cmnd/{topic}/POWER'
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
