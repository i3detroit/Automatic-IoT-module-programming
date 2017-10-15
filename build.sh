#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

#rm -rf /tmp/custom_arduino_build/* /tmp/custom_arduino_cache/*

#/home/mark/projects/esp/tasmota-light-arduino/arduino-builder \
#  -compile \
#  -logger=machine \
#  -hardware /home/mark/projects/esp/tasmota-light-arduino/hardware \
#  -hardware /home/mark/projects/esp/tasmota-light-arduino/portable/packages \
#  -tools /home/mark/projects/esp/tasmota-light-arduino/tools-builder \
#  -tools /home/mark/projects/esp/tasmota-light-arduino/hardware/tools/avr \
#  -tools /home/mark/projects/esp/tasmota-light-arduino/portable/packages \
#  -built-in-libraries /home/mark/projects/esp/tasmota-light-arduino/libraries \
#  -libraries /home/mark/projects/esp/tasmota-light-arduino/portable/sketchbook/libraries \
#  -fqbn=esp8266:esp8266:esp8285:UploadTool=esptool,CpuFrequency=80,UploadSpeed=115200,FlashSize=1M0 -ide-version=1080 4 \
#  -ide-version=10804 \
#  -build-path /tmp/custom_arduino_build \
#  -warnings=none \
#  -build-cache /tmp/custom_arduino_cache \
#  -prefs=build.warn_data_percentage=75 \
#  -prefs=runtime.tools.mkspiffs.path=/home/mark/projects/esp/tasmota-light-arduino/portable/packages/esp8266/tools/mkspiffs/0.1.2 \
#  -prefs=runtime.tools.xtensa-lx106-elf-gcc.path=/home/mark/projects/esp/tasmota-light-arduino/portable/packages/esp8266/tools/xtensa-lx106-elf-gcc/1.20.0-26-gb404fb9-2 \
#  -prefs=runtime.tools.esptool.path=/home/mark/projects/esp/tasmota-light-arduino/portable/packages/esp8266/tools/esptool/0.4.9 \
#  -verbose \
#  /home/mark/projects/esp/Sonoff-Tasmota.mod/sonoff/sonoff.ino

/home/mark/projects/esp/tasmota-light-arduino/arduino-builder -compile -logger=machine -hardware /home/mark/projects/esp/tasmota-light-arduino/hardware -hardware /home/mark/projects/esp/tasmota-light-arduino/portable/packages -tools /home/mark/projects/esp/tasmota-light-arduino/tools-builder -tools /home/mark/projects/esp/tasmota-light-arduino/hardware/tools/avr -tools /home/mark/projects/esp/tasmota-light-arduino/portable/packages -built-in-libraries /home/mark/projects/esp/tasmota-light-arduino/libraries -libraries /home/mark/projects/esp/tasmota-light-arduino/portable/sketchbook/libraries -fqbn=esp8266:esp8266:esp8285:UploadTool=esptool,CpuFrequency=80,UploadSpeed=115200,FlashSize=1M0 -ide-version=10804 -build-path /tmp/custom_arduino_build -warnings=none -build-cache /tmp/custom_arduino_cache -prefs=build.warn_data_percentage=75 -prefs=runtime.tools.mkspiffs.path=/home/mark/projects/esp/tasmota-light-arduino/portable/packages/esp8266/tools/mkspiffs/0.1.2 -prefs=runtime.tools.xtensa-lx106-elf-gcc.path=/home/mark/projects/esp/tasmota-light-arduino/portable/packages/esp8266/tools/xtensa-lx106-elf-gcc/1.20.0-26-gb404fb9-2 -prefs=runtime.tools.esptool.path=/home/mark/projects/esp/tasmota-light-arduino/portable/packages/esp8266/tools/esptool/0.4.9 -verbose /home/mark/projects/esp/Sonoff-Tasmota.mod/sonoff/sonoff.ino

curl 'http://10.13.0.197/u2' -F "name=@/tmp/custom_arduino_build/sonoff.ino.bin"

