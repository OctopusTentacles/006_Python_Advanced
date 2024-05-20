from flask import Flask


app = Flask(__name__)

@app.endpoint('test')
def test_endpoint():
    return 'Test endpoint was called!'


if __name__ == '__main__':
    app.run()


# python simple_app.py & - знак амперсента позволяет запускать
# приложение на заднем фоне - [1] 26006 - получаем номер задания и бит процесса.


# python simple_app.py > /dev/null &
# перенаправляем output программы в никуда,
# dev/null - черная дыра.