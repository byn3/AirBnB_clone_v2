#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
# from models.engine.db_storage import DBStorage
# from models.engine.file_storage import FileStorage
from flask import Flask, render_template
from models import storage
from os import environ
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


@app.route("/number_odd_or_even/<int:n>")
def hello6(n):
    word = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n, word=word)


@app.teardown_appcontext
def teardown_db(response_or_exec):
    """ tears down the db """
    storage.close()


@app.route("/states_list")
def hello7():
    """ sets up the states """
    array = list(storage.all("State").values())
    array.sort(key=lambda array: array.name)
    return render_template('7-states_list.html', elements=array)


@app.route("/cities_by_states")
def hello8():
    """ sets up the cities in states """
    array = list(storage.all("State").values())
    array.sort(key=lambda array: array.name)
    for state in array:
        state.cities.sort(key=lambda array: array.name)
    return render_template("8-cities_by_states.html", state=array)


@app.teardown_appcontext
def teardown_db2(POOO):
    """ tears down the P """
    storage.close()


@app.route("/states")
def hello9half():
    """ a comment """
    array = list(storage.all("State").values())
    # array = list(array.values())
    array.sort(key=lambda array: array.name)
    return render_template("9-states.html",
                           state=array, state_id=None, l=len(array))


@app.route("/states/<state_id>")
def hello9(state_id=None):
    """ sets up the cities in states """

    array = storage.all("State")
    if state_id:
        state = array.get("State.{}".format(state_id))
        if state:
            array = [state]
        else:
            array = []
    else:
        array = list(array.values())

    array.sort(key=lambda array: array.name)
    for state in array:
        state.cities.sort(key=lambda array: array.name)
    return render_template(
            "9-states.html", state=array, state_id=state_id, l=len(array))


@app.teardown_appcontext
def teardown_db3(POOO):
    """ tears down the P """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
