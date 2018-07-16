from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'MyNameJeff'
mysql = connectToMySQL('verifyemaildb')
print("all the emails", mysql.query_db("SELECT * FROM table1;"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    query = "SELECT * FROM table1 WHERE email = %(email)s;"
    data = {
             'email': request.form['email'],
           }
    result = mysql.query_db(query, data)
    if len(result) != 0:
        flash("This email already exists!")

    if len(request.form['email']) < 1:
        flash("You must input something!")

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("You must input a valid email address!")

    if '_flashes' in session.keys():
        return redirect('/')

    else:
        query = "INSERT INTO table1 (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        data = {
                 'email': request.form['email'],
               }
        mysql.query_db(query, data)
        return redirect('/verified')

@app.route('/verified')
def verified():
    emails = mysql.query_db("SELECT * FROM table1")
    print("Fetched all friends", emails)
    return render_template('verified.html', email = emails)

@app.route('/delete/<id>')
def delete(id):
    print("*"*80)
    print("Hello")
    query = "DELETE FROM table1 WHERE id = %(id)s;"
    print("*"*80)
    print("Done")
    data = {
        'id': int(id)
    }
    mysql.query_db(query, data)
    return redirect('/verified')

if __name__ == '__main__':
    app.run(debug=True)
