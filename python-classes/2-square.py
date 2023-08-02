"""
This module defines a Square class for creating and printing squares
"""

class Square:
    """
    A class representing a square

    Attributes;
        size(int): The size of the square's side
    """
    def __init__(self, size=0):
        """
        Initialize a new square instance

        Parameters:
            size(int): The size of the square's side. Default is 0
        Raises:
            TypeError: if the given value is not an integer
            ValueError: if the given value is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        Calculate the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
