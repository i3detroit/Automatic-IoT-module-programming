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

- platform: template
  sensors:
    {name}_time:
      friendly_name: '{f_name} Time'
      value_template: '{{{{ states.sensor.{name}.attributes.Time }}}}'
    {name}_uptime:
      friendly_name: '{f_name} Uptime'
      value_template: '{{{{ states.sensor.{name}.attributes.Uptime }}}}'
    {name}_vcc:
      friendly_name: '{f_name} Vcc'
      unit_of_measurement: 'V'
      value_template: '{{{{ states.sensor.{name}.attributes.Vcc }}}}'
    {name}_sleepmode:
      friendly_name: '{f_name} SleepMode'
      value_template: '{{{{ states.sensor.{name}.attributes.SleepMode }}}}'
    {name}_sleep:
      friendly_name: '{f_name} Sleep'
      value_template: '{{{{ states.sensor.{name}.attributes.Sleep }}}}'
    {name}_loadavg:
      friendly_name: '{f_name} LoadAvg'
      unit_of_measurement: '%'
      value_template: '{{{{ states.sensor.{name}.attributes.LoadAvg }}}}'
    {name}_wifi_ssid:
      friendly_name: '{f_name} Wifi SSId'
      value_template: '{{{{ states.sensor.{name}.attributes.Wifi.SSId }}}}'
    {name}_wifi_bssid:
      friendly_name: '{f_name} Wifi BSSId'
      value_template: >-
        {{% if states('sensor.{name}.attributes.Wifi.BSSId') | string == '02:9F:C2:24:32:82' %}}
          Office AP
        {{% elif states('sensor.{name}.attributes.Wifi.BSSId') | string == '02:9F:C2:24:30:D7' %}}
          Mezzanine AP
        {{% elif states('sensor.{name}.attributes.Wifi.BSSId') | string == '02:9F:C2:24:2D:F1' %}}
          Tool Crib AP
        {{% elif states('sensor.{name}.attributes.Wifi.BSSId') | string == '0E:EC:DA:B7:E0:7D' %}}
          B-Side South AP
        {{% elif states('sensor.{name}.attributes.Wifi.BSSId') | string == 'C6:FB:E4:44:66:C4' %}}
          B-Side North AP
        {{% else %}}
          {{{{ states.sensor.{name}.attributes.Wifi.BSSId }}}}
        {{% endif %}}
    {name}_wifi_channel:
      friendly_name: '{f_name} Wifi Channel'
      value_template: '{{{{ states.sensor.{name}.attributes.Wifi.Channel }}}}'
    {name}_wifi_rssi:
      friendly_name: '{f_name} Wifi RSSI'
      unit_of_measurement: '%'
      value_template: '{{{{ states.sensor.{name}.attributes.Wifi.RSSI }}}}'
    {name}_wifi_linkcount:
      friendly_name: '{f_name} Wifi Link Count'
      value_template: '{{{{ states.sensor.{name}.attributes.Wifi.LinkCount }}}}'
    {name}_wifi_downtime:
      friendly_name: '{f_name} Wifi Downtime'
      value_template: '{{{{ states.sensor.{name}.attributes.Wifi.Downtime }}}}'
"""

components = {
                'sensor': sensor
             }
