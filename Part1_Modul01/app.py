import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Это новая страничка, ответ сгенерирован в {now}'


# http://127.0.0.1:5555/test
#  или 
# http://localhost:5555/test

@app.route('/hello_world')
def hello_world():
    return f'Привет, мир!'
