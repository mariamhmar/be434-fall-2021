#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-12-01
Purpose: Rock the Casbah
"""

import argparse
from typing import NamedTuple, TextIO
import sys


class Args(NamedTuple):
    """ Command-line arguments """
    positional: str
    string_arg: str
    int_arg: int
    file: TextIO
    on: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Printing Backwards',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('files',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-o',
                        '--outfile',
                        help='FILE',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    for fh in args.files:
        for line in reversed(list(fh)):
            print(line.rstrip(), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
