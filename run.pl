#!/usr/bin/env perl
use strict;
use warnings;

<>;
while (<>) {
  if(!eof) {
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
    print "#define MQTT_FULLTOPIC \"$line[6]\"\n";
    print "#define MQTT_GRPTOPIC \"$line[4]\"\n";
    print "#define MQTT_TOPIC \"$line[8]\"\n";
    print "#define FRIENDLY_NAME \"$line[7]\"\n";
    print "#define APP_POWERON_STATE \"$line[5]\"\n";


    (my $hostname = $line[8]) =~ s/\//-/g;
    print "#define WIFI_HOSTNAME \"$hostname\"\n";
    print "#define MODULE \"$line[1]\"\n";
    print "\n\n";
  }
}
