from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def green():

    return render_template('index.html', color='green')


@app.route('/<color>')
def color(color):

    return render_template('index.html', color=color)


# TODO: Add endpoint to change background color
# TODO: Implement JavaScript logic in Python for index.html template
# TODO: Add functionality to allow rgb or hex values in the URL
