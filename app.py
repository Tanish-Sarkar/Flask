from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "this is my first flask app"

@app.route("/about")
def about():
    return "This is about page"

@app.route('/contact')
def contct():
    return "Contact me from here"