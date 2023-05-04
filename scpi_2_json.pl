#!/usr/bin/perl
# Tecnologico de Costa Rica
# Integrated Power Testing Module for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: Format a text file into a json file
# Usage: perl scpi_2_json.pl <file name> <target json>

use feature 'say'; 
use warnings;
use strict;

my ($file,$json) = @ARGV;
my @lines;
die "No file name," unless defined $file;
die "No json name," unless defined $json;

open FILE, '<', $file or die "Couldn't open file: $!";
@lines = <FILE>;
close FILE;
open OUT,  '>', $json or die "Couldn't open file: $!";

foreach (@lines){
    s/\A(\S+)\n\z/\"$1\",/;
    s/\A(\S+)\s+(\S+)\n\z/{\"$1\": \"$2\"},/
}
$lines[-1] =~ s/,\z//;

say OUT '[';
foreach (@lines){
    say OUT "  $_"
}
say OUT ']';

close OUT

