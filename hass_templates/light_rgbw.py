# Tasmota light with RGB & dimmer, and metadata
# Use for MagicHome-like devices

import generic

light = """- platform: mqtt
  name: {f_name}
  effect_list:
    - 2
    - 3
  state_topic: "stat/{base_topic}/{topic}/RESULT"
  command_topic: "cmnd/{base_topic}/{topic}/POWER"
  json_attributes_topic: 'tele/{base_topic}/{topic}/STATE'
  availability_topic: "tele/{base_topic}/{topic}/LWT"
  brightness_state_topic: "stat/{base_topic}/{topic}/RESULT"
  brightness_command_topic: "cmnd/{base_topic}/{topic}/Dimmer"
  brightness_scale: 100
  rgb_command_template: "{{{{ '%02x%02x%02x00' | format(red, green, blue)}}}}"
  rgb_state_topic: "stat/{base_topic}/{topic}/RESULT"
  rgb_command_topic: "cmnd/{base_topic}/{topic}/Color"
  white_value_state_topic: "stat/stat/{base_topic}/{topic}/RESULT"
  white_value_command_topic: "cmnd/{base_topic}/{topic}/channel4"
  white_value_scale: 100
  effect_command_topic: "cmnd/{base_topic}/{topic}/Scheme"
  effect_state_topic: "stat/{base_topic}/{topic}/RESULT"
  state_value_template: >
    {{% if "POWER" in value_json %}}
      {{{{ value_json.POWER }}}}
    {{% endif %}}
  brightness_value_template: >
    {{% if "Dimmer" in value_json %}}
      {{{{ value_json.Dimmer }}}}
    {{% endif %}}
  effect_value_template: >
    {{% if "Scheme" in value_json %}}
      {{{{ value_json.Scheme }}}}
    {{% endif %}}
  rgb_value_template: >
    {{% if "Color" in value_json %}}
      {{{{ (value_json.Color[0:2] | int(int, 16)) | string + ',' + (value_json.Color[2:4] | int(int, 16)) | string + ',' + (value_json.Color[4:6] | int(int, 16)) | string }}}}
    {{% endif %}}
  white_value_template: >
    {{% if "Channel4" in value_json %}}
      {{{{ value_json.Channel4}}}}
    {{% endif %}}
  payload_on: "ON"
  payload_off: "OFF"
  payload_available: "Online"
  payload_not_available: "Offline"
  on_command_type: "brightness"
"""

sensor = generic.generic_telemetry + """    {name}_power:
      friendly_name: '{f_name} Power'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.POWER }}}}'
    {name}_dimmer:
      friendly_name: '{f_name} Dimmer'
      unit_of_measurement: '%'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Dimmer }}}}'
    {name}_color:
      friendly_name: '{f_name} Color'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Color }}}}'
    {name}_hsb_color:
      friendly_name: '{f_name} HSB Color'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.HSBColor }}}}'
    {name}_color_channel:
      friendly_name: '{f_name} Color Channel'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Channel }}}}'
    {name}_scheme:
      friendly_name: '{f_name} Scheme'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Scheme }}}}'
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