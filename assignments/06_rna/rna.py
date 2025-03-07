#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-03-05
Purpose: Convert DNA to RNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Get DNA strand information",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        help="Input readable file(s)",
        nargs="+",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=None,
    )

    parser.add_argument(
        "-o",
        "--output",
        metavar="str",
        type=str,
        help="Output directory name",
        default="out",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    translate = {"A": "A", "T": "U", "C": "C", "G": "G"}
    rna = []

    if len(args.file) > 1:
        file_phrase = "files"
    else:
        file_phrase = "file"

    n_seq = 0
    for file in args.file:
        # print(f'Processing file {file.name}')
        out_name = file.name[7:]
        # print(out_name)
        out_file = args.output + "/" + out_name
        # print(out_file)
        # print(type(out_file))
        os.makedirs(args.output, exist_ok=True)
        out_fh = open(out_file, "wt")

        for line in file:
            n_seq += 1
            dna = line.strip()
            # print(dna)
            rna = "".join([translate[base] for base in dna])
            # print (rna)
            out_fh.write(rna + "\n")
        out_fh.close()
        if n_seq > 1:
            seq_phrase = "sequences"
        else:
            seq_phrase = "sequence"

    print(
        f'Done, wrote {n_seq} {seq_phrase} in {len(args.file)} {file_phrase} to directory "{args.output}".'
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
