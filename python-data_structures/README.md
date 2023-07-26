# alx_python - Python Data Structures

This repository contains Python scripts that implement various tasks related to data structures. Below are descriptions of each script along with their respective usage and outputs:

## Task 0: Can you C me now?
File: 0-no_c.py

### Description:
This function `no_c(my_string)` removes all occurrences of the characters 'c' and 'C' from the input string `my_string`. The function returns the new string without these characters. It demonstrates manipulating strings without using the `str.replace()` method or importing any module.

### Usage and Output:
```python
from 0-no_c import no_c

print(no_c("Holberton School"))  # Output: Holberton Shool
print(no_c("Chicago"))  # Output: hiago
print(no_c("C is fun!"))  # Output:  is fun!
```

## Task 1: Lists of lists = Matrix
File: 1-print_matrix_integer.py

### Description:
This function `print_matrix_integer(matrix=[[]])` prints a matrix of integers. The input `matrix` is a list of lists containing integers, and the function displays the matrix in a user-friendly format using `str.format()` to print integers. It demonstrates printing and formatting lists of lists without importing any module.

### Usage and Output:
```python
from 1-print_matrix_integer import print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

print_matrix_integer()
# Output: (Empty output)
```

## Task 2: More returns!
File: 2-multiple_returns.py

### Description:
This function `multiple_returns(sentence)` takes a string `sentence` as input and returns a tuple containing the length of the string and its first character. If the sentence is empty, the first character in the tuple will be `None`. It demonstrates returning multiple values as a tuple without importing any module.

### Usage and Output:
```python
from 2-multiple_returns import multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
# Output: Length: 32 - First character: A
```

Please make sure to follow the instructions provided for each task and verify the outputs accordingly. If you have any questions or need further assistance, feel free to reach out. Happy coding!
