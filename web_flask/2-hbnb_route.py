#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def home0():
    return "Hello HBNB!"

@app.route('/hbnb')
def home():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
