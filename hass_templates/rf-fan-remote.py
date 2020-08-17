# For custom RF ceiling fan remote

import generic

fan = """- platform: mqtt
  name: '{f_name} Fan'
  state_topic: 'stat/{topic}/fan'
  command_topic: 'cmnd/{topic}/fan'
  speed_state_topic: 'stat/{topic}/speed'
  speed_command_topic: 'cmnd/{topic}/speed'
  json_attributes_topic: 'tele/{topic}/STATE'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'
  payload_on: 'ON'
  payload_off: 'OFF'
  payload_low_speed: 'low'
  payload_medium_speed: 'medium'
  payload_high_speed: 'high'
  speeds:
    - 'off'
    - low
    - medium
    - high
"""

light = """- platform: mqtt
  name: '{f_name} Light'
  state_topic: 'stat/{topic}/light'
  command_topic: 'cmnd/{topic}/light'
  json_attributes_topic: 'tele/{topic}/STATE'
  availability_topic: 'tele/{topic}/LWT'
  payload_available: 'Online'
  payload_not_available: 'Offline'
  payload_on: 'ON'
  payload_off: 'OFF'
"""

sensor = generic.generic_telemetry

components = {
                'light': generic.comment + light,
                'fan': generic.comment + fan,
                'sensor': generic.comment + sensor
             }