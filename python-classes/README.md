Sure, I can help you with the "README.md" file for your Python project on Classes and Objects. Below is a template you can use as a starting point:

---

# Python - Classes and Objects

## Background Context

Object-Oriented Programming (OOP) is an essential concept in Python programming. In this project, we will explore the fundamentals of OOP and how to create classes and objects. It's crucial to read and understand all the provided resources before proceeding with the tasks. Experimentation and hands-on practice are key to grasping the concepts of OOP effectively.

## Resources

Make sure to read or watch the following resources in the specified order:

1. [Object-Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph "Inheritance" excluded. Skip class attributes, class method, and static method for now.)
2. [Object-Oriented Programming](https://python-textbok.readthedocs.io/en/1.0/Classes.html) (Read: General Introduction, First-class Everything, A Minimal Class in Python, Attributes, Methods, The __init__ Method, "Data Abstraction, Data Encapsulation, and Information Hiding," "Public, Protected, and Private Attributes")
3. [Properties vs. Getters and Setters](https://www.python-course.eu/python3_properties.php)
4. [Learn to Program 9: Object-Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
5. [Python Classes and Objects](https://www.geeksforgeeks.org/python-classes-and-objects/)
6. [Object-Oriented Programming](https://www.programiz.com/python-programming/object-oriented-programming)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without relying on external resources:

1. The awesomeness of Python programming
2. What is Object-Oriented Programming (OOP) and its significance
3. The concept of "first-class everything" in Python
4. Definition of a class and its role in OOP
5. The difference between a class, object, and instance
6. Understanding attributes and their types (public, protected, and private)
7. The purpose of the `self` keyword in Python classes
8. What is a method and how to define and use them in a class
9. The special `__init__` method and its usage as a constructor
10. Data Abstraction, Data Encapsulation, and Information Hiding in OOP
11. The concept of a property and its distinction from attributes in Python
12. Writing Pythonic getters and setters for classes
13. How to dynamically create new attributes for class instances
14. Attribute binding to objects and classes
15. Exploring the `__dict__` of a class and/or instance and its contents
16. How Python finds attributes of an object or class
17. Usage of the `getattr` function to access attributes

## Requirements

### General

- Recommended text editor: Visual Studio Code
- All files should be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- A `README.md` file, at the root of the project folder, is mandatory
- Code should follow the PEP 8 style (version 1.7)
- The length of your files will be tested using `wc`
- All modules, classes, and functions should have proper documentation (docstrings)
- Documentation should be informative sentences explaining the purpose and functionality of each module, class, or method

### Quiz Questions

You will find quiz questions along the way to reinforce your understanding. Make sure to answer them correctly to validate your comprehension of the topics covered.

## Tasks

### Task 0: Square with Size

Write a class `Square` that defines a square by:
- Having a private instance attribute `size`.
- Allowing instantiation with a specified size (no type/value verification).
- No importing of any modules.

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ python3 0-main.py
<class '0-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/$ 
```

### Task 1: Size Validation

Modify the `Square` class from Task 0 to include size validation:
- The `size` attribute must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer".
- If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ python3 1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
<class '1-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/$ 
```
### Task 2: Area of a Square

Extend the `Square` class from Task 1 to include a public instance method `area` that returns the current square's area.
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/$ python3 2-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/$ 
```
### Task 3: Access and Update Private Attribute

Enhance the `Square` class from Task 2 to include:
- A property `size` to retrieve the `size` attribute.
- A property setter `size` to set the `size` attribute with type and value validation.
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ python3 3-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/$ 
```
### Task 4: Printing a Square

Improve the `Square` class from Task 3 to include a public instance method `my_print` that prints the square using the character '#':
- If the `size` is equal to 0, print an empty line.
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/$ python3 4-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/$ 
```
