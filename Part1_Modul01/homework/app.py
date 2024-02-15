import datetime
import os
import random
from flask import Flask


app = Flask(__name__)


@app.route('/hello_world')
def hello():
    return f'«Привет, мир!»'


car_list = [
    'Chevrolet', 'Renault', 'Ford', 'Lada'
]
@app.route('/cars')
def cars():
    car_str = ', '.join(car_list)
    return car_str


cats_list = [
    'корниш-рекс', 'русская голубая', 
    'шотландская вислоухая', 'мейн-кун', 
    'манчкин',
]
@app.route('/cats')
def cats():
    cat = random.choice(cats_list)
    return cat


@app.route('/get_time/now')
def time_now():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return f'«Точное время: {current_time}»'


@app.route('/get_time/future')
def time_future():
    current_time = datetime.datetime.now()
    one_hour = datetime.timedelta(hours=1)
    current_time_after_hour = current_time + one_hour
    current_time_after_hour = current_time_after_hour.strftime('%H:%M:%S')
    return f'«Точное время через час будет {current_time_after_hour}»'



BASE_DIR = os.path.join(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace')

@app.route('/get_random_word')
def get_random_word():
    pass


# @app.route('/counter')
# def test_function():
#     pass


if __name__ == '__main__':
    app.run(debug=True)
