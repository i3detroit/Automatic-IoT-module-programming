# Tasmota light with RGB & dimmer, and metadata
# Use for MagicHome-like devices

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
  payload_on: "ON"
  payload_off: "OFF"
  payload_available: "Online"
  payload_not_available: "Offline"
  on_command_type: "brightness"
"""

sensor = """- platform: template
  sensors:
    {name}_time:
      friendly_name: '{f_name} Time'
      value_template: '{{{{ states.light.{name}.attributes.Time }}}}'
    {name}_uptime:
      friendly_name: '{f_name} Uptime'
      value_template: '{{{{ states.light.{name}.attributes.Uptime }}}}'
    {name}_vcc:
      friendly_name: '{f_name} Vcc'
      unit_of_measurement: 'V'
      value_template: '{{{{ states.light.{name}.attributes.Vcc }}}}'
    {name}_sleepmode:
      friendly_name: '{f_name} SleepMode'
      value_template: '{{{{ states.light.{name}.attributes.SleepMode }}}}'
    {name}_sleep:
      friendly_name: '{f_name} Sleep'
      value_template: '{{{{ states.light.{name}.attributes.Sleep }}}}'
    {name}_loadavg:
      friendly_name: '{f_name} LoadAvg'
      unit_of_measurement: '%'
      value_template: '{{{{ states.light.{name}.attributes.LoadAvg }}}}'
    {name}_power:
      friendly_name: '{f_name} Power'
      value_template: '{{{{ states.light.{name}.attributes.POWER }}}}'
    {name}_dimmer:
      friendly_name: '{f_name} Dimmer'
      unit_of_measurement: '%'
      value_template: '{{{{ states.light.{name}.attributes.Dimmer }}}}'
    {name}_color:
      friendly_name: '{f_name} Color'
      value_template: '{{{{ states.light.{name}.attributes.Color }}}}'
    {name}_hsb_color:
      friendly_name: '{f_name} HSB Color'
      value_template: '{{{{ states.light.{name}.attributes.HSBColor }}}}'
    {name}_color_channel:
      friendly_name: '{f_name} Color Channel'
      value_template: '{{{{ states.light.{name}.attributes.Channel }}}}'
    {name}_scheme:
      friendly_name: '{f_name} Scheme'
      value_template: '{{{{ states.light.{name}.attributes.Scheme }}}}'
    {name}_fade:
      friendly_name: '{f_name} Fade'
      value_template: '{{{{ states.light.{name}.attributes.Fade }}}}'
    {name}_speed:
      friendly_name: '{f_name} Speed'
      value_template: '{{{{ states.light.{name}.attributes.Speed }}}}'
    {name}_led_table:
      friendly_name: '{f_name} LED Table'
      value_template: '{{{{ states.light.{name}.attributes.LedTable }}}}'
    {name}_wifi_ssid:
      friendly_name: '{f_name} Wifi SSId'
      value_template: '{{{{ states.light.{name}.attributes.Wifi.SSId }}}}'
    {name}_wifi_bssid:
      friendly_name: '{f_name} Wifi BSSId'
      value_template: >-
        {{% if states('light.{name}.attributes.Wifi.BSSId') | string == '02:9F:C2:24:32:82' %}}
          Office AP
        {{% elif states('light.{name}.attributes.Wifi.BSSId') | string == '02:9F:C2:24:30:D7' %}}
          Mezzanine AP
        {{% elif states('light.{name}.attributes.Wifi.BSSId') | string == '02:9F:C2:24:2D:F1' %}}
          Tool Crib AP
        {{% elif states('light.{name}.attributes.Wifi.BSSId') | string == '0E:EC:DA:B7:E0:7D' %}}
          B-Side South AP
        {{% elif states('light.{name}.attributes.Wifi.BSSId') | string == 'C6:FB:E4:44:66:C4' %}}
          B-Side North AP
        {{% else %}}
          {{{{ states.light.{name}.attributes.Wifi.BSSId }}}}
        {{% endif %}}
    {name}_wifi_channel:
      friendly_name: '{f_name} Wifi Channel'
      value_template: '{{{{ states.light.{name}.attributes.Wifi.Channel }}}}'
    {name}_wifi_rssi:
      friendly_name: '{f_name} Wifi RSSI'
      unit_of_measurement: '%'
      value_template: '{{{{ states.light.{name}.attributes.Wifi.RSSI }}}}'
    {name}_wifi_linkcount:
      friendly_name: '{f_name} Wifi Link Count'
      value_template: '{{{{ states.light.{name}.attributes.Wifi.LinkCount }}}}'
    {name}_wifi_downtime:
      friendly_name: '{f_name} Wifi Downtime'
      value_template: '{{{{ states.light.{name}.attributes.Wifi.Downtime }}}}'
"""

components = {
                'light': light,
                'sensor': sensor
             }