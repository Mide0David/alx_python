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
