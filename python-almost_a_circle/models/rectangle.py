"""
This module defines the Rectangle class, a subclass of Base, for representing rectangles.
"""
from models.base import Base

class Rectangle(Base):
    """
    A class to represent rectangles with specified dimensions and position.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.

    Inherits from:
        Base: The base class for generating unique IDs.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance with given dimensions and position.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Default is 0.
            y (int, optional): The y-coordinate of the rectangle's position. Default is 0.
            id (int, optional): The unique ID of the rectangle. Default is None.

        Returns:
            None
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
