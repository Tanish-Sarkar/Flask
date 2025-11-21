from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')

    valids = {
        'Zac' : '123',
        'admin' : '456' 
    }

    if username in valids and password == valids[username]:
        return render_template('welcome.html', name = username)
    else:
        return "Invalid user"