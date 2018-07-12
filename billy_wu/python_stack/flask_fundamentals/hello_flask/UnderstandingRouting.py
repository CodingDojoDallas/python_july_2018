from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hihi "+name

@app.route('/repeat/<val>/<string>')
def repeat(val,string):
    return string*int(val)

if __name__=="__main__":
    app.run(debug=True)