# Simple tasmota light and metadata
# Use for sonoff basic, touch, SV

import generic

sensor_cluster = """- platform: mqtt
  name: '{f_name} Temperature'
  state_topic: 'tele/{topic}/SENSOR'
  unit_of_measurement: '°C'
  value_template: "{{{{ value_json['BME280']['Temperature'] }}}}"
  force_update: True
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} OneWire Temperature'
  state_topic: 'tele/{base_topic}/{topic}/SENSOR'
  unit_of_measurement: 'Â°C'
  value_template: "{{{{ value_json['DS18B20']['Temperature'] }}}}"
  force_update: True
  availability_topic: 'tele/{base_topic}/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Pressure'
  state_topic: 'tele/{topic}/SENSOR'
  unit_of_measurement: 'hPa'
  value_template: "{{{{ value_json['BME280']['Pressure'] }}}}"
  force_update: True
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Humidity'
  state_topic: 'tele/{topic}/SENSOR'
  unit_of_measurement: '%'
  value_template: "{{{{ value_json['BME280']['Humidity'] }}}}"
  force_update: True
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: mqtt
  name: '{f_name} Lux'
  state_topic: 'tele/{topic}/SENSOR'
  unit_of_measurement: 'lux'
  value_template: "{{{{ value_json['BH1750']['Illuminance'] }}}}"
  force_update: True
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

- platform: template
  sensors:
    {name}_pressure_kpa:
      friendly_name: "{f_name} Pressure"
      unit_of_measurement: 'kPa'
      value_template: "{{{{ states('sensor.{name}_pressure') | multiply(1/10) | round(1) }}}}"
"""

sensor = generic.sensor + generic.generic_telemetry + sensor_cluster

components = {
                'sensor': generic.comment + sensor
             }