#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-03-21
Purpose: Creating Synthetic DNA/RNA Sequences
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Get needed info for strand creation",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-t",
        "--seqtype",
        help="Sequence Type",
        metavar="str",
        choices=("dna", "rna"),
        type=str,
        default="dna",
    )

    parser.add_argument(
        "-n",
        "--numseqs",
        help="The number of sequences to be created",
        metavar="int",
        type=int,
        default=10,
    )

    parser.add_argument(
        "-m",
        "--minlen",
        help="The min length of a sequence",
        metavar="int",
        type=int,
        default=50,
    )

    parser.add_argument(
        "-x",
        "--maxlen",
        help="The max length of a sequence",
        metavar="int",
        type=int,
        default=75,
    )

    parser.add_argument(
        "-p",
        "--pctgc",
        help="The GC percentage of sequence",
        metavar="float",
        type=float,
        default=0.5,
    )

    parser.add_argument(
        "-s", "--seed", help="The random seed", metavar="int", type=int, default=None
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename readable file",
        metavar="str",
        type=str,
        default="out.fa",
    )

    args = parser.parse_args()

    if args.numseqs < 1:
        parser.error(f"--{args.numseqs} must be > 0")

    if args.minlen < 1:
        parser.error(f"--{args.minlen} must be > 0")

    if args.maxlen < args.minlen:
        parser.error(f"--{args.maxlen} must be >= min length")
    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args


# --------------------------------------------------


def create_pool(pctgc, max_len, seq_type):
    """Create the pool of bases"""

    t_or_u = "T" if seq_type == "dna" else "U"
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = "A" * num_at + "C" * num_gc + "G" * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return "".join(sorted(pool))


def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)
    out_fh = open(args.outfile, "wt")

    for i in range(args.numseqs):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = "".join(random.choices(pool, k=seq_len))
        out_fh.write(f">{i+1}\n{seq}\n")

    print(f'Done, wrote {i+1} {args.seqtype.upper()} sequences to "{args.outfile}".')

    out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
