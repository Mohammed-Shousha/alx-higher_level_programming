#!/usr/bin/python3
"""Contains pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the triangle."""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        last_row = triangles[-1]
        new_row = [1]

        for i in range(len(last_row) - 1):
            new_element = last_row[i] + last_row[i + 1]
            new_row.append(new_element)

        new_row.append(1)
        triangles.append(new_row)

    return triangles
