#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-11-09
Purpose: Show Conseved bases in two or more aligned sequences
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find Conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        help='find conserved bases',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    FILE = args.FILE.read().strip()
    seqs = FILE.splitlines()

    print(FILE)

    for i in range(len(seqs[0])):
        bases = [base[i] for base in seqs]
        if bases.count(bases[0]) == len(bases):
            print('|', end='')
        else:
            print('x', end='')
    
    print()

  

# --------------------------------------------------
if __name__ == '__main__':
    main()
