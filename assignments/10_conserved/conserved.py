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

    parser.add_argument('file',
                        help='find conserved bases',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)

    seqs = args.file.read().splitlines()

    print('\n'.join(seqs))

    for i in range(len(seqs[0])):
        bases = []
        for seq in seqs:
            bases += seq[i]

        print(bases)
        if all([bases[0] == base for base in bases]):
            print('|', end='')
        else:
            print('x', end='')

    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
