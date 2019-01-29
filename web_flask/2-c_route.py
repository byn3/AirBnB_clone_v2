#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
