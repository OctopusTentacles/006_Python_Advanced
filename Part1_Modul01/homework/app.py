import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def hello():
    return f'«Привет, мир!»'


car_list = ['Chevrolet', 'Renault', 'Ford', 'Lada']

@app.route('/cars')
def cars():
    car_str = ', '.join(car_list)
    return car_str


# @app.route('/cats')
# def test_function():
#     pass


# @app.route('/get_time/now')
# def test_function():
#     pass


# @app.route('/get_time/future')
# def test_function():
#     pass


# @app.route('/get_random_word')
# def test_function():
#     pass


# @app.route('/counter')
# def test_function():
#     pass


if __name__ == '__main__':
    app.run(debug=True)
