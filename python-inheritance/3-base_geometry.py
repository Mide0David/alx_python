"""
This module checks if an object is an instance of a specified class
of its subclass

"""
class BaseGeometryMeta(type):
    def __new__(cls, name, bases, attrs):
        # Create a new class instance
        new_class = super(BaseGeometryMeta, cls).__new__(cls, name, bases, attrs)
        return new_class

class BaseGeometry(metaclass=BaseGeometryMeta):
    pass

