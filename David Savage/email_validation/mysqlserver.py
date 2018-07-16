from flask import Flask, render_template, request, redirect, session, flash
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt  
import re

app = Flask(__name__)
app.secret_key = 'j5h)*ytg45##2*@ej'
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('email_validataion')
# now, we may invoke the query_db method
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument
# print("Here are all the Clients: ", mysql.query_db("SELECT * FROM clients;"))
# print("Here are all the Sites: ", mysql.query_db("SELECT * FROM sites;"))
# print("Here are all the Leads: ", mysql.query_db("SELECT * FROM leads;"))
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



# this is the route that that will issue the original HTML and to which it will come back. When the form comes back it will redirect to /process. Process will edit the form and 
# flash errors and then return to here to redisplay the form OR it will redirect to success. 

@app.route('/')
def index():
    return render_template('Input.html')

# This is a route to use for validation. When the redirect comes here, check the email address. If it's bad then redirect back to the 
# Original / route and that will issue the flash error messages on the original form.
# If it's good then render the success form.

@app.route('/process', methods=['POST'])
def process():

    print("Made it to process")

    print("Request Form ", request.form)

    query = "SELECT distinct emailAddress FROM emailaddress WHERE emailAddress = %(emailAddress)s;"
    data = { "emailAddress" : request.form['eaddress'] }
    possible_duplicates = mysql.query_db(query, data)

    print("Made it past SQL query")
    print("Possible duplicate length", len(possible_duplicates) )

    if len(request.form['eaddress']) < 1:
        flash("Email address cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['eaddress']):
        flash("Email addresses contain at least 1 asterisk!", 'email')
    elif len(possible_duplicates) > 0:
        flash("Duplicate email address!", 'email')

    print("made it past validation")

    if '_flashes' in session.keys():
        print ("Made it to return redirect /")
        return redirect("/")
    else:
        print ("Made it to return redirect /success") 
        session['eaddress'] = request.form['eaddress']
        return redirect("/success")



@app.route('/success')
def success():

    print ("Just before insert")
    print("Request Form again ", request.form)

    add_email = "INSERT INTO emailaddress (emailAddress,createdat,updatedat) VALUES (%(emailAddress)s, NOW(), NOW());"
    data = { "emailAddress" : session['eaddress'] }

    mysql.query_db(add_email, data)
   
    print("Just after insert")

    
    all_emails = mysql.query_db("SELECT * FROM emailaddress;")
    return render_template('Success.html', emails = all_emails)

# All the data has been edited. The email is not a duplicate. Insert this new email address into the database and then redirect to "/". Render_template to the new for that displays
# all the email addresses.

    # query = "SELECT distinct emailAddress FROM emailaddress WHERE emailAddress = 'davidsavagetx@gmail.com';"
    # data = { "emailAddress" : request.form['eaddress'] }
    # mysql.query_db(query, data)







# @app.route('/change_Dates', methods=['POST'])

# def create():
	
    # print("***********************Made it to Create function")
    # query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(occupation)s, NOW(), NOW());"
    # print("After Query")
    # data = {
    #          'fname': request.form['fname'],
    #          'lname':  request.form['lname'],
    #          'occupation': request.form['occupation']
    #        }
    # mysql.query_db(query, data)
    # print("Query and data sent to SQL.")
    # return redirect('/')


# @app.route('/createUser', methods=['POST'])
# def create():
#     # include some logic to validate user input before adding them to the database!
#     # create the hash
#     pw_hash = bcrypt.generate_password_hash(request.form['password'])  
#     print(pw_hash)  
#     # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'
#     # be sure you set up your database so it can store password hashes this long (60 characters)
#     query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password_hash)s);"
#     # put the pw_hash in our data dictionary, NOT the password the user provided
#     data = { "username" : request.form['username'],
#              "password_hash" : pw_hash }
#     mysql.query_db(query, data)
#     # never render on a post, always redirect!
#     return redirect("/")


# @app.route('/login', methods=['POST'])
# def login():
#     # see if the username provided exists in the database
#     query = "SELECT * FROM users WHERE username = %(username)s;"
#     data = { "username" : request.form["username"] }
#     result = mysql.query_db(query, data)
#     if result:
#         # assuming we only have one user with this username, the user would be first in the list we get back
#         # of course, for this approach, we should have some logic to prevent duplicates of usernames when we create users
#         # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
#         if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
#             # if we get True after checking the password, we may put the user id in session
#             session['userid'] = result[0]['id']
#             # never render on a post, always redirect!
#             return redirect('/success')
#     # if we didn't find anything in the database by searching by username or if the passwords don't match,
#     # flash an error message and redirect back to a safe route
#     flash("You could not be logged in")
#     return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
    print("At the moment, we are not handling any routes on our server.")