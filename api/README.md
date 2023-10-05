# README for API Project

## Table of Contents
1. [Introduction](#introduction)
2. [Learning Objectives](#learning-objectives)
3. [Requirements](#requirements)
4. [Tasks](#tasks)
    - [Task 0: Gather Data from an API](#task-0-gather-data-from-an-api)
    - [Task 1: Export to CSV](#task-1-export-to-csv)
    - [Task 2: Export to JSON](#task-2-export-to-json)
    - [Task 3: Dictionary of List of Dictionaries](#task-3-dictionary-of-list-of-dictionaries)

---

## Introduction
This project is designed to help you understand various aspects of working with APIs, data formats (CSV and JSON), and Python coding standards (PEP 8). You will work on tasks that involve gathering data from an API, exporting data to CSV and JSON formats, and creating a dictionary of lists of dictionaries. This README provides an overview of the project and the tasks involved.

---

## Learning Objectives
By the end of this project, you are expected to be able to explain the following concepts without the need for external references:

### General
1. What is an API?
2. What is a REST API?
3. What are microservices?
4. What is the CSV format?
5. What is the JSON format?
6. Pythonic package and module name style.
7. Pythonic class name style.
8. Pythonic variable name style.
9. Pythonic function name style.
10. Pythonic constant name style.
11. Significance of CapWords or CamelCase in Python.

---

## Requirements
### General
- Recommended editors: Visual Studio Code.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All your files should end with a new line.
- Libraries imported in your Python files must be organized in alphabetical order.
- A README.md file, at the root of the project folder, is mandatory.
- Your code should follow the PEP 8 style.
- The length of your files will be tested using `wc`.
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- You must use `get` to access dictionary values by key (it won't throw an exception if the key doesn't exist in the dictionary).
- Your code should not be executed when imported (by using `if __name__ == "__main__":`).

---

## Tasks

### Task 0: Gather Data from an API
**Mandatory**
Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com), for a given employee ID, returns information about his/her TODO list progress.

#### Requirements:
- You must use the `urllib` or `requests` module.
- The script must accept an integer as a parameter, which is the employee ID.
- The script must display on the standard output the employee TODO list progress in this exact format:

```
First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
```

where:
- `EMPLOYEE_NAME` is the name of the employee.
- `NUMBER_OF_DONE_TASKS` is the number of completed tasks.
- `TOTAL_NUMBER_OF_TASKS` is the total number of tasks, which is the sum of completed and non-completed tasks.

Second and N next lines display the title of completed tasks:
```
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
```

**Example:**
```
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
sylvain@ubuntu$
```

### Task 1: Export to CSV
**Mandatory**
Using what you did in Task 0, extend your Python script to export data in the CSV format.

#### Requirements:
- Records all tasks that are owned by this employee.
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv

**Example:**
```
sylvain@ubuntu$ python3 1-export_to_CSV.py 2
sylvain@ubuntu$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"


"2","Antonette","True","et itaque necessitatibus maxime molestiae qui quas velit"
"2","Antonette","True","adipisci non ad dicta qui amet quaerat doloribus ea"
"2","Antonette","False","voluptas quo tenetur perspiciatis explicabo natus"
"2","Antonette","True","expedita numquam nihil blanditiis quisquam ut accusamus"
"2","Antonette","False","sunt dolorum fuga mollitia atque alias mollitia maiores rerum"
"2","Antonette","False","repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
"2","Antonette","False","ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae"
"2","Antonette","True","doloremque ex facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores"
sylvain@ubuntu$
```

### Task 2: Export to JSON
**Mandatory**
Using what you did in Task 0, extend your Python script to export data in the JSON format.

#### Requirements:
- Records all tasks that are owned by this employee.
- Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"} ]}
- File name must be: USER_ID.json

**Example:**
```
sylvain@ubuntu$ python3 2-export_to_JSON.py 2
sylvain@ubuntu$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": "False", "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": "True", "username": "Antonette"}, {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": "True", "username": "Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": "True", "username": "Antonette"}, {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": "False", "username": "Antonette"}, {"task": "expedita numquam nihil blanditiis quisquam ut accusamus", "completed": "True", "username": "Antonette"}, {"task": "sunt dolorum fuga mollitia atque alias mollitia maiores rerum", "completed": "False", "username": "Antonette"}, {"task": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque", "completed": "False", "username": "Antonette"}, {"task": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae", "completed": "False", "username": "Antonette"}, {"task": "doloremque ex facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores", "completed": "True", "username": "Antonette"}]}
sylvain@ubuntu$
```

### Task 3: Dictionary of List of Dictionaries
**Mandatory**
Using what you did in Task 0, extend your Python script to export data in the JSON format but in a specific format.

#### Requirements:
- Records all tasks that are owned by this employee.
- Format must be: { "USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}], "USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}] }

**Example:**
```
sylvain@ubuntu$ python3 3-dictionary_of_list_of_dictionaries.py 2
sylvain@ubuntu$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": "False", "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": "True", "username": "Antonette"}, {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": "True", "username": "Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": "True", "username": "Antonette"}, {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": "False", "username": "Antonette"}, {"task": "expedita numquam nihil blanditiis quisquam ut accusamus", "completed": "True", "username": "Antonette"}, {"task": "sunt dolorum fuga mollitia atque alias mollitia maiores rerum", "completed": "False", "username": "Antonette"}, {"task": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque", "completed": "False", "username": "Antonette"}, {"task": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae", "completed": "False", "username": "Antonette"}, {"task": "doloremque ex facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores", "completed": "True", "username": "Antonette"}]}
```
