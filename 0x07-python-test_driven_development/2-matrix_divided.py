#!/usr/bin/python3
"""
This module has matrix_divided implementation
"""


def matrix_divided(matrix, div):
    """Divides a matrix by a scalar integer, rounded to two decimal places"""
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)

    row_lengths = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        row_lengths.append(len(row))
        for n in row:
            if type(n) not in [int, float]:
                raise TypeError(error_msg)

    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif int(div) == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(
        lambda row: list(map(
            lambda x: round(x / div, 2), row)), matrix))
