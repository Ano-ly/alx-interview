#!/usr/bin/env python3
"""N-queens problem"""
import sys


my_args = sys.argv
if len(my_args) > 2 or len(my_args) == 1:
    print("Usage: nqueens N")
    sys.exit(1)
N = my_args[1]
try:
    N = int(N)
except Exception:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)
