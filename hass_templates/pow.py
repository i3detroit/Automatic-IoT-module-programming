# Tasmota switch with energy monitoring
# Use on sonoff POW, S31

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

- platform: mqtt
  name: '{f_name} Total Start Time'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"TotalStartTime\"] }}}}'
  force_update: True
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Total Energy'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"Total\"] }}}}'
  force_update: True
  unit_of_measurement: 'kilowatt hours'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Energy Use Yesterday'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"Yesterday\"] }}}}'
  force_update: True
  unit_of_measurement: 'kilowatt hours'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Energy Use Today'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"Today\"] }}}}'
  force_update: True
  unit_of_measurement: 'kilowatt hours'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Energy Use Delta'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"Period\"] }}}}'
  force_update: True
  unit_of_measurement: 'Watt hours'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Power Draw'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"Power\"] }}}}'
  force_update: True
  unit_of_measurement: 'Watts'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Apparent Power Draw'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"ApparentPower\"] }}}}'
  force_update: True
  unit_of_measurement: 'Watts'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Reactive Power Draw'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"ReactivePower\"] }}}}'
  force_update: True
  unit_of_measurement: 'Watts'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Power Factor'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"Factor\"] }}}}'
  force_update: True
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Voltage'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"Voltage\"] }}}}'
  force_update: True
  unit_of_measurement: 'Volts'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Current'
  state_topic: 'tele/{topic}/SENSOR'
  value_template: '{{{{ value_json[\"ENERGY\"][\"Current\"] }}}}'
  force_update: True
  unit_of_measurement: 'Amps'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

"""

components = {
                'switch': switch,
                'sensor': sensor
             }
