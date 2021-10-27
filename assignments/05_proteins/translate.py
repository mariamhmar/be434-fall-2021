#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str ',
                        help='DNA/RNA sequence')

    parser.add_argument('-o',
                        '--output',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.text')

    parser.add_argument('-c',
                        '--codons',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='out.txt')                     
                        
    return parser.parse_args()


# --------------------------------------------------
def main():
    
    """Make a jazz noise here"""

    args = get_args()
    print(args)

    codon_table={}
    for line in args.codons:
        key, val = line.split()
        codon_table[key] = val
    k= 3
    seq = args.sequence
    protein = []
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        print(codon, codon_table.get(codon, '_'), end='')

    print(protein, file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')

    pprint(codon_table)

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
