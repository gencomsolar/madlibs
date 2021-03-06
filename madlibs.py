"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""
    play_game = request.args.get("choice")
    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",)
                           # person=player,
                           # compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Send player to game page if yes, goodbye page if no"""

    play_game = request.args.get("choice")

    if play_game == "yes":
      return render_template("game.html")
    else:
      return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Render the result of the madlib"""

    color = request.args.get("color")
    animal = request.args.get("animal")
    name = request.args.get("name")
    activity = request.args.get("activity")
    food = request.args.get("food")
    location = request.args.getlist("location")

    return render_template("madlib.html", color=color, animal=animal,
                                          name=name, activity=activity, food=food,
                                          location=location)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
