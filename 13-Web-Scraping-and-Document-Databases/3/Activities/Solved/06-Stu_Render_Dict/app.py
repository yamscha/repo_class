# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    movie_dictionary = {"Movie_1": "Bahubali",
                            "Movie_2": "KhaidiNo1"}
    return render_template("index.html", dict=movie_dictionary)


if __name__ == "__main__":
    app.run(debug=True)
