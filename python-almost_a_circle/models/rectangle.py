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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not valid (e.g., <= 0).

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not valid (e.g., <= 0).

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The x offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x offset of the rectangle.

        Args:
            value (int): The x value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not valid (e.g., < 0).

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """int: The y offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y offset of the rectangle.

        Args:
            value (int): The y value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not valid (e.g., < 0).

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle using '#' characters.

        Returns:
            None
        """
        for vertical in range(0, self.__y):
            print()
        for column in range(0, self.__height):
            for horizontal in range(0, self.__x):
                print(" ", end="")
            for row in range(0, self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle using either positional arguments or keyword arguments.

        Args:
            *args: Positional arguments (id, width, height, x, y).
            **kwargs: Keyword arguments for attributes.

        Returns:
            None
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The formatted string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
