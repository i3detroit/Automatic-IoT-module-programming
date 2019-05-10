light = """- platform: mqtt
  name: '{f_name}'
  state_topic: 'stat/{base_topic}/{topic}/POWER'
  command_topic: 'cmnd/{base_topic}/{topic}/POWER'
  availability_topic: 'tele/{base_topic}/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'
  payload_on: 'ON'
  payload_off: 'OFF'
"""

sensors = """- platform: mqtt
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
  value_template: '{{{{ value_json['Wifi']['Channel'] }}}}'
  force_update: True

- platform: mqtt
  name: '{f_name} Wifi RSSI'
  state_topic: 'tele/{base_topic}/{topic}/STATE'
  value_template: '{{{{ value_json['Wifi']['RSSI'] }}}}'
  force_update: True

- platform: mqtt
  name: '{f_name} Wifi BSSId'
  state_topic: 'tele/{base_topic}/{topic}/STATE'
  value_template: '{{{{ value_json['Wifi']['BSSId'] }}}}'
  force_update: True

- platform: template
  sensors:
    genie_charge_state:
      friendly_name: '{f_name} Wifi AP'
      value_template: >-
        {{% if states('sensor.{name}_wifi_bssid') | string == 'MAC0' %}}
          Office AP
        {{% elif states('sensor.{name}_wifi_bssid') | string == 'MAC1' %}}
          Mezzanine AP
        {{% elif states('sensor.{name}_wifi_bssid') | string == 'MAC2' %}}
          Tool Crib AP
        {{% elif states('sensor.{name}_wifi_bssid') | string == 'MAC3' %}}
          B-Side South AP
        {{% elif states('sensor.{name}_wifi_bssid') | string == 'MAC4' %}}
          B-Side North AP
        {{% else %}}
          Unknown AP
        {{% endif %}}
"""