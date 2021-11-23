#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-11-22
Purpose: Rock the Casbah
"""

import argparse
import re
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('PATTERN',
                        metavar='Pattern',
                        help='Search pattern')

    parser.add_argument('FILE',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=sys.stdout)
   
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)

# --------------------------------------------------
if __name__ == '__main__':
    main()
