#!/usr/bin/env perl
use strict;
use warnings;
use Term::ANSIColor;

my $sonoffSrcDir = "/home/mark/projects/esp/Sonoff-Tasmota.mod/sonoff";
my $sonoffDir = "/tmp/sonoff";
my $arduinoDir = "/home/mark/projects/esp/tasmota-light-arduino";

my $buildDir = "/tmp/autoSonoff_arduino_build";
my $cacheDir = "/tmp/autoSonoff_arduino_cache";


`rsync -avhI --delete --progress -r $sonoffSrcDir/* $sonoffDir`;
`mkdir $buildDir`;
`mkdir $cacheDir`;

my $buildCommand = <<EOF;
$arduinoDir/arduino-builder \\
  -compile -logger=machine \\
  -hardware $arduinoDir/hardware \\
  -hardware $arduinoDir/portable/packages \\
  -tools $arduinoDir/tools-builder \\
  -tools $arduinoDir/hardware/tools/avr \\
  -tools $arduinoDir/portable/packages \\
  -built-in-libraries $arduinoDir/libraries \\
  -libraries $arduinoDir/portable/sketchbook/libraries \\
  -fqbn=esp8266:esp8266:esp8285:UploadTool=esptool,CpuFrequency=80,UploadSpeed=115200,FlashSize=1M0 \\
  -ide-version=10804 \\
  -build-path $buildDir \\
  -warnings=none \\
  -build-cache $cacheDir \\
  -prefs=build.warn_data_percentage=75 \\
  -prefs=runtime.tools.mkspiffs.path=$arduinoDir/portable/packages/esp8266/tools/mkspiffs/0.1.2 \\
  -prefs=runtime.tools.xtensa-lx106-elf-gcc.path=$arduinoDir/portable/packages/esp8266/tools/xtensa-lx106-elf-gcc/1.20.0-26-gb404fb9-2 \\
  -prefs=runtime.tools.esptool.path=$arduinoDir/portable/packages/esp8266/tools/esptool/0.4.9 \\
  -verbose \\
  $sonoffDir/sonoff.ino
EOF

<>;
while (<>) {
  chomp;             # remove newline
  my @line = split(/\t/,$_);
  # id
  # module
  # ip
  # mac
  # MQTT_GRPTOPIC
  # APP_POWERON_STATE
  # MQTT_FULLTPIC
  # FRIENDLY_NAME
  # MQTT_TOPIC
  # comments

  $line[7] =~ s/id/$line[0]/;
  $line[8] =~ s/id/$line[0]/;

  print "Modifying sonoff directory for '$line[7]'\n";
  #device specific not in user_config_override.h
  (my $hostname = $line[7]) =~ s/\//-/g;
  `sed -i 's/#define WIFI_HOSTNAME.*/#define WIFI_HOSTNAME "$hostname"/' $sonoffDir/sonoff.ino`;
  `sed -i 's/#define MODULE.*/#define MODULE $line[1]/' $sonoffDir/sonoff.ino`;

  my $filename = "$sonoffDir/user_config_override.h";
  open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";

  #device specific in user_config_override.h
  print $fh "#define MQTT_FULLTOPIC \"$line[6]\"\n";
  print $fh "#define MQTT_GRPTOPIC \"$line[4]\"\n";
  print $fh "#define MQTT_TOPIC \"$line[8]\"\n";
  print $fh "#define FRIENDLY_NAME \"$line[7]\"\n";
  print $fh "#define APP_POWERON_STATE $line[5]\n";

  #define CFG_HOLDER             0x20161206
  printf $fh "#define CFG_HOLDER 0x%08X\n", rand(0xffffffff);

  #same in every device
  print $fh "#define SAVE_STATE 0\n";
  print $fh "#define STA_SSID1 \"i3detroit-wpa\"\n";
  print $fh "#define STA_PASS1 \"i3detroit\"\n";
  print $fh "#define STA_SSID2 \"i3detroit\"\n";
  print $fh "#define STA_PASS2 \"\"\n";
  print $fh "#define WIFI_CONFIG_TOOL  WIFI_RETRY\n";
  print $fh "#define MQTT_HOST \"10.13.0.22\"\n";
  print $fh "#define MQTT_USER \"\"\n";
  print $fh "#define MQTT_PASS \"\"\n";
  print $fh "#define TIME_DST Second, Sun, Mar, 2, -240\n";
  print $fh "#define TIME_STD First, Sun, Nov, 2, -300\n";
  print $fh "#define APP_TIMEZONE 99\n";


  print $fh "#undef MQTT_HOST_DISCOVERY\n";
  print $fh "#undef USE_I2C\n";
  print $fh "#undef USE_BH1750\n";
  print $fh "#undef USE_BMP\n";
  print $fh "#undef USE_HTU\n";
  print $fh "#undef USE_SHT\n";
  print $fh "#undef USE_IR_REMOTE\n";
  print $fh "#undef USE_WS2812\n";
  print $fh "#undef USE_WS2812_CTYPE\n";

  close $fh;

  `$buildCommand`;
  my $programCommand = "curl 'http://$line[2]/u2' -F 'name=\@$buildDir/sonoff.ino.bin'";
  my $result = `$programCommand`;

  if($? != 0) {
    print color("red"), "non-zero return, maybe it's not on the network?\n", color("reset");
  } elsif ($result =~ /failed/) {
    $result =~ /body>.*<h3>(.*)<form action/;
    print color("red"), "upload failed, stop fucking up\n", color("reset");
    print "\n$1\n\n";
  } else {
    print color("green"), "upload win\n", color("reset");
  }

}
