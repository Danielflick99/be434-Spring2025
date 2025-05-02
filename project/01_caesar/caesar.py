#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-05-02
Purpose: Caesar Cipher
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Encode or Decode a Message",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num_to_shift",
        help="The number of chars to shift",
        metavar="int",
        type=int,
        default=3,
    )

    parser.add_argument(
        "FILE", help="A readable input file name", metavar="STR", type=str
    )

    parser.add_argument(
        "-d", "--decode", help="Decode the message", action="store_true"
    )

    args = parser.parse_args()

    if not (os.path.isfile(args.FILE)):
        parser.error(f"No such file or directory: '{args.FILE}'")

    return args


# --------------------------------------------------


def caesar_shift(num_to_shift):

    encode = {}
    decode = {}

    # store the alphabet in a list
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_list = list(alpha)

    # create the encode and decode lookups
    # walk through each character in the alphabet
    x = 0
    for char in alpha:
        # determine the "caesar shift" value for each character
        cshift = num_to_shift

        # get and store the encoded and decoded character values
        encode[char] = alpha_list[(x + cshift) % 26]
        decode[char] = alpha_list[(x - cshift) % 26]
        # be sure to increment as you walk through the alphabet
        x += 1

    return (encode, decode)


def main():
    """Calcuate the encode/decode of a string"""

    args = get_args()

    encode, decode = caesar_shift(args.num_to_shift)

    fh = open(args.FILE, "rt")

    for line in fh:
        current_line = []
        for char in list(line.rstrip()):
            char = char.upper()

            if char not in encode:
                new_char = char
            else:
                if args.decode:
                    new_char = decode[char]
                else:
                    new_char = encode[char]
            current_line.append(new_char)

        print("".join(current_line))


# --------------------------------------------------
if __name__ == "__main__":
    main()
