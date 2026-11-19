#!/usr/bin/python3
"""Module that defines the function matrix_divided.

The function divides all the elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list): a list of lists of integers or floats.
        div (int, float): the divisor.
    Raises:
        TypeError: if matrix is not a matrix of numbers, if the rows
            have different sizes, or if div is not a number.
        ZeroDivisionError: if div is 0.
    Returns:
        A new matrix.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) and len(row) > 0
                    for row in matrix)):
        raise TypeError(msg)
    for row in matrix:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(msg)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
