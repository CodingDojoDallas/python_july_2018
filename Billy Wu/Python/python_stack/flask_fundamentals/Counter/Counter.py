from flask import Flask, session, render_template, redirect
app = Flask(__name__)
app.secret_key = 'secretsecret'

@app.route('/')
def counterpage():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    print(session)
    return render_template('/Counter.html')

@app.route('/destroy_session', methods=['POST'])
def clearsession():
    session.clear()
    return redirect('/')

@app.route('/addvalue', methods=['POST'])
def addvalue():
    session['counter'] += 1
    # return render_template('/Counter.html')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)