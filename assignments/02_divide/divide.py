#!/usr/bin/env python3
"""
Author : Daniel Flick <danielflick@arizona.edu>
Date   : 2025-02-06
Purpose: Divide two numbers
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Divide two numbers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("INT1", type=int, metavar="int", 
                        help="The first integer")
    parser.add_argument("INT2", type=int, 
                        metavar="int", 
                        help="The second integer")
    return parser.parse_args()


# ---------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    int1 = args.INT1
    int2 = args.INT2

    if int2 == 0:
        sys.exit("usage: Cannot divide by zero, dum-dum!")
    else:
        print(f"{int1} / {int2} = {int1//int2}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
