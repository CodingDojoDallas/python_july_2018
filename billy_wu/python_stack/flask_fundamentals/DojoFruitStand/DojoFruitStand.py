from flask import Flask, render_template, redirect, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def formpage():
    return render_template('DojoFruitStand.html')

@app.route('/checkout', methods=['POST'])
def user_info():
    print("Got User Info")
    strawquantity = request.form['strawquantity']
    raspquantity = request.form['raspquantity']
    applequantity = request.form['applequantity']
    name = request.form['name']
    studentid = request.form['studentid']
    fruittotal = int(strawquantity) + int(raspquantity) + int(applequantity)
    print(request.form)
    return render_template('DojoFruitStandCheckout.html', user=request.form, total=fruittotal, datetime=datetime.now().strftime('%B %d %Y %I:%M:%S %p'))
    # return redirect('/checkout')

# @app.route('/checkout')
# def checkout():

if __name__=="__main__":
    app.run(debug=True)