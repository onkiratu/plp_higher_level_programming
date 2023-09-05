#!/usr/bin/python3
"""
This module holds a function that divides elements of a matrix
Function: matrix_divided(matrix, div)

"""


def matrix_divided(matrix, div):
    """
    This function divides elements of a matrix

    Args:
    matrix: the matrix that contains the elements
    div: dividing matrix
    """
    newList = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for index in matrix:
        for element in index:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    for index in matrix:
        if len(index) > len(matrix[0]) or len(index) < len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    for row in matrix:
        new_row = []
        for number in row:
            new_row.append(round(number/div, 2))
        newList.append(new_row)

    return newList
