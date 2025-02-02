#!/usr/bin/env python3
"""
Author : Daniel Flick  <danielflick@arizona.edu>
Date   : 2025-02-02
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description='Print greeting')
    parser.add_argument('-g', '--greeting', help='A greeting',
                        metavar='str', type=str, default='Howdy')
    parser.add_argument('-n', '--name', help='A name to greet',
                        metavar='str', type=str, default='Stranger')
    parser.add_argument('-e', '--excited', action="store_false",
                        help="End with bang, default is false")
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    if args.excited:
        print(f'{greeting}, {name}.')
    else:
        print(f'{greeting}, {name}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
