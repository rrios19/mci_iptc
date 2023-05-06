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

my ($file,$time) = @ARGV;
my @lines;
die "Missing file argument," unless defined $file;
die "Missing time argument," unless defined $time;

open FILE, '<', $file or die "Couldn't open testfile: $!";
@lines = <FILE>;
close FILE;
$file =~ s/\A(\w+)(\.\w+)?\z/${time}_$1\.json/;
open OUT,  '>', $file or die "Couldn't create file: $!";

foreach (@lines){
    next if s/\A(\*\w+\?)\n\z/\"$1\",/;
    next if s/\A(\w+):(\w+\?)\n\z/{\"$1\": [\"$2\"]},/;
    s/\A(\w+):(\w+)\s+(\w+)\n\z/{\"$1\": [\"$2\", \"$3\"]},/
}
$lines[-1] =~ s/,\z//;

say OUT '[';
foreach (@lines){
    say OUT "  $_"
}
say OUT ']';

close OUT;

print $file

