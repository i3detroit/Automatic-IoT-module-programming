import generic_templates

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

sensor = generic_templates.tasmota_telemetry

components = {
                'light': light,
                'sensor': sensor
             }