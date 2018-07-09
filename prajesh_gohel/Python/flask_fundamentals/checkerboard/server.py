from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default():
    print("That's a spicey meataball!")
    return render_template("default.html")

@app.route('/<x>/<y>')
def custom(x, y):
    rows = int(y)
    squares = int(x)
    return render_template("custom.html", row = rows, square = squares)

if __name__ == '__main__':
    app.run(debug=True)
