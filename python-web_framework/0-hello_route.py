"""
    Flask Application Documentation
    displays messages
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

if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True)
