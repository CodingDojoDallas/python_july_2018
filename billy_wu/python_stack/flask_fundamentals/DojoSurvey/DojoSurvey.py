from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def formpage():
    return render_template('DojoSurvey.html')

@app.route('/result', methods=['POST'])
def user_info():
    print("Got User Info")
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print(request.form)
    # return render_template('DojoSurveyResult.html', user=request.form)
    # return redirect('/DojoSurveyResult.html', user=request.form)
    return render_template('result.html', user=request.form)

@app.route('/danger')
def danger():
    print('a user tried to visit /danger.  we have redirected the user to /')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)