from flask import Flask, render_template, redirect, session, request, flash
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('customersdb')
# now, we may invoke the query_db method
print("all the customers_and_leads", mysql.query_db("SELECT * FROM customers_and_leads;"))

@app.route('/')
def index():
    all_customers_and_leads = mysql.query_db("SELECT * FROM customersdb")
    print("Fetched all customers_and_leads", all_customers_and_leads)
    return render_template('index.html', customers_and_leads = all_customers_and_leads)

if __name__ == "__main__":
    app.run(debug=True)
