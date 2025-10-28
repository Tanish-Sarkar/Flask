from flask import Flask, request

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


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "You send data"
    else:
        return "You are only viewing the form"