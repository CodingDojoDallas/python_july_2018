from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    print("Done")
    return render_template("index.html")

@app.route('/play')
def level1():
    print("Level One Rendered")
    return render_template("level1.html")

@app.route('/play/<x>')
def level2(x):
    boxes = int(x)
    print(int(x))
    return render_template("level2.html", box = boxes)

@app.route('/play/<x>/<color>')
def level3(x, color):
    boxes = int(x)
    return render_template("level3.html", box = boxes, colors = color)

if __name__ == "__main__":
    app.run(debug=True)
