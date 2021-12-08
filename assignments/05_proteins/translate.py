#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-12-08
Purpose: Rock the Casbah
"""

import argparse
from typing import NamedTuple, TextIO
 

class Args(NamedTuple):
    """ Command-line arguments """
    positional: str
    string_arg: str
    int_arg: int
    file: TextIO
    on: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-o',
                        '--output',
                        help='output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    parser.add_argument('-c',
                        '--codons',
                        help='Input codon file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)


    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(args)

    codon_table = {}
    for line in args.codons:
        key, val = line.split()
        codon_table[key] = val

    k= 3
    seq = args.sequence.upper()
    protein = ''
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        protein += codon_table.get(codon, '-')
        #print(codon, codon_table.get(codon, '-'), end='')

    print(protein, file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')

    #pprint(codon_table)

# --------------------------------------------------
if __name__ == '__main__':
    main()
