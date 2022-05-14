#!/usr/bin/python3
"""
The application listens on 0.0.0.0, port 5000.
Routes:
    - /: Displays 'Hello HBNB!'
    - /hbnb: Displays 'HBNB'
    - /c/<text>: Display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    - /python/(<text>): display “Python ”, followed by the value of the
        text variable (replace underscore _ symbols with a space ).
        The default value of text is “is cool”
    - /number/<n>: display “n is a number” only if n is an integer
    - /number_template/<n>: display a HTML page only if n is an integer:
        h1 tag: “Number: n” inside the tag body
    - /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_AirBnB():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Display C follow by the value of text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonn(text="is cool"):
    """Display default= is cool, other case = Python + <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def integ(n):
    """Display "<n> is a number" only if <n> is a integer"""
    if type(n) == int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html(n):
    """Display HTML and change h1 page only if n is an integer"""
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    Display HTML and change h1 page only if n is an integer
    “Number: n is even|odd”
    """
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html",
                               num="{} is even".format(n))
    else:
        return render_template("6-number_odd_or_even.html",
                               num="{} is odd".format(n))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
