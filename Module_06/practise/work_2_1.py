"""
Запустите локально пример с bank_api.
Попробуйте с помощью разных комбинаций параметров добиться того,
чтобы была выполнена каждая строчка кода - мы должны попасть 
во все функции, в каждый if и for блок.

Чтобы достоверно проверить выполнение каждой строчки кода,
можно добавить после каждого выражения запись в файл 
вида "строка такая-то была посещена"..
"""


import csv
import os

from flask import Flask
from typing import Optional
from werkzeug.exceptions import InternalServerError


# текущая дирректория для файлов:
cur_dir = os.path.dirname(__file__)


app = Flask(__name__)

def log_execution(line: str):
    with open(os.path.join(cur_dir, 'log.txt'), 'a') as log_file:
        log_file.write(f'{line}\n')

@app.route('bank_api/<branch>/<init:person_id>')
def bank_api(branch: str, person_id: int):
    log_execution('Entered bank_api function')