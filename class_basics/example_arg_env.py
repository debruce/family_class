#!/usr/local/bin/python3

import os
import sys

for var in os.environ:
    print(f"environment variable {var:20s} is set to {os.environ[var]}")

print()

for var in sys.argv:
    print(f"argument variable {var}")