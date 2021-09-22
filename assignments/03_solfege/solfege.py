#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-09-22
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='solfege',
                        nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    answers = {}
    answers['Do'] = 'A deer, a female deer'
    answers['Re'] = 'A drop of golden sun'
    answers['Mi'] = 'A name I call myself'
    answers['Fa'] = 'A long long way to run'
    answers['Sol'] = 'A needle pulling thread'
    answers['La'] = 'A note to follow sol'
    answers['Ti'] = 'A drink with jam and bread'
    for notes in args.str:

        if notes not in answers:
            print(f'I don\'t know "{notes}"')
        else:
            print(notes + ', ' + answers[notes])


# --------------------------------------------------
if __name__ == '__main__':
    main()
