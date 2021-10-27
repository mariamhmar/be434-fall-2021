#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-10-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
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
        parser.error(f'--kmer "{args.kmer}" must be greater than 0')
 
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    words1 = {}
    for line in args.file1:
        for word in line.split():
            words1[word] = 1

    words2 = {}
    for line in args.file2:
        for word in line.split():
            words2[word] = 1

    for key in words1:
        if key in words2:
            print(key)

    def find_kmers(seq, k):
        n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]



# --------------------------------------------------
if __name__ == '__main__':
    main()
