# Almost a Circle - Object-Oriented Programming Project

This project involves building a Python package that includes classes for managing geometric shapes such as rectangles and squares. The project is divided into several parts, each of which focuses on adding new functionality to the classes. The base class `Base` is provided to manage the common attributes and methods for all classes.

## Getting Started

To start using the classes and testing the project, follow these instructions:

1. Clone the repository: `git clone https://github.com/your_username/alx_python.git`
2. Navigate to the `python-almost_a_circle` directory: `cd alx_python/python-almost_a_circle`

## Class Descriptions

### 0. Base Class

- Class Name: `Base`
- File: `models/base.py`

The `Base` class is the base class for all other classes in the project. It manages the `id` attribute for instances and provides a constructor to either assign a provided `id` or generate a new one.

#### Sample Test Case

```python
from models.base import Base

b1 = Base()
print(b1.id)  # Output: 1

b2 = Base()
print(b2.id)  # Output: 2

b3 = Base()
print(b3.id)  # Output: 3

b4 = Base(12)
print(b4.id)  # Output: 12

b5 = Base()
print(b5.id)  # Output: 4
```

### 1. First Rectangle

- Class Name: `Rectangle`
- Inherits from: `Base`
- File: `models/rectangle.py`

The `Rectangle` class represents a rectangle with width, height, and position attributes. This class inherits the `id` management from the `Base` class.

#### Sample Test Case

```python
from models.rectangle import Rectangle

r1 = Rectangle(10, 2)
print(r1.id)  # Output: 1

r2 = Rectangle(2, 10)
print(r2.id)  # Output: 2

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)  # Output: 12
```

### 2. Validate Attributes

- Class Name: `Rectangle`
- Inherits from: `Base`
- File: `models/rectangle.py`

This update adds validation to the setter methods and instantiation of the `Rectangle` class. It raises exceptions for invalid inputs.

#### Sample Test Case

```python
from models.rectangle import Rectangle

try:
    Rectangle(10, "2")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))  # Output: [TypeError] height must be an integer

try:
    r = Rectangle(10, 2)
    r.width = -10
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))  # Output: [ValueError] width must be > 0

# Add more test cases for other attributes
```

### 3. Area First

- Class Name: `Rectangle`
- Inherits from: `Base`
- File: `models/rectangle.py`

This update adds a method to calculate the area of the `Rectangle` instance.

#### Sample Test Case

```python
from models.rectangle import Rectangle

r1 = Rectangle(3, 2)
print(r1.area())  # Output: 6

r2 = Rectangle(2, 10)
print(r2.area())  # Output: 20

r3 = Rectangle(8, 7, 0, 0, 12)
print(r3.area())  # Output: 56
```

### 4. Display #0

- Class Name: `Rectangle`
- Inherits from: `Base`
- File: `models/rectangle.py`

This update adds a method to display the `Rectangle` instance using the character `#`.

#### Sample Test Case

```python
from models.rectangle import Rectangle

r1 = Rectangle(4, 6)
r1.display()
# Output:
# ####
# ####
# ####
# ####
# ####
# ####

print("---")

r2 = Rectangle(2, 2)
r2.display()
# Output:
# ##
# ##
```

### 5. `__str__`

- Class Name: `Rectangle`
- Inherits from: `Base`
- File: `models/rectangle.py`

This update overrides the `__str__` method to provide a custom string representation for the `Rectangle` instance.

#### Sample Test Case

```python
from models.rectangle import Rectangle

r1 = Rectangle(4, 6, 2, 1, 12)
print(r1)  # Output: [Rectangle] (12) 2/1 - 4/6

r2 = Rectangle(5, 5, 1)
print(r2)  # Output: [Rectangle] (1) 1/0 - 5/5
```

### 6. Display #1

- Class Name: `Rectangle`
- Inherits from: `Base`
- File: `models/rectangle.py`

This update improves the `display` method to take care of the `x` and `y` positions of the `Rectangle` instance.

#### Sample Test Case

```python
from models.rectangle import Rectangle

r1 = Rectangle(2, 3, 2, 2)
r1.display()
# Output:
#   ##
#   ##
#   ##

print("---")

r2 = Rectangle(3, 2, 1, 0)
r2.display()
# Output:
# ###
# ###
```

### 7. Update #0

- Class Name: `Rectangle`
- Inherits from: `Base`
- File: `models/rectangle.py`

This update adds a method to update the attributes of the `Rectangle` instance using no-keyword arguments.

#### Sample Test Case

```python
from models.rectangle import Rectangle

r1 = Rectangle(10, 10, 10, 10)
print(r1)  # Output: [Rectangle] (1) 10/10 - 10/10

r1.update(89)
print(r1)  # Output: [Rectangle] (89) 10/10 - 10/10

r1.update(89, 2)
print(r1)  # Output: [Rectangle] (89) 10/10 - 2/10

# Add more update test cases
```

### 8. Update #1

- Class Name: `Rectangle`
- Inherits from: `Base`
- File: `models/rectangle.py`

This update enhances the `update` method to accept key-worded arguments.

#### Sample Test Case

```python
from models.rectangle import Rectangle

r1 = Rectangle(10, 10, 10, 10)
print(r1)  # Output: [Rectangle] (1) 10/10 - 10/10

r1.update(height=1)
print(r1)  # Output: [Rectangle] (1) 10/10 - 10/1

r1.update(width=1, x=2)
print

(r1)  # Output: [Rectangle] (1) 2/10 - 1/1

# Add more update test cases
```

### 9. The Square

- Class Name: `Square`
- Inherits from: `Rectangle`
- File: `models/square.py`

The `Square` class inherits from the `Rectangle` class and represents a square shape with equal width and height.

#### Sample Test Case

```python
from models.square import Square

s1 = Square(5)
print(s1)  # Output: [Square] (1) 0/0 - 5

s2 = Square(2, 2)
print(s2)  # Output: [Square] (2) 2/0 - 2

s3 = Square(3, 1, 3)
print(s3)  # Output: [Square] (3) 1/3 - 3
```

### 10. Square Size

- Class Name: `Square`
- Inherits from: `Rectangle`
- File: `models/square.py`

This update adds getter and setter methods for the `size` attribute of the `Square` class.

#### Sample Test Case

```python
from models.square import Square

s1 = Square(5)
print(s1.size)  # Output: 5

s1.size = 10
print(s1.size)  # Output: 10

try:
    s1.size = "9"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))  # Output: [TypeError] width must be an integer
```

## Conclusion

This project demonstrates the principles of object-oriented programming in Python by building classes for managing geometric shapes. Each class inherits attributes and methods from the base class `Base` and introduces new functionality. The implementation of getters, setters, and custom methods provides a solid foundation for creating and manipulating instances of these shapes.

---
