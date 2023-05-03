#!/usr/bin/perl

my ($file) = @ARGV;
my @lines;
die "No arguments," unless defined $file;

open FILE, '<', $file or die "Couldn't open file: $!";
@lines = <FILE>;
close FILE;
$file =~ s/(\.\w+)?\z/.json/;
open OUT,  '>', $file or die "Couldn't open file: $!";


foreach (@lines){
    s/\A(\S+)\n\z/\"$1\",\n/;
    s/\A(\S+)\s+(\S+)\n\z/{\"$1\": \"$2\"},\n/
}
$lines[-1] =~ s/,?\n\z/\n/;


print OUT "[\n";
foreach (@lines){
    print OUT "  $_"
}
print OUT "]\n";

close OUT

