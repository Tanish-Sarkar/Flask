from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Manual Dynamic Forms

# @app.route('/feedback', methods = ['POST', 'GET'])
# def feedback():
#     if request.method == 'POST':
#         name = request.form.get("username")   # returns None if not found (prevent KeyError and app crash)
#         message = request.form.get('message')

#         return render_template("thankyou.html", user = name, message = message)

#     return render_template("feedback.html")


app.secret_key = "my-secret-key"
@app.route('/', methods = ['POST', 'GET'])
def form():
    if request.method == 'POST':
        name = request.form.get("name")   # returns None if not found (prevent KeyError and app crash)
        if not name:
            flash("Name can not be empty")
            return redirect(url_for('form'))
        
        flash(f"Thanks {name}, your feedback was saved")
        return redirect(url_for("thankyou"))
    
    return render_template("form.html")

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")
