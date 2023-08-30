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
        str: A message "C <text>" where <text> is the provided text.
    """
        return "C" + text.replace("_", " ")

if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)
