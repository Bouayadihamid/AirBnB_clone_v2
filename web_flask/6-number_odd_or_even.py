#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pytext(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemplate(n):
    if isinstance(n, int):
        return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numberEvenOdd(n):
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template("6-number_odd_or_even.html",
                                   number=n, info="even")
        else:
            return render_template("6-number_odd_or_even.html",
                                   number=n, info="odd")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
