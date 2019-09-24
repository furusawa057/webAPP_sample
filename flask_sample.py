import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return '<h1>Hello World from Japan</h1>'


@app.route('/goodbye')
def goodbye():
    return 'Goodbye'


@app.route('/add/<a>/<b>')
def add(a, b):
    return str(int(a) + int(b))


@app.route('/omikuji')
def omikuji():
    results = ['大吉', '吉', '凶']
    # fortune_num=random.randint(0,len(result)-1)
    result = random.choice(results)
    # return f'今日の運勢は{result}'
    return render_template('omikuji.html', unsei=result)


if __name__ == '__main__':
    app.run(debug=True)
