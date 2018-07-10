from flask import Flask, render_template, session, redirect, request, flash
import re
PASSWORD_REGEX = re.compile(r'^?=[A-Z].*[0-9]$')
app = Flask(__name__)
app.secret_key = "TotallyNotASecretKey"

@app.route('/')
def index():
    print(session)
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def users():
    if len(request.form['first_name']) < 1:
        flash("First Name required")

    elif not request.form['first_name'].isalpha():
        flash("First Name can only have letters!")

    if len(request.form['last_name']) < 1:
        flash("Last Name required")

    elif not request.form['first_name'].isalpha():
        flash("Last Name can only have letters!")

    if len(request.form['pass']) < 1:
        flash("Password required")

    elif len(request.form['pass']) < 8:
        flash("Password is too short!")

    elif not PASSWORD_REGEX.match(request.form['pass']):
        flash("Password requires at least one uppercase letter and one number!")

    if len(request.form['pass_confirm']) < 1:
        flash("Please confirm your password")

    elif request.form['pass'] != request.form['pass_confirm']:
        flash("Password and Confirm Password must match!")

    if len(request.form['email']) < 1:
        flash("Email required")

    if '_flashes' in session.keys():
        return redirect('/')

    else:
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['pass'] = request.form['pass']
        session['pass_confirm'] = request.form['pass_confirm']
        session['email'] = request.form['email']
        flash("Success!")
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
