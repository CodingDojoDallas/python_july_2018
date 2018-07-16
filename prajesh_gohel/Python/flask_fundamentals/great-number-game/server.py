from flask import Flask, render_template, session, redirect
import random
app = Flask(__name__)
app.secret_key = "3040293"

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(0, 101)

    if 'guess' > session['number']:


    print(session)
    return render_template('index.html')

@app.route('/check')
def game():
    print(request.form['guess'])
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)
