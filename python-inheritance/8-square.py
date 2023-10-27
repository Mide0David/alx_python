"""
    this is a module class about different 
    geometric shapes
"""

class BaseGeometry:
    """
    Base class for geometric shapes.

    This class provides a foundation for creating geometric shapes and defining their properties.
    It contains a method 'area' that raises an exception as it needs to be implemented by subclasses.
    Additionally, the 'integer_validator' method is provided to validate integer values for shape properties.

    Methods:
    1. area(): This method raises an Exception as it needs to be implemented by subclasses to calculate the area.
    2. integer_validator(name, value): Validates that the given 'value' is an integer and greater than 0.

    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        This method is not implemented in the base class and must be overridden in subclasses.

        Raises:
            Exception: As this method is not implemented, calling it will raise an Exception.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the integer value for a shape property.

        Args:
            name (str): The name of the property being validated.
            value (int): The value of the property to be validated.

        Raises:
            TypeError: If the 'value' is not an integer.
            ValueError: If the 'value' is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class representing a rectangle shape.

    This class inherits from BaseGeometry and provides an implementation for the area method.
    It also has an __init__ method to initialize the rectangle with width and height properties.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        area(): Calculate the area of the rectangle (width * height).
        __str__(): Return a string representation of the rectangle in the format "[Rectangle] width/height".

    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """
        self.__width = width
        self.integer_validator("width", self.__width)

        self.__height = height
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle in the format "[Rectangle] width/height".

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
class Square(Rectangle):
    """
    A class representing a square, a special case of a rectangle.

    Attributes:
        Inherits attributes from the Rectangle class.

    Methods:
        Inherits methods from the Rectangle class.
    """

    def __init__(self, size):
        """
        Initialize a square with the given size.

        Args:
            size (int): The size of the square (both width and height).

        """
        super().__init__(size, size)
    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square in the format "[Square] size/size".

        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
