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
                        help='out txt',
                        metavar='FILE',
                        type=str,
                        default='out.text')

    parser.add_argument('-c',
                        '--codons',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True
                         )

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='out.txt')                     
                        
    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    for line in args.codons:
        print(line.rstrip().split())
    """Make a jazz noise here"""

    args = get_args()
    print('seq =', args.sequence)
    print('codons =', args.codons)
    print('outfile =', args.outfile)

# --------------------------------------------------
if __name__ == '__main__':
    main()
