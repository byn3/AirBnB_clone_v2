#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb")
def hello1():
    return "HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
