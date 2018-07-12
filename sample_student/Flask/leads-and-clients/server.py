from flask import Flask, request, render_template, redirect
from mysqlconnection import connectToMySQL


app = Flask(__name__)
mysql = connectToMySQL("leadsdb")


@app.route('/')
def index():
    clients: List[Dict[str, int]] = mysql.query_db("SELECT * FROM clients")
    return render_template('index.html', clients=clients)
