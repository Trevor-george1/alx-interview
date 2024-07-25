#!/usr/bin/python3
"""
function that returns a list of lists of intergers
representing the pascal triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of intergers
    representing the pascal triangle
    """
    if n <= 0:
        return []
    else:
        triangle = [[1]]

        for i in range(1, n):
            triangle.append([1])

            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle[i].append(1)
        return triangle
