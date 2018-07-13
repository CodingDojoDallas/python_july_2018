from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default_Board():
    return render_template('Checkerboard_index.html',row=8,column=8)

@app.route('/<x>/<y>')
def customized_board(x,y):
    return render_template('Checkerboard_index.html',row=int(x),column=int(y))

if __name__=="__main__":
    app.run(debug=True)