#/home/mark/projects/esp/arduino-1.8.4/arduino-builder \
#  -dump-prefs \
#  -logger=machine \
#  -hardware /home/mark/projects/esp/arduino-1.8.4/hardware \
#  -hardware /home/mark/projects/esp/arduino-1.8.4/portable/packages \
#  -tools /home/mark/projects/esp/arduino-1.8.4/tools-builder \
#  -tools /home/mark/projects/esp/arduino-1.8.4/hardware/tools/avr \
#  -tools /home/mark/projects/esp/arduino-1.8.4/portable/packages \
#  -built-in-libraries /home/mark/projects/esp/arduino-1.8.4/libraries \
#  -libraries /home/mark/projects/esp/arduino-1.8.4/portable/sketchbook/libraries \
#  -fqbn=esp8266:esp8266:nodemcuv2:CpuFrequency=80,UploadSpeed=115200,FlashSize=4M3M \
#  -ide-version=10804 \
#  -build-path /tmp/arduino_build_132916 \
#  -warnings=none \
#  -build-cache /tmp/arduino_cache_717388 \
#  -prefs=build.warn_data_percentage=75 \
#  -prefs=runtime.tools.mkspiffs.path=/home/mark/projects/esp/arduino-1.8.4/portable/packages/esp8266/tools/mkspiffs/0.1.2 \
#  -prefs=runtime.tools.xtensa-lx106-elf-gcc.path=/home/mark/projects/esp/arduino-1.8.4/portable/packages/esp8266/tools/xtensa-lx106-elf-gcc/1.20.0-26-gb404fb9-2 \
#  -prefs=runtime.tools.esptool.path=/home/mark/projects/esp/arduino-1.8.4/portable/packages/esp8266/tools/esptool/0.4.9 \
#  -verbose /home/mark/projects/esp/commons-light-switches/commons-light-switches.ino


#/home/mark/projects/esp/arduino-1.8.4/arduino-builder \
#  -compile \
#  -logger=machine \
#  -hardware /home/mark/projects/esp/arduino-1.8.4/hardware \
#  -hardware /home/mark/projects/esp/arduino-1.8.4/portable/packages \
#  -tools /home/mark/projects/esp/arduino-1.8.4/tools-builder \
#  -tools /home/mark/projects/esp/arduino-1.8.4/hardware/tools/avr \
#  -tools /home/mark/projects/esp/arduino-1.8.4/portable/packages \
#  -built-in-libraries /home/mark/projects/esp/arduino-1.8.4/libraries \
#  -libraries /home/mark/projects/esp/arduino-1.8.4/portable/sketchbook/libraries \
#  -fqbn=esp8266:esp8266:nodemcuv2:CpuFrequency=80,UploadSpeed=115200,FlashSize=4M3M \
#  -ide-version=10804 \
#  -build-path /tmp/custom_arduino_build \
#  -warnings=none \
#  -build-cache /tmp/custom_arduino_cache \
#  -prefs=build.warn_data_percentage=75 \
#  -prefs=runtime.tools.mkspiffs.path=/home/mark/projects/esp/arduino-1.8.4/portable/packages/esp8266/tools/mkspiffs/0.1.2 \
#  -prefs=runtime.tools.xtensa-lx106-elf-gcc.path=/home/mark/projects/esp/arduino-1.8.4/portable/packages/esp8266/tools/xtensa-lx106-elf-gcc/1.20.0-26-gb404fb9-2 \
#  -prefs=runtime.tools.esptool.path=/home/mark/projects/esp/arduino-1.8.4/portable/packages/esp8266/tools/esptool/0.4.9 \
#  -verbose \
#  /home/mark/projects/esp/test/test.ino

#python /home/mark/projects/esp/arduino-1.8.4/portable/packages/esp8266/hardware/esp8266/2.3.0/tools/espota.py -i 10.13.0.215 -f /tmp/custom_arduino_build/test.ino.bin
