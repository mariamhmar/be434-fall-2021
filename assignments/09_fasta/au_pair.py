#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-11-02
Purpose: FASTA sequence files
"""

import argparse
import os
from Bio import SeqIO

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='FASTA sequence files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        help='Input files',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='Output Directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for fh in args.files:
        root, ext = os.path.splitext(os.path.basename(fh.name))
        forward = open(os.path.join(out_dir, root + '_1' + ext), 'wt')
        reverse = open(os.path.join(out_dir, root + '_2' + ext), 'wt')
        parser = SeqIO.parse(fh, 'fasta')

        for i, rec in enumerate(parser):
            SeqIO.write(rec, forward if i % 2 == 0 else reverse, 'fasta')

    print(f'Done, see output in "{out_dir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
