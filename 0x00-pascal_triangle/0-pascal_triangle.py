#!/usr/bin/python3
"""Pascal's triangle function"""


def pascal_triangle(n):
    """Function that returns Pascal's Triangle"""
    triangle = []
    if n <= 0:
        return ([])
    i = 0
    while i < n:
        row1 = []
        row2 = []
        if i == 0:
            row1.append(1)
            triangle.append(row1)
        elif i == 1:
            row1.append(1)
            row1.append(1)
            triangle.append(row1)
        else:
            prev = triangle[i-1]
            start = 0
            end = len(prev) - 1
            mid = len(prev) // 2
            row1.append(1)
            while (start <= mid) and (len(prev) - 1) != start:
                row1.append(prev[start] + prev[start + 1])
                start += 1
            row2.append(1)
            while True:
                end -= 1
                if end <= mid:
                    break
                row2.append(prev[end] + prev[end + 1])
            row2.reverse()
            row1.extend(row2)
            triangle.append(row1)
        i += 1
    return (triangle)
