
# Simple tasmota light and metadata
# Use for sonoff basic, touch, SV

import generic

climate = """
- platform: mqtt
  name: {f_name}
  modes:
    - 'off'
    - 'heat'
    - 'cool'
  # swing_modes:
  #   - 0
  #   - 1
  #   - 2
  #   - 3
  fan_modes:
    - 'auto'
    - 'on'
  availability_topic: "tele/{base_topic}/{topic}/LWT"
  payload_available: "Online"
  payload_not_available: "Offline"

  current_temperature_topic: "tele/{base_topic}/{topic}/sensors"
  current_temperature_template: "{{{{value_json.temperature}}}}"

  mode_command_topic: "cmnd/{base_topic}/{topic}/mode"
  mode_state_topic: "tele/{base_topic}/{topic}/input"
  mode_state_template: "{{{{value_json.mode}}}}"

  action_topic: "tele/{base_topic}/{topic}/output"
  action_template: "{{{{value_json.state}}}}"

  temperature_command_topic: "cmnd/{base_topic}/{topic}/target"
  temperature_state_topic: "tele/{base_topic}/{topic}/input"
  temperature_state_template: "{{{{value_json.target}}}}"

  fan_mode_command_topic: "cmnd/{base_topic}/{topic}/fan"
  fan_mode_state_topic: "tele/{base_topic}/{topic}/input"
  fan_mode_state_template: "{{{{value_json.fan}}}}"

  # swing_mode_command_topic: "cmnd/{base_topic}/{topic}/swing"
  # swing_mode_state_topic: "tele/{base_topic}/{topic}/input"
  # swing_mode_state_template: "{{{{value_json.swing}}}}"
  min_temp: 5
  max_temp: 30
  precision: .1

"""

sensor = """
- platform: mqtt
  name: "{f_name} Ambient Temperature"
  state_topic: "tele/{base_topic}/{topic}/sensors"
  unit_of_measurement: "°C"
  value_template: '{{{{ value_json.temperature }}}}'
  force_update: True

- platform: mqtt
  name: "{f_name} Ambient Pressure"
  state_topic: "tele/{base_topic}/{topic}/sensors"
  unit_of_measurement: "Pa"
  value_template: '{{{{ value_json.pressure }}}}'
  force_update: True

- platform: template
  sensors:
    {name}_pressure_kpa:
      friendly_name: "Ambient Pressure"
      unit_of_measurement: 'kPa'
      value_template: "{{{{ ((states('sensor.{name}_ambient_pressure') | multiply(1/1000)) | float) | round(1) }}}}"

- platform: mqtt
  name: "{f_name} Ambient Humidity"
  state_topic: "tele/{base_topic}/{topic}/sensors"
  unit_of_measurement: "%"
  value_template: '{{{{ value_json.humidity }}}}'
  force_update: True

- platform: mqtt
  name: "{f_name} Target Temperature"
  state_topic: "tele/{base_topic}/{topic}/input"
  unit_of_measurement: "°C"
  value_template: '{{{{ value_json.target }}}}'
  force_update: True

- platform: mqtt
  name: "{f_name} Requested State"
  state_topic: "tele/{base_topic}/{topic}/input"
  value_template: '{{{{ value_json.mode }}}}'
  force_update: True

- platform: mqtt
  name: "{f_name} Requested Fan State"
  state_topic: "tele/{base_topic}/{topic}/input"
  value_template: '{{{{ value_json.fan }}}}'
  force_update: True

- platform: mqtt
  name: "{f_name} Swing"
  state_topic: "tele/{base_topic}/{topic}/input"
  value_template: '{{{{ value_json.swing }}}}'
  force_update: True

- platform: mqtt
  name: "{f_name} Timeout"
  state_topic: "tele/{base_topic}/{topic}/input"
  value_template: '{{{{ value_json.timeout }}}}'
  unit_of_measurement: "ms"
  force_update: True

- platform: template
  sensors:
    {name}_timeout_human_readable:
      friendly_name: "{f_name} Reset Timeout"
      unit_of_measurement: "hours"
      value_template: "{{{{ states('sensor.{name}_timeout') | float / 3600000 | round(1) }}}}"

- platform: mqtt
  name: "{f_name} Active State"
  state_topic: "tele/{base_topic}/{topic}/output"
  value_template: '{{{{ value_json.state }}}}'
  force_update: True

- platform: mqtt
  name: "{f_name} Active Fan State"
  state_topic: "tele/{base_topic}/{topic}/output"
  value_template: '{{{{ value_json.fan }}}}'
  force_update: True

- platform: mqtt
  name: "{f_name} Power Source"
  state_topic: "tele/{base_topic}/{topic}/sensors"
  value_template: '{{{{ value_json.powerSource }}}}'
  force_update: True

- platform: template
  sensors:
    {name}_temp_on:
      friendly_name: "{f_name} Temp On"
      unit_of_measurement: "°C"
      value_template: >-
        {{% if states('sensor.{name}_active_state').state | string == "cooling" or states('sensor.{name}_active_state').state | string == "heating" %}}
          {{{{states('sensor.{name}_ambient_temperature').state | float }}}}
        {{% endif %}}



"""

components = {
                'climate': climate,
                'sensor': sensor
             }
