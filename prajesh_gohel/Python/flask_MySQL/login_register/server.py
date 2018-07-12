from flask import Flask, session, render_template, flash, request, redirect
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "NotTheBees!"
mysql = connectToMySQL('login_register')
print("all the emails", mysql.query_db("SELECT * FROM users;"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
             'email': request.form['email'],
           }
    result = mysql.query_db(query, data)
    print("*"*80)
    print(result)
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

    if len(request.form['pass_confirm']) < 1:
        flash("Please confirm your password")

    elif request.form['pass'] != request.form['pass_confirm']:
        flash("Password and Confirm Password must match!")

    if len(request.form['email']) < 1:
        flash("Email required")

    elif len(result) != 0:
        flash("This email already exists!")

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("You must input a valid email address!")

    if '_flashes' in session.keys():
        return redirect('/')

    else:
        pw_hash = bcrypt.generate_password_hash(request.form['pass'])
        session['email'] = request.form['email']
        session['logged_in'] = True
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pass_hash)s, NOW(), NOW());"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name': request.form['last_name'],
                 'email': request.form['email'],
                 'pass_hash': pw_hash
               }
        mysql.query_db(query, data)
        flash("You have successfully registered!")
        return redirect('/success')

@app.route('/verify', methods = ['POST'])
def verify():
    query = "SELECT password FROM users WHERE email = %(email)s;"
    data = {
             'email': request.form['email'],
           }
    result = mysql.query_db(query, data)
    print("*"*80)
    print(result)
    if len(request.form['email']) < 1:
        flash("Email required")

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("You must input a valid email address!")

    if len(request.form['passlog']) < 1:
        flash("Password required")

    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['passlog']):
            session['email'] = request.form['email']
            session['logged_in'] = True
            return redirect('/success')

    flash("Could not login")
    return redirect('/')

@app.route('/success')
def success():
    if session['logged_in'] == False:
        flash("Please Log in")
        return redirect('/')

    elif 'email' not in session:
        flash("Please Log in")
        return redirect('/')
        
    all_users = mysql.query_db("SELECT * FROM users")
    return render_template('logged_in.html', users = all_users)

@app.route('/log_out')
def log_out():
    session.pop('email')
    session['logged_in'] = False
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
