# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template


@app.route("/")
def index():
   movies = [{"Bahubali": "Fantasy"}, {"Rudramadevi": "Historical"},
              {"Khaidi150":"Action"}]
   return render_template("index.html", list=movies)


if __name__ == "__main__":
    app.run(debug=True)
