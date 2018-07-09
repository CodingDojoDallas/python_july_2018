from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("\n", "-"*80, "\nSuccess!", "\n")
    return "Hello World!"

@app.route("/dojo")
def dojo():
    print("\n", "-"*80, "\nSuccess!", "\n")
    return "Dojo"

@app.route("/say/<name>")
def say(name):
    # print("\n", "-"*80, "\nSuccess!", "\n")
    print(name)
    return "Hi "+name.capitalize()

@app.route("/repeat/<num>/<name>")
def repeat(num, name):
    output = (name + " ")*int(num)
    print(output)
    return output

if __name__ == '__main__':
    app.run(debug=True)
