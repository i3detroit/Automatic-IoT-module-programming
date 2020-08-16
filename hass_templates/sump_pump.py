# Sump Pump measurement, just distance sensor

import generic

sensor_cluster = """- platform: mqtt
  name: '{f_name} Distance'
  state_topic: 'tele/{topic}/SENSOR'
  unit_of_measurement: 'cm'
  value_template: "{{{{ value_json['SR04']['Distance'] }}}}"
  force_update: True
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'

"""

sensor = generic.sensor + generic.generic_telemetry + sensor_cluster

components = {
                'sensor': sensor
             }
