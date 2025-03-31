#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-03-27
Purpose: Finding Common Words
"""

import argparse

# from subprocess import STDOUT
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Finding common words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "FILE1", help="A readable file", metavar="FILE", type=argparse.FileType("rt")
    )

    parser.add_argument(
        "FILE2", help="A readable file", metavar="FILE", type=argparse.FileType("rt")
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="str",
        type=str,
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    strand1 = args.FILE1.read().rstrip()
    strand1_w = strand1.split()

    strand2 = args.FILE2.read().rstrip()
    strand2_w = strand2.split()

    common_words = set(strand1_w).intersection(strand2_w)

    if args.outfile == sys.stdout:
        print("\n".join(sorted(common_words)))
    else:
        out_fh = open(args.outfile, "wt")
        out_fh.write("\n".join(sorted(common_words)) + "\n")


# --------------------------------------------------
if __name__ == "__main__":
    main()
