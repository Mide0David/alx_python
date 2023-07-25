# alx_python - Python Import Modules

This repository contains Python scripts that demonstrate various tasks related to importing modules and handling exceptions. Below are descriptions of each script along with their respective usage and outputs:

## Task 0: Import a simple function from a simple file
File: 0-add.py

### Description:
This script imports the function `add(a, b)` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`. It demonstrates the usage of the `print` function with string formatting to display integers.

### Usage and Output:
```bash
$ ./0-add.py
1 + 2 = 3
```

## Task 1: How to make a script dynamic!
File: 1-args.py

### Description:
This program prints the number of and the list of its arguments. It uses the `argv` variable to retrieve command-line arguments and displays the number of arguments, their positions, and their values.

### Usage and Output:
```bash
$ ./1-args.py
0 arguments.

$ ./1-args.py Hello
1 argument:
1: Hello

$ ./1-args.py Hello Holberton School 98 Battery street
6 arguments:
1: Hello
2: Holberton
3: School
4: 98
5: Battery
6: street
```

## Task 2: Everything can be imported
File: 2-variable_load.py

### Description:
This script imports the variable `a` from the file `variable_load_2.py` and prints its value. It demonstrates importing variables from other Python files.

### Usage and Output:
```bash
$ ./2-variable_load.py
98
```

## Task 3: Integers division with debug
File: 3-safe_print_division.py

### Description:
This script defines the function `safe_print_division(a, b)` that divides two integers and prints the result. It uses `try`, `except`, and `finally` blocks to handle division by zero and prints the result using string formatting.

### Usage and Output:
```bash
$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
```

## Task 4: Raise exception
File: 4-raise_exception.py

### Description:
This script defines the function `raise_exception()` that raises a type exception using Python's built-in `raise` statement.

### Usage and Output:
```bash
$ ./4-main.py
Exception raised
```

## Task 5: Raise a message
File: 5-raise_exception_msg.py

### Description:
This script defines the function `raise_exception_msg(message="")` that raises a name exception with a given message using the `raise` statement.

### Usage and Output:
```bash
$ ./5-main.py
C is fun
```

Please make sure to follow the instructions provided for each task and verify the outputs accordingly. If you have any questions or need further assistance, feel free to reach out. Happy coding!
