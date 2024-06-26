#!/usr/bin/python3
"""starts a Flask web application, C is fun!"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
     text = text.replace('_', ' ')
    return f'Python {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """A function that returns a number or not"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', number=n)
#def intNumber(n):
#return ("{:d} is a number".format(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
