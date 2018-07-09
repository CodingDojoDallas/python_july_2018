from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)

def addTotal(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    now = datetime.datetime.now()
    print(now)
    sum = addTotal([int(request.form['strawberry']), int(request.form['raspberry']), int(request.form['blackberry']), int(request.form['apple'])])
    return render_template("checkout.html", checkout_time = now, total = sum)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
