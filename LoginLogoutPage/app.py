from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = 'supersecret'  # locking the session for security and our flash app will only know this

# Home login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("Username")
        password = request.form.get("Password")

        if username == 'admin' and password == '123':
            session['user'] = username  # store in session
            return redirect(url_for('welcome'))
        else:
            return Response("Fir se try kijiye", mimetype='text/plain')
        
    return """
            <h2>Login Page</h2>
            <form method='POST'>
            Username: <input type='text' name='Username'><br>
            Password: <input type='text' name='Password'><br>
            <input type='submit' value='Login'>
            </form>
        """


# welcome page after login
@app.route('/welcome')
def welcome():
    if 'user' in session:
        return f"""
                <h2>Welcome, {session['user']}!</h2>
                <a href={url_for('logout')}>Logout</a>

        """
    return redirect(url_for("login"))

# Logout Route
@app.route('/logout')
def logout():
    session.pop("user", None)  #None is for handdling the error in case user is not preent
    return redirect(url_for('login'))
