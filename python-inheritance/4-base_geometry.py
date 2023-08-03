"""
    This module serves as a foundation for defining various shapes 
    and their properties and methods


"""
class BaseGeometry:
    """
    Base class for geometry-related objects.

    This class serves as the foundation for defining various geometric shapes
    and their corresponding properties and methods.

    Methods:
        area(self) -> None
            Placeholder method to calculate the area of the geometric shape.

            Raises:
                Exception: This method is not implemented in the base class and
                           should be overridden in subclasses to provide specific
                           implementations for calculating the area of a particular shape.
    """
    def area(self):
        raise Exception("area() is not implemented")
