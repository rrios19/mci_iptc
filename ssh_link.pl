#!/usr/bin/perl
# Perl v5.36.0 on macOS Ventura 13.0.1
# Author: Ronald Rios
# Description: Link by ssh and run the app

use warnings;
use strict;
use Net::SSH qw{ssh};

my $ip = 192.168.1.19; #Static IP
my $command = qw{perl -e 'print "Hello from PI\n"'};

ssh("pi\@$ip", $command) 





#foreach (`arp -a`){
#    $ip = $1 if /raspberrypi\s+\((.*)\)/
#}

#unless ($ip){
#    say "Can't find a raspberry" 
#} else {
#    say "Connecting to $ip";
#    exec 'ssh',"pi\@$ip"
#}

