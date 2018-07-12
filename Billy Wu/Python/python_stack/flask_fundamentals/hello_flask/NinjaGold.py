from flask import Flask, session, render_template, request, redirect, random
#import datetime # needs datetime.datetime.now() in code
from datetime import datetime # this line lets us use just datetime.now()
app = Flask(___name___)
app.secret_key = "as;lfkj"

@app.route('/')
def displayHome():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []#{'color':red, 'msg':"earned x gold"}
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)#checks forms, good practice to check stuff
    if 'farm' in request.form:
        earned.gold = random.randint(10,20)
        session['gold'] += earned.gold
        d = {
            'col': "green",
            'msg': "Earned " + str(earned_gold) + " gold from the farm!"#add datetime as well, datetime.now()
            #datetime.now().strftime('%Y/%m/%d %I:%M%p')
        }
        session['activities'].append(d)
    elif 'cave' in request.form:
        earned.gold = random.randint(5,10)
        session['gold'] += earned.gold
    elif 'house' in request.form:
        earned.gold = random.randint(2,5)
        session['gold'] += earned.gold
    elif 'casino' in request.form:
        earned.gold = random.randint(-50,50)
        session['gold'] += earned.gold
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)