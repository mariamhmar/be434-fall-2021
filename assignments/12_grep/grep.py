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

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

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
    num_FILE = len(args.FILE)

    for fh in args.FILE:
        for line in fh:
            if re.search(args.pattern, line,
                         re.IGNORECASE if args.insensitive else 0):
                # print(line, end='',file=args.outfile)

                print('{}{}'.format(
                    f'{fh.name}:' if num_FILE > 1 else '', line),
                    end='', file=args.outfile)
            # if re.search(args.pattern, line):
            # print(line, end='', file=args.outfile)

# for line in fh:
#   num_lines += 1
#  num_words += len(line.split())

# for line in args.pattern:
#  match = re.match(pattern, line)
# print(match, fh)


# --------------------------------------------------
if __name__ == '__main__':
    main()
