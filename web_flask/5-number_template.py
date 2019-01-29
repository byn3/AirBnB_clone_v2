#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ root of site """
    return "Hello HBNB!"


@app.route("/hbnb")
def hello1():
    """ extension of hbnb """
    return "HBNB!"


@app.route("/c/<text>")
def hello2(text):
    """ extension of a text and c """
    gString = "C " + str(text)
    return gString.replace("_", " ")


@app.route("/python")
def hello3():
    """ python route """
    return "Python is cool"


@app.route("/python/<text>")
def hello3half(text):
    """ inception of python stuff """
    gString = "Python " + str(text)
    return gString.replace("_", " ")


@app.route("/number/<int:n>")
def hello4(n):
    """ comment describing what this basic flask thing does """
    gString = str(n) + " is a number"
    return gString


@app.route("/number_template/<int:n>")
def hello5(n):
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
