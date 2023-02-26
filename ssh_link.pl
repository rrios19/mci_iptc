#!/usr/bin/perl
# Perl v5.36.0 on macOS Ventura 13.0.1
# Author: Ronald Rios
# Description: ssh

use feature 'say';
use warnings;
use strict;

my $ip;

foreach (`arp -a`){
    $ip = $1 if /raspberrypi\s+\((.*)\)/
}

unless ($ip){
    say "Can't find a raspberry" 
} else {
    say "Connecting to $ip";
    exec 'ssh',"pi\@$ip"
}

