#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-04-25
Purpose: Find Patterns in Files
"""

import argparse
import re
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Search pattern in file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("pattern", metavar="str", help="Search pattern")

    parser.add_argument(
        "infile", help="A readable file", metavar="FILE", nargs="+", type=str
    )

    parser.add_argument(
        "-i",
        "--insensitive",
        help="Case insensitive search (default: False)",
        action="store_true",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        metavar="str",
        type=str,
        help="Output file name",
        default=sys.stdout,
    )

    args = parser.parse_args()

    for filename in args.infile:
        if not (os.path.isfile(filename)):
            parser.error(f"No such file or directory: '{filename}'")
    return args


# --------------------------------------------------
def main():
    """Find pattern in strings in files"""

    args = get_args()

    pattern = args.pattern

    match = []

    for filename in args.infile:
        for line in open(filename):
            +
            if (
                re.search(pattern, line, re.IGNORECASE)
                if args.insensitive
                else re.search(pattern, line)
            ):

                line = line.strip()
                if len(args.infile) > 1:
                    match.append(f"{filename}:{line}")
                else:
                    match.append(line)

    if args.outfile == sys.stdout:
        print("\n".join(match))
    else:
        out_fh = open(args.outfile, "wt")
        out_fh.write("\n".join(match) + "\n")


# --------------------------------------------------
if __name__ == "__main__":
    main()
