#!/usr/bin/python3
"""Island Perimeter ccalculation"""


def calc_sides(grid, r_idx, c_idx, len_rows, len_cols):
    """Support function"""
    sides = 0
    if c_idx != len_cols - 1:
        if grid[r_idx][c_idx + 1] == 0:
            sides += 1
    else:
        sides += 1
    if c_idx != 0:
        if grid[r_idx][c_idx - 1] == 0:
            sides += 1
    else:
        sides += 1
    if r_idx != 0:
        if grid[r_idx - 1][c_idx] == 0:
            sides += 1
    else:
        sides += 1
    if r_idx != len_rows - 1:
        if grid[r_idx + 1][c_idx] == 0:
            sides += 1
    else:
        sides += 1
    return (sides)


def island_perimeter(grid):
    """Island perimeter function"""
    if len(grid) == 0:
        return (0)
    len_rows = len(grid)
    len_cols = len(grid[0])
    i = 0
    per = 0
    while i < len_rows:
        j = 0
        while j < len_cols:
            if grid[i][j] == 1:
                sides = calc_sides(grid, i, j, len_rows, len_cols)
                per += sides
            j += 1
        i += 1
    return (per)
