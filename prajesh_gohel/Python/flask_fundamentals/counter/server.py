from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "ThatsASpicyMeataball"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1

    print(session)
    return render_template('index.html')

@app.route('/double')
def double():
    session['count'] += 1
    print(session)
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('count')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
