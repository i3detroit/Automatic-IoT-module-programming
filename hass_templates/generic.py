# Generic tasmota device telemetry
# Use for stateless things like sensor switch buttons that are just
# a D1 Mini with a button

import datetime as dt

comment = """########################################
### Home assistant config for {hass_domain} {f_name}
### Generated by https://github.com/i3detroit/Automatic-IoT-module-programming
""" + """### on {now}
########################################
""".format(now=dt.datetime.now())

sensor = """- platform: mqtt
  name: '{f_name}'
  state_topic: 'stat/{topic}/SENSOR'
  json_attributes_topic: 'tele/{topic}/STATE'
  availability_topic: 'tele/{topic}/LWT'
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
{wifi_APs_string}
"""

components = {
                'sensor': comment + sensor + generic_telemetry
             }
