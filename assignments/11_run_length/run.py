#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-04-19
Purpose: Calculate Run Length Encoding
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Run-length encoding/data compression",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("strand", metavar="str", help="A DNA strand or File Name")

    return parser.parse_args()


# --------------------------------------------------


def run_length(dna):

    convert = []
    reps = 1
    prior = ""
    for char in dna:

        if not (char == prior):
            if reps == 1:
                convert.append(char)

                prior = char
            else:
                convert.append(str(reps))
                convert.append(char)
                prior = char
                reps = 1
        else:
            reps += 1

    if reps == 1:
        result = "".join(convert)
    else:
        convert.append(str(reps))
        result = "".join(convert)

    return result


def main():
    """Run-length encoding"""

    args = get_args()

    if os.path.isfile(args.strand):
        fh = open(args.strand, "rt")
        for line in fh:
            dna = line.strip()
            print(run_length(dna))
        fh.close
    else:
        dna = args.strand
        print(run_length(dna))


# --------------------------------------------------
if __name__ == "__main__":
    main()
