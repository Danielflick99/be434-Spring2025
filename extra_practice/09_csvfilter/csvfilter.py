#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-04-04
Purpose: Filter CSV file
"""

import argparse
import csv
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Filter CSV File",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        required=True,
        help="A required argument that is a readable file",
    )

    parser.add_argument(
        "-v",
        "--value",
        metavar="str",
        type=str,
        required=True,
        help="A required value to match against each record",
    )

    parser.add_argument(
        "-c",
        "--col",
        help="An optional col name to search for a given value",
        metavar="str",
        type=str,
    )

    parser.add_argument(
        "-d",
        "--delimiter",
        help="An optional delimiter to parse the file",
        metavar="delim",
        type=str,
        default=",",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="An optional output file name",
        metavar="str",
        default="out.csv",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh = args.file

    reader = csv.DictReader(fh, delimiter=args.delimiter)
    headers = reader.fieldnames

    if args.col:
        if args.col not in headers:
            print(f'--col "{args.col}" not a valid column!')
            sys.exit(1)

    out_fh = open(args.outfile, "wt")

    writer = csv.DictWriter(out_fh, fieldnames=headers)
    writer.writeheader()

    num_written = 0

    for rec in reader:
        text = rec.get(args.col) if args.col else ",".join(rec.values())
        if re.search(args.value, text, re.IGNORECASE):
            num_written += 1
            writer.writerow(rec)

    print(f'Done, wrote {num_written} to "{args.outfile}".')
    out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
