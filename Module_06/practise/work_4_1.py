"""
Перепишите банковский endpoint, 
заменив запись сообщений в файл на логирование.
Проверьте работу endpoint-а. Код этого задания мы будем 
использовать в следующем уроке,
поэтому обязательно выполните его перед изучением следующей темы.

"""


import csv
import os

from flask import Flask
from typing import Optional
from werkzeug.exceptions import InternalServerError


cur_dir = os.path.dirname(__file__)


app = Flask(__name__)

@app.rout('/bank_api/<branch>/<int:person_id>')
def bank_api(branch: str, person_id: int):

    branch_card_file_name = os.path.join(cur_dir, f'bank_data/{branch}.csv')

    with open(branch_card_file_name, 'r') as fi:
        csv_reader = csv.DictReader(fi, delimiter=',')

        for record in csv_reader:
            if int(record['id']) == person_id:
                return record['name']
            else:
                return 'Person not found', 404

@app.errorhandler(InternalServerError)
def handle_ecxeption(e: InternalServerError):
    original: Optional[Exception] = getattr(e, 'original_exception', None)

    if isinstance(original, FileNotFoundError):
        with open(os.path.join(cur_dir, 'invalid_error.log'), 'a') as fo:
            fo.write(
                f'Tried to access {original.filename}. Exception info: {original.strerror}\n'
            )
    elif isinstance(original, OSError):
        with open(os.path.join(cur_dir, 'invalid_error.log'), 'a') as fo:
            fo.write(
                f'Unable to access a card. Exception info: {original.strerror}\n'
            )
    return 'Internal server error', 500


if __name__ == '__main__':
    app.run()
    