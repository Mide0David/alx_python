# Python-Functions

This repository contains Python functions for various tasks. Each task has its own file within the `python-functions` directory.

## Task 0: Addition Function

The file for this task is `0-sum.py`. It contains a function called `add` that takes two integers as input and returns their sum.

**Prototype:**
```python
def add(a, b):
    # Returns the value of a + b
```

Example usage:
```python
print(add(1, 2))    # Output: 3
print(add(98, 0))   # Output: 98
print(add(100, -2)) # Output: 98
```

## Task 1: Power Function

The file for this task is `1-power.py`. It contains a function called `pow` that computes `a` raised to the power of `b` and returns the result.

**Prototype:**
```python
def pow(a, b):
    # Returns the value of a ^ b
```

Example usage:
```python
print(pow(2, 2))    # Output: 4
print(pow(98, 2))   # Output: 9604
print(pow(98, 0))   # Output: 1
print(pow(100, -2)) # Output: 0.0001
print(pow(-4, 5))   # Output: -1024
```

## Task 2: Temperature Converter Function

The file for this task is `2-temperature.py`. It contains a function called `convert_to_celsius` that takes a temperature in Fahrenheit as input and returns the temperature in Celsius.

**Prototype:**
```python
def convert_to_celsius(fahrenheit):
    # Returns the temperature in Celsius
```

Example usage:
```python
print(convert_to_celsius(100))    # Output: 10.0
print(convert_to_celsius(-40))    # Output: -17.77777777777778
print(convert_to_celsius(-459.67))# Output: -253.88888888888889
print(convert_to_celsius(32))     # Output: -5.0
```

## Task 3: String Manipulation Function

The file for this task is `3-string.py`. It contains a function called `reverse_string` that takes a string as input and returns the reverse of that string.

**Prototype:**
```python
def reverse_string(string):
    # Returns the reversed string
```

Example usage:
```python
print(reverse_string("Hello"))      # Output: "olleH"
print(reverse_string("Python"))     # Output: "nohtyP"
print(reverse_string("OpenAI"))     # Output: "IAepnO"
```

## Task 4: Fibonacci Sequence Function

The file for this task is `4-fibonacci.py`. It contains a function called `fibonacci_sequence` that takes a number `n` as input and returns a list of the first `n` Fibonacci numbers.

**Prototype:**
```python
def fibonacci_sequence(n):
    # Returns a list of the first n Fibonacci numbers
```

Example usage:
```python
print(fibonacci_sequence(1))  # Output: [0]
print(fibonacci_sequence(5))  # Output: [0, 1, 1, 2, 3]
print(fibonacci_sequence(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Task 5: Prime Number Function

The file for this task is `5-prime.py`. It contains a function called `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.

**Prototype:**
```python
def is_prime(number):
    # Returns True if the number is prime, and False otherwise
```

Example usage:
```python
print(is_prime(2))    # Output: True
print(is_prime(7))    # Output: True
print(is_prime(10))   # Output: False
print(is_prime(15))   # Output: False
print(is_prime(23))   # Output: True
```

## Task 6: Password Validation Function

The file for this task is `6-password.py`. It contains a function called `validate_password` that takes a password as input and performs various checks to validate it.

**Prototype:**
```python
def validate_password(password):
    # Returns True if the password passes all the checks, and False otherwise
```

Checks performed by `validate_password`:
- The password should be at least 8 characters long.
- The password should contain at least one uppercase letter, one lowercase letter, and one digit.
- The password should not contain spaces.

Example usage:
```python
print(validate_password("Password123"))      # Output: True
print(validate_password("short"))            # Output: False
print(validate_password("NoDigitsOrUpperCase"))  # Output: False
print(validate_password("Password with spaces")) # Output: False
```

**Note:** This is the basic structure of the tasks and their respective files. Please make sure to implement the functions as specified in the prototypes within the corresponding files.
