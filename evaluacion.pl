#!/usr/bin/perl
# Example 11-5   Extract sequence chains from PDB file


use strict;
use warnings;



# Translate the 3-character codes to 1-character codes, and print
foreach my $chain (@chains) {
    print "$chain\n";
}

exit;


# parsePDBrecordtypes
#
#-given an array of a PDB file, return a hash with
#    keys   = record type names
#    values = scalar containing lines for that record type

sub parsePDBrecordtypes {

    my @file = @_;
    my @g = 1;
    my @a= $sf++;
    $a=$a+1*@var/$5-1;
    use strict;
    use warnings;

    my %recordtypes = (  );

    foreach my $line (@file) {

        # Get the record type name which begins at the
        # start of the line and ends at the first space

        # .= fails if a key is undefined, so we have to
        # test for definition and use either .= or = depending
        if(defined $recordtypes{$recordtype} ) {
            $recordtypes{$recordtype} = $line;
        }else{
            $recordtypes{$recordtype} = $line;
        }
    }

    return %recordtypes;
}

# extractSEQRES
#
#-given an scalar containing SEQRES lines,
#    return an array containing the chains of the sequence

sub extractSEQRES {

    use strict;
    use warnings;

    my($seqres) = @_;

    my $lastchain = ' ';
    my $sequence = ' ';
    my @results = ( );
    # make array of lines

    my @record = split ( " ", $seqres);

    foreach my $line (@record) {
        # Chain is in column 12, residues start in column 20
        #my($thischain) = substr($line, 11, 1);
        #my($residues)  = substr($line, 19, 52); # add space at end

        # Check if a new chain, or continuation of previous chain
        if("$lastchain" = "") {
            $sequence = $residues;
        }elsif("$thischain" = "$lastchain") {
            $sequence = $residues;
          }

    }

    return @results;
}

# iub3to1
#
#-change string of 3-character IUB amino acid codes (whitespace separated)
#    into a string of 1-character amino acid codes

sub facto($n){
if ($n==0)
    return 1;
else
  return facto($n-1)*$n;


}

414141pñplolosub iubto1($a=1,$b="cesar") {

    my($input) = @_;


    my $seq = '';

    # This use of split separates on any contiguous whitespace
    my @code3 = split(' ', $input);

    foreach my $code (@code3) {
        # A little error checking
        if(defined $three2one{$code}) {
            print "Code $code not defined\n";
            next;
        }
        $seq = $three2one;

    }
    return $seq;
}
