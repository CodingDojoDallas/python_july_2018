from flask import Flask, render_template, session, request, redirect
import random
import datetime
app = Flask(__name__)
app.secret_key = '1g5bX6rlke'

@app.route('/')
def index():
    # session.clear()
    if 'gold' not in session:
        session['gold'] = 0

    if 'activities' not in session:
        session['activities'] = [] #{'color': red, 'msg': "Earned 50 gold!"}
    return render_template('index.html')

@app.route('/process', methods = ["POST"])
def process():
    if request.form['building'] == 'farm':
        earned_gold = random.randint(20, 51)
        session['gold'] += earned_gold
        d = {
        'color': "green",
        'msg': "You earned" + str(earned_gold) + "gold from the farm. Nice!"
        }
        session['activities'].append(d)

    elif request.form['building'] == 'cave':
        earned_gold = random.randint(51, 101)
        session['gold'] += earned_gold
        d = {
        'color': "green",
        'msg': "You earned " + str(earned_gold) + " gold from the cave. Nice!"
        }
        session['activities'].append(d)

    elif request.form['building'] == 'house':
        earned_gold = random.randint(25, 201)
        session['gold'] += earned_gold
        d = {
        'color': "green",
        'msg': "You earned" + str(earned_gold) + "gold from the building. Nice!"
        }
        session['activities'].append(d)

    elif request.form['building'] == 'casino':
        earned_gold = random.randint(-1000, 1001)
        session['gold'] += earned_gold

    print("*"*70)
    print(session)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    print(session)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
