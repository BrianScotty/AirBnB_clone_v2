#!/usr/bin/python3
"""
Module: 0-hello_route
Flask web application that responds to /
"""
from flask import Flask

def create_app():
    """Create a Flask app."""
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """Display 'Hello HBNB!'"""
        return 'Hello HBNB!'

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
