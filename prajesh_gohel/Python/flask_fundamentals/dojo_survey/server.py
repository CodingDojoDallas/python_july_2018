from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    print(request.form)
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    return render_template("result.html")

@app.route('/danger')
def danger():
    print('A user attempted to visit /danger. They have been redirected to /')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
