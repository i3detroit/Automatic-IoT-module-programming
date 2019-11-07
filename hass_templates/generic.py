# Generic tasmota device telemetry
# Use for stateless things like sensor switch buttons that are just
# a D1 Mini with a button

sensor = """- platform: mqtt
  name: '{f_name}'
  state_topic: 'stat/{base_topic}/{topic}/SENSOR'
  json_attributes_topic: 'tele/{base_topic}/{topic}/STATE'
  availability_topic: 'tele/{base_topic}/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'
"""
generic_telemetry = """- platform: template
  sensors:
    {name}_time:
      friendly_name: '{f_name} Time'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Time }}}}'
    {name}_uptime:
      friendly_name: '{f_name} Uptime'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Uptime }}}}'
    {name}_vcc:
      friendly_name: '{f_name} Vcc'
      unit_of_measurement: 'V'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Vcc }}}}'
    {name}_heap:
      friendly_name: '{f_name} Heap'
      value_template: '{{{{ states.light.{name}.attributes.Heap }}}}'
    {name}_sleepmode:
      friendly_name: '{f_name} SleepMode'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.SleepMode }}}}'
    {name}_sleep:
      friendly_name: '{f_name} Sleep'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.Sleep }}}}'
    {name}_loadavg:
      friendly_name: '{f_name} LoadAvg'
      unit_of_measurement: '%'
      value_template: '{{{{ states.{hass_domain}.{name}.attributes.LoadAvg }}}}'
    {name}_wifi_ssid:
      friendly_name: '{f_name} Wifi SSId'
      value_template: "{{{{ state_attr('{hass_domain}.{name}', 'Wifi')['SSId'] }}}}"
    {name}_wifi_ap:
      friendly_name: '{f_name} Wifi AP'
      value_template: >-
        {{% if state_attr('{hass_domain}.{name}', 'Wifi')['BSSId'] | string == '02:9F:C2:24:32:82' %}}
          Office AP
        {{% elif state_attr('{hass_domain}.{name}', 'Wifi')['BSSId'] | string == '02:9F:C2:24:30:D7' %}}
          Mezzanine AP
        {{% elif state_attr('{hass_domain}.{name}', 'Wifi')['BSSId'] | string == '02:9F:C2:24:2D:F1' %}}
          Tool Crib AP
        {{% elif state_attr('{hass_domain}.{name}', 'Wifi')['BSSId'] | string == '0E:EC:DA:B7:E0:7D' %}}
          B-Side South AP
        {{% elif state_attr('{hass_domain}.{name}', 'Wifi')['BSSId'] | string == 'C6:FB:E4:44:66:C4' %}}
          B-Side North AP
        {{% else %}}
          {{{{ state_attr('{hass_domain}.{name}', 'Wifi')['BSSId'] }}}}
        {{% endif %}}
    {name}_wifi_bssid:
      friendly_name: '{f_name} Wifi BSSId'
      value_template: "{{{{ state_attr('{hass_domain}.{name}', 'Wifi')['BSSId'] }}}}"
    {name}_wifi_channel:
      friendly_name: '{f_name} Wifi Channel'
      value_template: "{{{{ state_attr('{hass_domain}.{name}', 'Wifi')['Channel'] }}}}"
    {name}_wifi_rssi:
      friendly_name: '{f_name} Wifi RSSI'
      unit_of_measurement: '%'
      value_template: "{{{{ state_attr('{hass_domain}.{name}', 'Wifi')['RSSI'] }}}}"
    {name}_wifi_linkcount:
      friendly_name: '{f_name} Wifi Link Count'
      value_template: "{{{{ state_attr('{hass_domain}.{name}', 'Wifi')['LinkCount'] }}}}"
    {name}_wifi_downtime:
      friendly_name: '{f_name} Wifi Downtime'
      value_template: "{{{{ state_attr('{hass_domain}.{name}', 'Wifi')['Downtime'] }}}}"
"""

components = {
                'sensor': sensor + generic_telemetry
             }
