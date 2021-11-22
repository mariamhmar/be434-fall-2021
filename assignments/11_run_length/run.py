#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-11-16
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='str', help='A positional argument')

    args = parser.parse_args()

    if os.path.isfile(args.seq):
        args.seq = open(args.seq).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for seq in args.seq.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq: str) -> str:
    """run length encoding"""

    counts = []
    count = 0
    prev = ''
    for char in seq:
        if prev == '':
            prev = char
            count = 1
        elif char == prev:
            count += 1
        else:
            counts.append((prev, count))
            count = 1
            prev = char

    counts.append((prev, count))

    #print(counts)

    ret = ''
    for char, count in counts:
        #print(char, counts)
        ret += char + (str(count) if count > 1 else '')

    return ret


#--------------------------------------------
def test_rle():
    """Test rle"""

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


#--------------------------------------------
if __name__ == '__main__':
    main()
