#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-02-20
Purpose: Produce DNA Reverse Complement
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Print the reverse complement of DNA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", type=str, metavar="str", help="Input sequence or file")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Reverse the DNA sequence, input thrugh file or stdin"""

    args = get_args()

    if os.path.isfile(args.text):
        strand = open(args.text).read().rstrip()
    else:
        strand = args.text

    strand_rc = {
        "T": "A",
        "A": "T",
        "C": "G",
        "G": "C",
        "t": "a",
        "a": "t",
        "c": "g",
        "g": "c",
    }

    print("".join([strand_rc[base] for base in strand[::-1]]))


# --------------------------------------------------
if __name__ == "__main__":
    main()
