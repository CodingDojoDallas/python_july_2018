from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
mysql = connectToMySQL('leads_and_clients')
print("all the users", mysql.query_db("SELECT * FROM Customers;"))

@app.route('/')
def index():
    all_customers = mysql.query_db("SELECT * FROM Customers")
    print("Fetched all customers", all_customers)
    return render_template('index.html', customers = all_customers)

if __name__ == '__main__':
    app.run(debug=True)
