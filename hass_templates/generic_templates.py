# Generic components shared by many devices, such as tasmota telemetry values

tasmota_telemetry = """- platform: mqtt
  name: '{f_name} VCC'
  state_topic: 'tele/{base_topic}/{topic}/STATE'
  value_template: '{{{{ value_json.Vcc }}}}'
  force_update: True

- platform: mqtt
  name: '{f_name} Uptime'
  state_topic: 'tele/{base_topic}/{topic}/STATE'
  value_template: '{{{{ value_json.Uptime }}}}'
  force_update: True

- platform: mqtt
  name: '{f_name} LoadAvg'
  state_topic: 'tele/{base_topic}/{topic}/STATE'
  value_template: '{{{{ value_json.LoadAvg }}}}'
  force_update: True

- platform: mqtt
  name: '{f_name} Wifi Channel'
  state_topic: 'tele/{base_topic}/{topic}/STATE'
  value_template: '{{{{ value_json["Wifi"]["Channel"] }}}}'
  force_update: True

- platform: mqtt
  name: '{f_name} Wifi RSSI'
  state_topic: 'tele/{base_topic}/{topic}/STATE'
  value_template: '{{{{ value_json["Wifi"]["RSSI"] }}}}'
  force_update: True

- platform: mqtt
  name: '{f_name} Wifi BSSId'
  state_topic: 'tele/{base_topic}/{topic}/STATE'
  value_template: '{{{{ value_json["Wifi"]["BSSId"] }}}}'
  force_update: True

- platform: template
  sensors:
    {name}_wifi_ap:
      friendly_name: '{f_name} Wifi AP'
      value_template: >-
        {{% if states('sensor.{name}_wifi_bssid') | string == '02:9F:C2:24:32:82' %}}
          Office AP
        {{% elif states('sensor.{name}_wifi_bssid') | string == '02:9F:C2:24:30:D7' %}}
          Mezzanine AP
        {{% elif states('sensor.{name}_wifi_bssid') | string == '02:9F:C2:24:2D:F1' %}}
          Tool Crib AP
        {{% elif states('sensor.{name}_wifi_bssid') | string == '0E:EC:DA:B7:E0:7D' %}}
          B-Side South AP
        {{% elif states('sensor.{name}_wifi_bssid') | string == 'C6:FB:E4:44:66:C4' %}}
          B-Side North AP
        {{% else %}}
          Unknown AP
        {{% endif %}}
"""

components = {
                'sensor': tasmota_telemetry
             }