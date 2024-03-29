import datetime
import os
import random
import re
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


# ===================================================================
words = list()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

def get_words():
    global words
    with open(BOOK_FILE, 'r', encoding='utf8') as book:
        patern = r"\b[A-Za-zА-Яа-яЁё]+\b"
        words.extend(re.findall(patern, book.read()))
    
get_words()

@app.route('/get_random_word')
def get_random_word():
    word = random.choice(words)
    return f'Случайное слово из "Война и мир": {word}'


# ==================================================================
@app.route('/counter')
def counter():
    counter.visits += 1
    return f'Страница открыта {counter.visits} раз!'

counter.visits = 0

if __name__ == '__main__':
    app.run(debug=True)
