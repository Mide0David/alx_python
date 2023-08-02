"""
This module defines a square class for creating and printing squares 
"""
class Square:
    """This creates a square of any size

    Attributes:
        size(int): The size of the square's side

    """
    def __init__(self, size=None):
        self.__size = size
