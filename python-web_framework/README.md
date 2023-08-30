# Flask Web Framework Project

![Project Badge](BadgeURL) <!-- Replace BadgeURL with the actual badge URL -->

## Table of Contents

- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
  - [Hello Flask!](#hello-flask)
  - [HBNB](#hbnb)
  - [C is fun!](#c-is-fun)
  - [Python is cool!](#python-is-cool)
  - [Is it a number?](#is-it-a-number)
  - [Number template](#number-template)
  - [Odd or even?](#odd-or-even)
- [Contributing](#contributing)
- [License](#license)

## Description

This repository contains a collection of Flask web application tasks implemented as part of a learning project. Each task focuses on various aspects of building web applications using the Flask framework in Python.

## Learning Objectives

Upon completing this project, you will be able to explain:

- What a web framework is and how Flask fits into the web development ecosystem.
- How to define routes and handle variables in Flask.
- The concept of templates and dynamic template creation.
- How to display data from a MySQL database in HTML.
- Guidelines for adhering to PEP 8 style in Python scripts.
- Creating W3C-compliant HTML/CSS files for web development.

## Requirements

### Python Scripts

- Python 3.4.3
- PEP 8 style (version 1.7)
- Documentation for modules, classes, and functions

### HTML/CSS Files

- W3C-compliant HTML/CSS
- README.md file at the root of the project folder
- Styles should be organized in the 'styles' folder
- Images should be stored in the 'images' folder

## Installation

To set up and run the Flask web application, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Install Flask: `pip3 install Flask`
3. Navigate to the project directory: `cd your-repo`

## Usage

1. Each task is implemented in a separate Python file.
2. To run a specific task, use the command: `python3 filename.py`
3. Access the web application in your browser at: `http://0.0.0.0:5000/`

## Tasks

### Hello Flask!

```python
# 0-hello_route.py
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### HBNB

```python
# 1-hbnb_route.py
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### C is fun!

```python
# 2-c_route.py
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return "C " + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Python is cool!

```python
# 3-python_route.py
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return "Python " + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Is it a number?

```python
# 4-number_route.py
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Number template

```python
# 5-number_template.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Odd or even?

```python
# 6-number_odd_or_even.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return "C "

 + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
