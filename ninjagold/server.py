from flask import Flask, session, render_template, request, redirect
import random
#import datetime  #datetime.datetime.now()
from datetime import datetime #datetime.now()
app = Flask(__name__)
app.secret_key ="hguirghirhtgitrwhgirthgitrhgrt"

@app.route('/')
def displayhome():
	#session.clear()

	if 'gold' not in session:
		session['gold'] = 0
	if 'activities' not in session:
		session['activities'] = [] #{'color':red, 'msg':"Earned 30 gold"}
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	print("******************")
	print(request.form)
	if 'farm' in request.form:
		if(len(request.form['farm']) == 0):
			print ("error")
		earned_gold = random.randint(10,20)
		session['gold'] += earned_gold
		d ={
		'col': "green",
		'msg': "Earned " + str(earned_gold) +" golds from the farm!" + datetime.now().strftime('%Y/%m/%d %I:%M %p')
		}
		session['activities'].append(d)
	elif 'cave' in request.form:
		earned_gold = random.randint(5,10)
		session['gold'] += earned_gold
		d ={
		'col': "green",
		'msg': "Earned " + str(earned_gold) +" golds from the cave!"
		}
		session['activities'].append(d)
	elif 'house' in request.form:
		earned_gold = random.randint(2,5)
		session['gold'] += earned_gold
		d ={
		'col': "green",
		'msg': "Earned " + str(earned_gold) +" golds from the house!"
		}
		session['activities'].append(d)
	elif 'casino' in request.form:
		earned_gold = random.randint(-50,50)
		session['gold'] += earned_gold
		if earned_gold < 0:
			d ={
		'col': "red",
		'msg': "Entered a casino and lost " + str(earned_gold) +" golds"
		}
			session['activities'].append(d)
		else:
			d ={
		'col': "green",
		'msg': "Earned " + str(earned_gold) +" golds from the casino!"
		}
			session['activities'].append(d)
		
	return redirect('/')
app.run(debug=True)
