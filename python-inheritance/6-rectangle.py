"""
    This module define various 
    geometric shapes
"""
class BaseGeometry:
    """
    Base class for geometry-related objects.

    This class serves as the foundation for defining various geometric shapes
    and their corresponding properties and methods.

    Methods:
        area(self) -> None:
            Placeholder method to calculate the area of the geometric shape.

            Raises:
                Exception: This method is not implemented in the base class and
                           should be overridden in subclasses to provide specific
                           implementations for calculating the area of a particular shape.

        integer_validator(self, name: str, value: int) -> None:
            Validates an integer value for a given property.

            This method checks if the provided value is an integer and greater than 0.

            Parameters:
                name (str): The name of the property being validated.
                value (int): The value to be validated.

            Raises:
                TypeError: If the provided value is not an integer.
                ValueError: If the provided value is not greater than 0.

            Returns:
                None
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
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
