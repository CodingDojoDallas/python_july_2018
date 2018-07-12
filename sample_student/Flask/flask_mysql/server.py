from flask import Flask, render_template
from mysqlerrors import connectToMySQL


app = Flask(__name__)


mysql = connectToMySQL('mydb')


@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users;")
    return render_template('index.html', users=users)
