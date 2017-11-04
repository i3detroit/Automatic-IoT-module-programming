#!/usr/bin/env perl
use strict;
use warnings;
use Term::ANSIColor;

my $arduinoDir = "/home/mark/projects/esp/esp-arduino";

my $buildDir = "/tmp/custom_arduino_build";
my $cacheDir = "/tmp/custom_arduino_cache";


`mkdir $buildDir`;
`mkdir $cacheDir`;

sub buildCommand {
  my ($fqbn, $ino) = @_;
  #my $fqbn = "esp8266:esp8266:$device:CpuFrequency=80,FlashFreq=40,FlashMode=dout,FlashSize=$flash";
  return <<EOF;
  $arduinoDir/arduino-builder \\
    -compile \\
    -logger=machine \\
    -hardware $arduinoDir/hardware \\
    -hardware $arduinoDir/portable/packages \\
    -tools $arduinoDir/tools-builder \\
    -tools $arduinoDir/hardware/tools/avr \\
    -tools $arduinoDir/portable/packages \\
    -built-in-libraries $arduinoDir/libraries \\
    -libraries $arduinoDir/portable/sketchbook/libraries \\
    -fqbn=$fqbn \\
    -ide-version=10804 \\
    -build-path $buildDir \\
    -warnings=none \\
    -build-cache $cacheDir \\
    -prefs=build.warn_data_percentage=75 \\
    -prefs=runtime.tools.mkspiffs.path=$arduinoDir/portable/packages/esp8266/tools/mkspiffs/0.1.2 \\
    -prefs=runtime.tools.esptool.path=$arduinoDir/portable/packages/esp8266/tools/esptool/0.4.9 \\
    -prefs=runtime.tools.xtensa-lx106-elf-gcc.path=$arduinoDir/portable/packages/esp8266/tools/xtensa-lx106-elf-gcc/1.20.0-26-gb404fb9-2 \\
    -verbose \\
    $ino
EOF
}

<>;
while (<>) {
  chomp;             # remove newline
  my ($name, $ip, $mac, $fqbn) = split(/\t/,$_);

  my $codeDir = "/home/mark/projects/esp/custom-mqtt-programs/$name";
  print "Modifying sonoff directory for '$name'\n";

  my $buildCommand = buildCommand($fqbn, "$codeDir/$name.ino");
  print "$buildCommand\n";
  `$buildCommand`;
  if($? != 0) {
    print color("red"), "non-zero return, stop fucking up?\n", color("reset");
    exit(1);
  }


  if($ip eq "x") {
    #get ip
    #
    $ip = `grep "$mac" hosts | cut -d' ' -f2`;
    chomp $ip;

    if($ip eq "") {
      print color("red"), "No ip for device\n", color("reset");
      exit(42);
    }

    print "found ip from other file: '$ip'\n";

  } else {
    print "ip from tsv: $ip\n";
  }
  my $programCommand = "python $arduinoDir/portable/packages/esp8266/hardware/esp8266/2.3.0/tools/espota.py -i $ip -f $buildDir/$name.ino.bin";
  print "$programCommand\n";
  my $result = `$programCommand`;


  if($? != 0) {
    print color("red"), "non-zero return, maybe it's not on the network?\n", color("reset");
    exit(1);
  } else {
    print color("green"), "upload win\n", color("reset");
  }
}
