from flask import Flask, session, render_template, redirect
import random
app = Flask(__name__)
app.secret_key = 'secretsecret'

@app.route('/')
def mainpage():
    # session.clear()
    randint = random.randrange(1,101)
    print(session)
    return render_template('/GreatNumberGame.html')

@app.route('/guess')
def guess():
    if 'guess' not in session:
        session['guess'] = guess
        print(session)
    if session['guess'] >= randint:
        return redirect('/', number=1)
    elif session['guess'] <= randint:
        return redirect('/', number=2)


# @app.route('/destroy_session', methods=['POST'])
# def clearsession():
#     session.clear()
#     return redirect('/')

# @app.route('/addvalue', methods=['POST'])
# def addvalue():
#     session['counter'] += 1
#     # return render_template('/Counter.html')
#     return redirect('/')

if __name__=="__main__":
    app.run(debug=True)