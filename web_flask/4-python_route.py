#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
from werkzeug.utils import escape
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home0():
    return "Hello HBNB!"

@app.route('/hbnb')
def home():
    return "HBNB"

@app.route('/c/<text>')
def display_text(text):
    text = text.replace('_', ' ')
    return f'C {escape(text)}'

@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is cool"):
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
