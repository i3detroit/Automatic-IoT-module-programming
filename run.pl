#!/usr/bin/env perl
use strict;
use warnings;

<>;
while (<>) {
  if(!eof) {
    chomp;             # remove newline
    my @line = split(/\t/,$_);
    print join("\n",@line),"\n\n";
    #number/topic, type, ip,          grouptopic, friendly name, comment
  }
}
