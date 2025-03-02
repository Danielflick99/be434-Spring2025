#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-03-01
Purpose: Finding Sequence ID with Highest GC Content 
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Add Your Purpose",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "infile",
        help="A readable file",
        metavar="FILE",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    names = []
    dna_id = []
    sequence = ""

    for line in args.infile:
        line = line.strip()
        if line[0:1] == ">":
            if sequence:
                dna_id.append(sequence)
            names.append(line[1:])
            sequence = ""
        else:
            sequence += line[0:]

    if sequence:
        dna_id.append(sequence)

    # print(names)
    # print(dna_id)
    gc_conc = []
    high_gc = 0
    max_indx = 0
    j = -1

    for string in dna_id:
        j += 1
        conc = (string.count("G") + string.count("C")) / len(string) * 100
        gc_conc.append(conc)
        # print(gc_conc[j])
        if gc_conc[j] > high_gc:
            high_gc = gc_conc[j]
            max_indx = j

    names[max_indx] += " "
    print(f"{names[max_indx]}{high_gc:.06f}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
