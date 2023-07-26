#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """print a matrix element"""
    for index in matrix:
        for element in index:
            if element == index[-1]:
                print("{:d}".format(element), end="")
            else:
                print("{:d} ".format(element), end="")
        print()
