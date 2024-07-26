#!/usr/bin/python3
"""makeChange function"""


def makechange(coins, total):
    """Get minimum number of coins required for a total"""
    if total <= 0:
        return (0)
    arr = [total + 1 for i in range(0, total + 1)]
    arr[0] = 0
    i = 0
    while i < len(arr):
        for c in coins:
            if c <= i:
                sub = i - c
                arr[i] = min(arr[i], arr[sub] + 1)
            else:
                continue
        i += 1
    if arr[total] == total + 1:
        return (-1)
    else:
        return (arr[total])
