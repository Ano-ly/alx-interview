#!/usr/bin/python3
"""Minimum operations, Paste or Copy and Paste"""


def minOperations(n):
    """Minimum operations"""

    prev = 1
    ops = 0
    clipboard = 1
    reach = 1
    while reach != n:
        if prev == 1:
            ops += 2
            reach += prev
            prev = reach
        elif n % prev == 0:
            if clipboard >= 0.5 * prev or prev * 2 > n:
                ops += 1
                reach += clipboard
                prev = reach
            elif prev * 2 <= n:
                ops += 2
                clipboard = prev
                reach += prev
                prev = reach
        else:
            ops += 1
            reach += clipboard
            prev = reach
    return (ops)
