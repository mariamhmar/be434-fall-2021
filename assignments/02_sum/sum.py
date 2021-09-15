#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-09-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Adding Numbers program',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument ('numbers',
                        metavar='INT',
                        type=int,
                        nargs= "+",
                        help='A positional argument')

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    #print(args.numbers)
    #print(sum(args.numbers))
    numbers = args.numbers
    
    strings = [str(n) for n in numbers]
    
    print('{} = {}'.format( ' + ' .join(strings), sum(numbers)))
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
