from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "your-very-secret-key-here-make-it-long-and-random"

@app.route('/', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome {name}!, You Registered Successfully", "success")
        return redirect(url_for("success"))
    
    # Print form errors for debugging
    if form.errors:
        print("Form errors:", form.errors)
    
    return render_template("register.html", form=form)

@app.route('/success')
def success():
    return render_template("success.html")

# if __name__ == '__main__':
#     app.run(debug=True)