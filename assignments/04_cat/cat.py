#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-09-26
Purpose: Concatenating Files
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Concatenating files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-n',
                        '--number',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.files:
        line_num = 0
        for line in fh:
            line_num += 1
            if args.number:
                print('{:6}\t{}'.format(line_num, line.rstrip()))
            else:
                print(line.rstrip())


# ------------------------------s--------------------
if __name__ == '__main__':
    main()
