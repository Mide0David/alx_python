"""
This module defines a Square class for creating and printing squares
"""

class Square:
    """A class representing a square

    Attributes:
        size(int): Thw size of the square's side
    """

    def __init__(self, size=0):
        """
        Initialize a new square instance

        Parameters:
            size(int): The size of the square'side. Default is 0
        """
        self.size = size


    @property
    def size(self):
        """
        Get the size of the square's side

        Returns:
            int: The size of the square"s side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square side

        Parameters:
            value (int): The size of the square's side

        Raises:
            TypeError: if the given value is not an integer
            ValueError: if the given value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """
        Calculate the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prnt the square using '#' characters

        If the size is 0, it will print an empty line

        Example:
            If the size is 3 it will print:
            ###
            ###
            ###
        """

        if self.__size == 0:
            print("")
        else:
            for column in range(0, self.__size):
                for row in range(0, self.__size):
                    print("#", end="")
                print()
