#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-11-02
Purpose: FASTA sequence files
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='FASTA sequence files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('readable file',
                        metavar='FILE',
                        help='Input files',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='Output Directory',
                        metavar='DIR',
                        default='split')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
def main():
    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    
args = get_args()

# --------------------------------------------------
if __name__ == '__main__':
    main()
