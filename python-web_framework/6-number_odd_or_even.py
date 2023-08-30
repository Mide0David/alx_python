"""
Flask Documentation
Displays messages on multiple pages with dynamic content and template rendering
"""

from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """
    Route handler for the root URL ("/").
    
    Returns:
        str: The response message "Hello HBNB!".
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbn():
    """
    Route handler for the "/hbnb" URL.
    
    Returns:
        str: The response message "HBNB".
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def two(text):
    """
    Route handler for the "/c/<text>" URL.
    
    Parameters:
        text (str): The text provided in the URL.
    
    Returns:
        str: A message "C <text>" where <text> is the provided text.
    """
    return f"C {text}"

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def three(text=None):
    """
    Route handler for the "/python" and "/python/<text>" URLs.
    
    Parameters:
        text (str, optional): The text provided in the URL. Defaults to None.
    
    Returns:
        str: A message based on the provided text or a default message if no text is provided.
    """
    if text is None or text == "":
        return "python is cool"
    else:
        return f"python {text}"

@app.route("/number/<int:n>", strict_slashes=False)
def four(n):
    """
    Route handler for the "/number/<int:n>" URL.
    
    Parameters:
        n (int): The integer provided in the URL.
    
    Returns:
        str: A message indicating that the provided value is a number.
    """
    return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def five(n):
    """
    Route handler for the "/number_template/<int:n>" URL.
    
    Parameters:
        n (int): The integer provided in the URL.
    
    Returns:
        HTML: Renders the "5-number.html" template with the provided number.
    """
    return render_template("5-number.html", num=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def six(n):
    """
    Route handler for the "/number_odd_or_even/<int:n>" URL.
    
    Parameters:
        n (int): The integer provided in the URL.
    
    Returns:
        HTML: Renders the "6-number_odd_or_even.html" template to determine if the provided number is odd or even.
    """
    return render_template("6-number_odd_or_even.html", num=n)

if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)