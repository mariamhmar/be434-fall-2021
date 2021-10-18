#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-10-15
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='SEQ',
                        nargs= '+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sequence_list = args.seq

    iupac = {'A':'A', 'C':'C', 'G':'G', 'T':'T', 'U':'U', 
            'R':'[AG]', 'Y':'[CT]', 'S':'[GC]', 'W':'[AT]', 'K':'[GT]',
            'M':'[AC]', 'B':'[CGT]', 'D':'[AGT]', 'H':'[ACT]', 
            'V':'[ACG]', 'N': '[ACGT]'}

    for seq in sequence_list:
        for item in seq:
            print(iupac.get(item))
    for seq in sequence_list:
        for item += 1:
        print(item, iupac.get(item))  
      

# --------------------------------------------------
if __name__ == '__main__':
    main()

