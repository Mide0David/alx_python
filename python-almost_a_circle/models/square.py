"""
This module defines the Square class, a subclass of Rectangle, for representing squares.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    A class to represent squares with specified size and position.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.

    Inherits from:
        Rectangle: The base class for representing rectangles.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Initialize a Square instance with given size and position.
        __str__(): Return a string representation of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance with given size and position.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position. Default is 0.
            y (int, optional): The y-coordinate of the square's position. Default is 0.
            id (int, optional): The unique ID of the square. Default is None.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value to set.

        Returns:
            None
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The formatted string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
