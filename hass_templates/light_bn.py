# Tasmota light with dimmer and metadata
# Use for Sonoff BN

import generic

light = """- platform: mqtt
  name: '{f_name}'
  state_topic: 'stat/{base_topic}/{topic}/POWER'
  command_topic: 'cmnd/{base_topic}/{topic}/POWER'
  availability_topic: 'tele/{base_topic}/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'
  payload_on: 'ON'
  payload_off: 'OFF'
  brightness_scale: 50
  brightness_command_topic: 'cmnd/{base_topic}/{topic}/Dimmer'
  brightness_state_topic: 'stat/{base_topic}/{topic}/RESULT'
  brightness_value_template: '{{{{value_json.Dimmer}}}}'
"""

sensor = generic.generic_telemetry + """    {name}_power:
      friendly_name: '{f_name} Power'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.POWER }}}}'
    {name}_dimmer:
      friendly_name: '{f_name} Dimmer'
      unit_of_measurement: '%'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Dimmer }}}}'
    {name}_fade:
      friendly_name: '{f_name} Fade'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Fade }}}}'
    {name}_speed:
      friendly_name: '{f_name} Speed'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Speed }}}}'
    {name}_led_table:
      friendly_name: '{f_name} LED Table'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.LedTable }}}}'
"""

components = {
                'light': light,
                'sensor': sensor
             }
