from flask import Flask, render_template, request, redirect, session
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('friendsdb')
# now, we may invoke the query_db method
print("Here are all the Friends: ", mysql.query_db("SELECT * FROM friends;"))
# print("Print Specified user", mysql.query_db("SELECT * FROM users Where ID = 3;"))
# print("Print Savage", mysql.query_db("SELECT user_first_name FROM users Where user_last_name = 'Savage';"))

@app.route('/')
def index():

    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched all friends", all_friends)
    return render_template('Input.html', friends = all_friends)

@app.route('/create_friend', methods=['POST'])

def create():
	
    print("***********************Made it to Create function")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(occupation)s, NOW(), NOW());"
    print("After Query")
    data = {
             'fname': request.form['fname'],
             'lname':  request.form['lname'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    print("Query and data sent to SQL.")
    return redirect('/')
    #return "jjjjjjjj"



if __name__ == "__main__":
    app.run(debug=True)
    print("At the moment, we are not handling any routes on our server.")