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
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='FILE',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)
   
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)

    for fh in args.FILE:
        num_lines = 0
        num_words = 0
        num_chars = 0
    for line in fh:
            num_lines += 1
            num_words += len(line.split())
    
    for line in args.pattern:
        match = re.match(pattern, line)
        print(match, fh)
 
  

# --------------------------------------------------
if __name__ == '__main__':
    main()
