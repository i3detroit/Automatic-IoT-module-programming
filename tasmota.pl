#!/usr/bin/env perl
use strict;
use warnings;
use Term::ANSIColor;

my $sonoffSrcDir = "../Sonoff-Tasmota.mod/sonoff";
my $arduinoDir = "../tasmota-light-arduino";
my $codeDir = "/tmp/sonoff";

my $buildDir = "/tmp/autoSonoff_arduino_build";
my $cacheDir = "/tmp/autoSonoff_arduino_cache";


#TODO: if file named 'hosts' older than XXX run command from readme
#sudo nmap -sP 10.13.0.0-255 | grep -v "Host" | tail -n +3 | tr '\n' ' ' | sed 's|Nmap|\nNmap|g' |  grep "MAC Address" | perl -pe 's/.*report for (?:([^ ]*) \()?((?:[0-9]{1,3}\.?){4})\)? MAC Address: ([A-Z0-9:]*).*/$1 $2 $3/'

`rsync -avhI --delete --progress -r $sonoffSrcDir/* $codeDir`;
`mkdir $buildDir`;
`mkdir $cacheDir`;

sub buildCommand {
  my ($device, $flash) = @_;
  my $fqbn;
  if($device eq "generic") {
    $fqbn = "esp8266:esp8266:$device:CpuFrequency=80,FlashFreq=40,FlashMode=dout,FlashSize=$flash";
  } elsif ($device eq "esp8285") {
    $fqbn = "esp8266:esp8266:$device:UploadTool=esptool,CpuFrequency=80,UploadSpeed=115200,FlashSize=$flash";
  } else {
    print color("red"), "Unknown Device Type\n", color("reset");
    exit(42);
  }
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
    $codeDir/sonoff.ino
EOF
}

<>;
while (<>) {
  chomp;             # remove newline
  (my $id, my $module, my $ip, my $mac, my $MQTT_GRPTOPIC, my $APP_POWERON_STATE, my $MQTT_FULLTOPIC, my $FRIENDLY_NAME, my $MQTT_TOPIC) = split(/\t/,$_);

  if( ! length $MQTT_TOPIC > 0) {
    print color("red"), "Hit a blank line\n", color("reset");
    exit(1);
  }

  $FRIENDLY_NAME =~ s/%id%/$id/;
  $MQTT_TOPIC =~ s/%id%/$id/;

  print "Modifying sonoff directory for '$FRIENDLY_NAME'\n";
  #device specific not in user_config_override.h
  (my $hostname = $MQTT_TOPIC) =~ s/\//-/g;
  `sed -i 's/#define WIFI_HOSTNAME.*/#define WIFI_HOSTNAME "$hostname"/' $codeDir/sonoff.h`;
  `sed -i 's/#define MODULE.*/#define MODULE $module/' $codeDir/sonoff.h`;

  my $filename = "$codeDir/user_config_override.h";
  open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";

  #device specific in user_config_override.h
  print $fh "#define MQTT_FULLTOPIC \"$MQTT_FULLTOPIC\"\n";
  print $fh "#define MQTT_GRPTOPIC \"$MQTT_GRPTOPIC\"\n";
  print $fh "#define MQTT_TOPIC \"$MQTT_TOPIC\"\n";
  print $fh "#define FRIENDLY_NAME \"$FRIENDLY_NAME\"\n";
  print $fh "#define APP_POWERON_STATE $APP_POWERON_STATE\n";

  #define CFG_HOLDER             0x20161206
  printf $fh "#define CFG_HOLDER 0x%08X\n", rand(0xffffffff);

  #same in every device
  print $fh "#define SAVE_STATE 0\n";
  print $fh "#define STA_SSID1 \"i3detroit-iot\"\n";
  print $fh "#define STA_PASS1 \"securityrisk\"\n";
  print $fh "#define STA_SSID2 \"i3detroit\"\n";
  print $fh "#define STA_PASS2 \"\"\n";
  print $fh "#define WIFI_CONFIG_TOOL  WIFI_RETRY\n";
  print $fh "#define MQTT_HOST \"10.13.0.22\"\n";
  print $fh "#define MQTT_USER \"\"\n";
  print $fh "#define MQTT_PASS \"\"\n";
  print $fh "#define TIME_DST Second, Sun, Mar, 2, -240\n";
  print $fh "#define TIME_STD First, Sun, Nov, 2, -300\n";
  print $fh "#define APP_TIMEZONE 99\n";
  print $fh "#define SERIAL_LOG_LEVEL LOG_LEVEL_NONE\n";


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

  #SONOFF_TOUCH: esp8285
  #everything else: generic
  my $device = 'generic';
  if(grep( /^$module$/, ('SONOFF_TOUCH', 'SONOFF_4CH', 'SONOFF_BRIDGE') ) ) {
    $device = 'esp8285';
  }
  my $buildCommand = buildCommand($device, '1M0');
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

    print "found ip from other file: $ip\n";

  } else {
    print "ip from tsv: $ip\n";
  }
  my $programCommand = "curl 'http://$ip/u2' -F 'name=\@$buildDir/sonoff.ino.bin'";
  print "$programCommand\n";
  my $result = `$programCommand`;


  if($? != 0) {
    print color("red"), "non-zero return, maybe it's not on the network?\n", color("reset");
    exit(1);
  } elsif ($result =~ /Failed/) {
    $result =~ /body>.*<h3>(.*)<form action/;
    print color("red"), "upload failed, stop fucking up\n", color("reset");
    print "\n$1\n\n";
    exit(1);
  } elsif($result =~ /Successful/) {
    print color("green"), "upload win\n", color("reset");
  } else {
    print color("yellow"), "unknown upload status\n", color("reset");
    print "\n\n$result\n\n";
  }

}
