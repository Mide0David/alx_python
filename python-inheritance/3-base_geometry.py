"""
        # Exclude the attribute __init_subclass__
Custom metaclass to exclude __init_subclass__
"""
class BaseGeometryMeta(type):
        """
    This metaclass is used to remove the __init_subclass__ method from class attributes.
    """
    def __dir__(cls):
        """
        Exclude the '__init_subclass__' attribute from class attributes when using dir().
        """
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != "__init_subclass__"]

# BaseGeometry class with a custom metaclass
class BaseGeometry(metaclass=BaseGeometryMeta):
        """
    The BaseGeometry class serves as a base class with the '__init_subclass__' method excluded.
    """
    def __dir__(self):
                """
        Exclude '__init_subclass__' attribute from instance attributes when using dir().
        """
        # Exclude the attribute __init_subclass__
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != "__init_subclass__"]
