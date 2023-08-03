"""
    This module contains a class for geometric shapes
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
