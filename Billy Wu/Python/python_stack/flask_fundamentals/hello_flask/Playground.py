from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('Playground_index.html', phrase="Hello World!", times=0)

@app.route('/play')
def play():
    return render_template('Playground_index.html', phrase="Cheese!", times=3)

@app.route('/play/<x>')
def play_times(x):
    return render_template('Playground_index.html', phrase="Pizza!", times=int(x))

@app.route('/play/<x>/<color>')
def times_color(x, color):
    return render_template('Playground_index.html', phrase="Cookies!", times=int(x), boxcolor=color)

# @app.route('/play/<x>/<color>')
# def play
if __name__=="__main__":
    app.run(debug=True)