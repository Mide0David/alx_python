"""
    This module checks if a given object is an instance of
    a specified class or any of it subclasses

"""
def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of the specified class or 
    any of its subclasses.

    Parameters:
        obj: Any object - The object to be checked.
        a_class: type - The class to compare the object's type with.

    Returns:
        bool: True if the object is an instance of the specified class or any
                of its subclasses;False otherwise.
    """
    return isinstance(obj, a_class)
