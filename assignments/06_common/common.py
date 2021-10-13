#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-10-13
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Finding common values',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='FILE output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('file1',
                        help='FILE1',
                        metavar='FILE',
                        type=argparse.FileType('rt'),)

    parser.add_argument('file2',
                        help='FILE2',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

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


# --------------------------------------------------
if __name__ == '__main__':
    main()
