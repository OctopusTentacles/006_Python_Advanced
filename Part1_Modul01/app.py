import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/test')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Это новая страничка, ответ сгенерирован в {now}'


# http://127.0.0.1:5555/test
#  или 
# http://localhost:5555/test

@app.route('/hello/world')
def hello_world():
    return f'Привет, мир!'


# global variable:
count = 0
@app.route('/counter')
def run_count():
    global count
    count += 1
    return f'Страница открыта {count} раз!'
