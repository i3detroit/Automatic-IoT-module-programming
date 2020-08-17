# Tasmota dimmer light switch and metadata
# Use for tuya-based dimmer switch like:
#  - https://templates.blakadder.com/treatlife_DS01.html


import generic

light = """- platform: mqtt
  name: '{f_name}'
  state_topic: 'stat/{topic}/POWER'
  command_topic: 'cmnd/{topic}/POWER'
  json_attributes_topic: 'tele/{topic}/STATE'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'
  payload_on: 'ON'
  payload_off: 'OFF'
  brightness_scale: 100
  brightness_command_topic: 'cmnd/{topic}/Dimmer'
  brightness_state_topic: 'stat/{topic}/RESULT'
  brightness_value_template: '{{{{value_json.Dimmer}}}}'
"""

sensor = generic.generic_telemetry + """    {name}_power:
      friendly_name: '{f_name} Power'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.POWER }}}}'
    {name}_dimmer:
      friendly_name: '{f_name} Dimmer'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Dimmer }}}}'
    {name}_fade:
      friendly_name: '{f_name} Fade'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Fade }}}}'
    {name}_speed:
      friendly_name: '{f_name} Speed'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Speed }}}}'
"""

components = {
                'light': generic.comment + light,
                'sensor': generic.comment + sensor
             }
