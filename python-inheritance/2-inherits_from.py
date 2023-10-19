"""
This module checks if an object is an instance of a specified class
of its subclass

"""
def inherits_from(obj, a_class):

    """
    Check if the given object is an instance of the specified class or its subclass.

    Args:
        obj: Any object - The object to be checked.
        a_class: type - The class to compare the object's type with.

    Returns:
        bool: True if the object is an instance of the specified class or its subclass;
              False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
