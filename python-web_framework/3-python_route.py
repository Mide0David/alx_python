"""
Flask Documentation
Displays messages on three pages
"""

from flask import Flask

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
                                                            34,16         70%
        str: A message "C <text>" where <text> is the provided text.
    """
    return "C " + text.replace("_", " ")


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
        return "Python is cool"
    else:
        return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)
