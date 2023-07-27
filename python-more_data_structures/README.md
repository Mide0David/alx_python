# Repository Name: alx_python
## Directory: python-more_data_structures

## Task 0: Squared simple

### Description
The function `square_matrix_simple(matrix)` takes a 2-dimensional array `matrix` as input and computes the square value of all integers in the matrix. It returns a new matrix with the same size as the input matrix, where each value is the square of the corresponding value in the input matrix. The initial matrix is not modified by the function. The function should not import any modules and is allowed to use regular loops, map, etc.

### Prototype
```python
def square_matrix_simple(matrix=[]):
```

### Input
- `matrix`: A 2-dimensional array (list of lists) containing integers.

### Output
- Returns a new 2-dimensional array (list of lists) with the same size as the input matrix.
- Each value in the output matrix is the square of the corresponding value in the input matrix.

### Example
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
# Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

print(matrix)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Task 1: Present in both

### Description
The function `common_elements(set_1, set_2)` takes two sets as input and returns a new set containing the common elements that are present in both sets. The function does not import any modules.

### Prototype
```python
def common_elements(set_1, set_2):
```

### Input
- `set_1`: A set containing elements (e.g., strings, numbers, etc.).
- `set_2`: Another set containing elements (e.g., strings, numbers, etc.).

### Output
- Returns a new set containing the common elements that are present in both `set_1` and `set_2`.

### Example
```python
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }

c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
# Output: ['C']
```

## Task 2: Update dictionary

### Description
The function `update_dictionary(a_dictionary, key, value)` takes a dictionary `a_dictionary`, a key `key`, and a value `value` as input. It replaces or adds the key-value pair in the dictionary as follows:
- If the key already exists in the dictionary, its corresponding value is replaced with the new value.
- If the key does not exist in the dictionary, a new key-value pair is added to the dictionary.

### Prototype
```python
def update_dictionary(a_dictionary, key, value):
```

### Input
- `a_dictionary`: A dictionary (key-value pairs) where the keys are strings and the values can be of any type.
- `key`: A string representing the key to be replaced or added.
- `value`: The value to be associated with the given key.

### Output
- Returns the updated dictionary.

### Example
```python
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
# Output:
# language: Python
# number: 89
# track: Low level

print_sorted_dictionary(a_dictionary)
# Output:
# language: Python
# number: 89
# track: Low level

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
# Output:
# city: San Francisco
# language: Python
# number: 89
# track: Low level

print_sorted_dictionary(a_dictionary)
# Output:
# city: San Francisco
# language: Python
# number: 89
# track: Low level
```

## Task 3: Best score

### Description
The function `best_score(a_dictionary)` takes a dictionary `a_dictionary` as input. The dictionary contains students as keys and their corresponding scores (which are integers) as values. The function returns the key (student's name) with the highest integer value (score). If no scores are found, the function returns `None`. It is assumed that all students have different scores.

### Prototype
```python
def best_score(a_dictionary):
```

### Input
- `a_dictionary`: A dictionary (key-value pairs) where the keys are strings representing student names and the values are integers representing their scores.

### Output
- Returns the student's name (key) with the highest integer value (score) in the dictionary.
- If no scores are found, returns `None`.

### Example
```python
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))
# Output: Best score: Molly

best_key = best_score(None)
print("Best score: {}".format(best_key))
# Output: Best score: None
```

## Task 4: Multiply by using map

### Description
The function `multiply_list_map(my_list, number)` takes a list `my_list` and a number `number` as input. It returns a new list with all values in `my_list` multiplied by the given `number`. The function should not modify the original list and should use the `map` function for the multiplication.

### Prototype
```python
def multiply_list_map(my_list=[], number=0):
```

### Input
- `my_list`: A list of integers.
- `number`: An integer representing the number to be used for multiplication.

### Output
- Returns a new list with the same length as `my_list`, where each value is the result of multiplying the corresponding value in `my_list` by `number`.

### Example
```python
my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
# Output: [4, 8, 12, 16, 24]

print(my_list)
# Output: [1, 2, 3, 4, 6]
```
