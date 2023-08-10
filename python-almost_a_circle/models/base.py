"""
This module defines the Base class, a base class for generating unique IDs for objects.
"""
class Base:
    """
    A base class for generating unique IDs for objects.

    Attributes:
        __nb_objects (int): A counter to keep track of the number of created objects.

    Methods:
        __init__(self, id=None): Initialize a Base instance with a unique ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance with a unique ID.

        Args:
            id (int, optional): The ID to assign to the instance. If not provided, a new unique ID will be generated.

        Returns:
            None
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
