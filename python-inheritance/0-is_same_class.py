"""
This module returns True if a instance 
is of a specified class
"""

def is_same_class(obj, a_class):
   """
   parameters:
      obj: Any object - The object to be checked
      a_class: type - The class to compare the object's type with

   Returns:
      bool: True if the object's type is the  same as the specified class, 
            false otherwise
   """
   return type(obj) is a_class
