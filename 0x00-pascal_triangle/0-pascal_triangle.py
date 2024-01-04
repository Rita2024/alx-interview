#!/usr/bin/python3
""" Implementation of pascal triangle """

def pascal_triangle(n):
    """ Check if n is less than or equal to 0 """
    if n <= 0:
        return []

    """ Initialize Pascal's triangle with the first list """
    triangle = [[1]]

    """ Generate the rest of the triangle """
    for z in range(1, n):

        """ Get the rows in the triangle """
        rows = triangle[-1]

        """ Create the colums by adding the numbers above """
        columns = [1] + [rows[i - 1] + rows[i] for i in range(1, len(rows))] + [1]

        """ Add the new list to the triangle """
        triangle.append(columns)

    return triangle