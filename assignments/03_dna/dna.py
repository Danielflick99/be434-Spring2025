#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-02-11
Purpose: Count Number of Occurrences of a Substring
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Tetranucleotide frequency",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("DNA", type=str, metavar="str", help="DNA sequence")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Count Number of Occurrences of a Substring"""

    args = get_args()
    strand = args.DNA

    print(strand.count("A"), strand.count("C"), strand.count("G"), strand.count("T"))


# --------------------------------------------------
if __name__ == "__main__":
    main()
