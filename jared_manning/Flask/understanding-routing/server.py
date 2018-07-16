from flask import Flask, route, request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


# I'm really happy with how this route and the private function turned out. :D
@app.route('/say')
@app.route('/say/flask')
@app.route('/say/michael')
@app.route('/say/john')
@app.route('/say/<other_name>')
def say_hi(other_name=None):
    return f'Hi {__get_name(request.path)}!'


def __get_name(path):
    return {
        '/say/flask': 'Flask',
        '/say/michael': 'Michael',
        '/say/john': 'John',
        '/say': 'Root'
    }.get(path, 'Stranger')


@app.route('/repeat/<times>/<word>')
def repeat(times, word='default'):
    times = int(times)
    return f'{word} ' * times

# Deprecated. Run `FLASK_ENV=development FLASK_APP=server.py flask run` in your
# terminal.
# if __name__ == '__main__':
#     app.run()
