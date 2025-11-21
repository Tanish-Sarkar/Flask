from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student_profile():
    return render_template(
        'profile.html', name='Zac', is_topper=True,
        subjects = ['Maths', 'Quant', 'Economics']
    )