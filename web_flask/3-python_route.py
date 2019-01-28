#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/python")
def hello3():
    return "Python is cool"

@app.route("/python/<text>")
def hello3half(text):
    gString = "Python " + str(text)
    return gString.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
