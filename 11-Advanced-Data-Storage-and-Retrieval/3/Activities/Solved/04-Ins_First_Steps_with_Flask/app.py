# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
application = Flask(__name__)


# 3. Define what to do when a user hits the index route
@application.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user hits the /about route
@application.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    application.run(debug=True)
