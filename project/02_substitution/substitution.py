#!/usr/bin/env python3
"""

Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-05-02
Purpose: Encode Using Random Substitution Cipher
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Encode or Decode a Message",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-s", "--seed", help="The random seed", metavar="int", type=int, default=3
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


def substitution(seed):
    random.seed(seed)
    encode = {}
    decode = {}

    # store the alphabet in a list
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_list = list(alpha)

    random_list = random.sample(alpha_list, len(alpha_list))

    # print(alpha_list)
    # print(random_list)

    # create the encode and decode lookups
    # walk through each character in the alphabet
    x = 0
    for char in alpha:

        # get and store the encoded and decoded character values
        encode[char] = random_list[x]
        decode[random_list[x]] = char
        # be sure to increment as you walk through the alphabet
        x += 1

    # print(encode, decode)
    return (encode, decode)


def main():
    """Calcuate the encode/decode of a string"""

    args = get_args()

    encode, decode = substitution(args.seed)

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
