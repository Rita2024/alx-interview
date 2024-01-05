#!/usr/bin/python3
""" Implementation of pascal triangle """


def pascal_triangle(n):
    """ Check if n is less than or equal to 0 """
    if n <= 0:
        return []

    """ Initialize Pascal's triangle with the first list """
    triangle = [[1]]

    for z in range(1, n):
        nlist = [1]
        for x in range(1, z):
            nlist.append(triangle[z - 1][x - 1] + triangle[z - 1][x])
        nlist.append(1)
        triangle.append(nlist)

    return triangle
