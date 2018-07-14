from flask import Flask, render_template, request, redirect, flash, session
import re
app = Flask(__name__)
app.secret_key = "MyNameIsGarfieldAndILoveLasagna"

@app.route('/')
def index():
    print(request.form)
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash("What's yo name???")

    if len(request.form['comment']) > 120:
        flash("Too many words! Your limit is 120 characters")

    elif len(request.form['comment']) < 1:
        flash("You need to comment, scrub!")

    if request.form['location'] == 'Choose...':
        flash("I need a location, ya doof!")

    if request.form['language'] == 'Choose...':
        flash("Pick a computer language!")

    if '_flashes' in session.keys():
        return redirect('/')

    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/result')

@app.route('/result')
def result():
    print(session)
    return render_template("result.html")

@app.route('/danger')
def danger():
    print("*"*80)
    print('A user attempted to visit /danger. They have been redirected to /')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
