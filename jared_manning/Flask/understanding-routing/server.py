# import session
# name in <input name=""> => request.POST['number']
from flask import *

app = Flask(__name__)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' in session:
        return render_template('index.html', number=session['number'])
    return render_template('index.html', number=None)


@app.route('/getinfo', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        session['number'] = request.form['number']
        return redirect(url_for('index'))
    return render_template('getinfo.html')
