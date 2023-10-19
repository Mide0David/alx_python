"""
    This module serves as a foundation for defining various shapes 
    and their properties and methods


"""

class BaseGeometryMeta(type):
    """
    This is a metaclass used to represent the class type in order to eliminate
    the inherited method init subclass

        Exclude attribute init subclass in dir()

    """

    def __dir__(cls):
        attributes = super().__dir__()

        return [
            attribute for attribute in attributes if attribute != "__init_subclass__"
        ]

class BaseGeometry(metaclass=BaseGeometryMeta):

    """
    Base class for geometry-related objects.

    This class serves as the foundation for defining various geometric shapes
    and their corresponding properties and methods.

    Methods:
        __dir__(self) -> None
            Exclude attribute init subclass in dir()
        area(self) -> None
            Placeholder method to calculate the area of the geometric shape.

            Raises:
                Exception: This method is not implemented in the base class and
                           should be overridden in subclasses to provide specific
                           implementations for calculating the area of a particular shape.
    """

     def __dir__(self):

        attributes = super().__dir__()

        return [
            attribute for attribute in attributes if attribute != "__init_subclass__"
        ]

    def area(self):
        raise Exception("area() is not implemented")
