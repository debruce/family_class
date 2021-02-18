#!/usr/local/bin/python3

import os
import sys
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here", type=int)
parser.add_argument("other", help="other string is set here", type=float)
parser.add_argument("--verbosity", help="increase output verbosity")
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")


args = parser.parse_args()

print(f"echo is set to {args.echo}")
print(f"other is set to {args.other}")
print(f"verbosity is set to {args.verbosity}")
print(f"verbose is set to {args.verbose}")

if args.verbosity:
    print(f"verbosity is assigned and has a value of {args.verbosity}")

# print(f"my pid is {os.getpid()}")
# print(f"my parent's pid is {os.getppid()}")

# for key,value in os.environ.items():
#     print(f"environment variable {key:20s} is set to {value}")

# print()

# for var in sys.argv:
#     print(f"argument variable {var}")
