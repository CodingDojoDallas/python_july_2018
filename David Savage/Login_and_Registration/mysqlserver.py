from flask import Flask, render_template, request, redirect, session, flash
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt  
import re

app = Flask(__name__)
app.secret_key = 'j5h)*ytg45##2*@ej'
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('reg_and_login')
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
    return render_template('Input_and_Edit.html')

# This is a route to use for validation. When the redirect comes here, check the email address. If it's bad then redirect back to the 
# Original / route and that will issue the flash error messages on the original form.
# If it's good then render the success form.

@app.route('/process_reg', methods=['POST'])
def process_reg():

    print("Made it to /process_reg")

    form_remail=request.form["remail"]
    query = "SELECT emailAddress FROM users WHERE emailAddress = %(form_remail)s;"
    data = { "emailAddress" : request.form['remail'] }
    possible_duplicates = mysql.query_db(query, data)
    print("Database read for registration ", possible_duplicates)


    if len(request.form['rfname']) == 0: #check to be sure first name was entered
        flash("Please enter a first name", 'rfname')
    elif (request.form['rfname']).isalpha == 1: #check to be sure that first name is alphabetic
        flash("Last name must be alphabetic", 'rfname')
    elif len(request.form['rlname']) == 0: #check to be sure last name was entered
        flash("Please enter a last name", 'rlname')
    elif (request.form['rlname']).isalpha == 1: #check to be sure that last name is alphabetic
        flash("Last name must be alphabetic", 'rlname')

    elif len(request.form['remail']) == 0: #check if email address was entered
        flash("Please enter an email address", 'remail')
    elif possible_duplicates is True: #check to see if email is already in the system
        flash("Your email is already present in our system, remail")
    elif not EMAIL_REGEX.match(request.form['remail']): #check to be sure there is an asterisk in email address
        flash("Email addresses must contain at least 1 asterisk!", 'remail')

    elif len(request.form['rpassword']) == 0:
        flash("Password must be entered", 'rpassword') 
    elif len(request.form['rpassword']) < 7:
        flash("Password must be at least 8 characters long", 'rpassword')
    elif len(request.form['rcpassword']) == 0:
        flash("Confirm Password must be entered when registering", 'rcpassword')
    elif request.form['rpassword'] != request.form['rcpassword']:
        flash(" Confirm password and Password do not match", 'rpassword')
    else:    
        print("Made it past all registration edits")
        print("Request Form ", request.form)

    if '_flashes' in session.keys():
        print ("Errors found in login validation")
        print (session.keys())
        return redirect("/")
    else:
        print ("No Errors found in login validation") 
        session['rfname'] = request.form['rfname']
        session['rlname'] = request.form['rlname']
        session['remail'] = request.form['remail']
        session['rpassword'] = request.form['rpassword']

        return redirect("/reg_success")



@app.route('/process_login', methods=['POST'])
def process_login():

    print("Made it to /process_login")

    query = "SELECT ID, emailAddress, password FROM users WHERE emailAddress = %(sql_lemail)s;" 
    data = { "sql_lemail":request.form['lemail'] } 
    email_in_database = mysql.query_db(query, data) 

    print("Email in database: ", email_in_database)

    print("Database read for login", email_in_database[0]['password'])

          # (result[0]['password'], request.form['password'])

    if len(request.form['lemail']) == 0: #check if email address was entered
        flash("Please enter an email address", 'lemail')
    elif email_in_database is False: 
        print("Email read was not found")
        print(email_in_database)
        flash("Your email address is not in our system", 'lemail')
    elif not EMAIL_REGEX.match(request.form['lemail']): #check to be sure there is an asterisk in email address
        flash("Email addresses must contain at least 1 @ symbol!", 'lemail')
    elif len(request.form['lpassword']) == 0:
        flash("Password must be entered", 'lpassword', ) 
    elif len(request.form['lpassword']) < 7:
        flash("Password must be at least 7 characters long", 'lpassword')
        print("Made it past all login edits")
        print("Request Form ", request.form)

    bcrypt.check_password_hash(email_in_database[0]['password'], request.form['lpassword'])

    if '_flashes' in session.keys():
        print ("Errors found in login validation")
        print (session.keys())
        return redirect("/")
    else:
        print ("No Errors found in login validation") 
        session['lemail'] = request.form['lemail']
        session['rfname'] = request.form['lpassword']
        return redirect("/login_success")

@app.route('/process_noclick', methods=['POST'])
def process_noclick():

    flash("No button was clicked", 'rfname')

    print("Made it to /process_noclick")

    print ("Neither button was clicked but the HTML form was returned.")
    return redirect("/")


@app.route('/reg_success')
def reg_success():

    print("Made it to reg_success")

      
    pw_hash = bcrypt.generate_password_hash(session['rpassword'])
    print(pw_hash)

    query = "INSERT INTO users (lastName, firstName, emailAddress, password, createdOn, updatedOn) VALUES (%(firstName)s, %(lastName)s, %(emailAddress)s, %(password)s, NOW(), NOW()) ;" 
    data = { "firstName":session['rfname'], "lastName":session['rlname'], "emailAddress":session['remail'], "password":pw_hash } 
    add_new_user = mysql.query_db(query, data)

    print("Made it to just after SQL insert in reg_success")
    print(add_new_user)

    return redirect("/application")

@app.route('/login_success')
def login_success():

    print ("Made it to login_success")
    print("Request Form again ", [session])

    return redirect("/application")

@app.route('/application')
def success():

    return render_template('David_Savage_Displaying_Blocks_With_Sound.html')

if __name__ == "__main__":
    app.run(debug=True)
    print("At the moment, we are not handling any routes on our server.")




