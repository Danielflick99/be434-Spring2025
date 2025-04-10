#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-04-10
Purpose: Determine Commonalities of Two Sequences
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Add Your Purpose",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "FILE", help="A readable input file name", metavar="STR", type=str
    )

    args = parser.parse_args()

    if not (os.path.isfile(args.FILE)):
        parser.error(f"No such file or directory: '{args.FILE}'")

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    fh = open(args.FILE, "rt")

    seqs = [line.strip() for line in fh]

    conserved = ""

    for i in range(len(seqs[0])):
        chars = set([seq[i] for seq in seqs])
        conserved += "|" if len(chars) == 1 else "X"

    for seq in seqs:
        print(seq)

    print(conserved)


# ------------------------------------------------
if __name__ == "__main__":
    main()
