#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-10-26
Purpose: Program that Prints Kmers
"""

import argparse
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-k',
                        '--kmer',
                        help='Integer',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('file1',
                        help='FILE1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),)

    parser.add_argument('file2',
                        help='FILE2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    kmers1 = count_kmers(args.file1, args.kmer)
    kmers2 = count_kmers(args.file2, args.kmer)

    for common in set(kmers1).intersection(set(kmers2)):
        print('{:10} {:5} {:5}'.format(
            common, kmers1.get(common), kmers2.get(common)))


def count_kmers(fh, k):
    '''count kmers in file handle'''

    kmers = defaultdict(int)
    for line in fh:
        for word in line.split():
            for kmer in find_kmers(word, k):
                kmers[kmer] += 1

    return kmers


def find_kmers(seq, k):
    """ kmers value"""
    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
