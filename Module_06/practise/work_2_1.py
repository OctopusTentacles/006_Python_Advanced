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

@app.route('/bank_api/<branch>/<int:person_id>')
def bank_api(branch: str, person_id: int):
    log_execution('Entered bank_api function')
    branch_card_file_name = f'bank_data/{branch}.csv'
    log_execution(f'branch_card_file_name set to {branch_card_file_name}')

    with open(branch_card_file_name, 'r') as fi:
        log_execution(f'Opened file {branch_card_file_name}')
        csv_reader = csv.DictReader(fi, delimiter='')
        log_execution('Initialized csv_reader')

        for record in csv_reader:
            log_execution(f'Reading record: {record}')
            if int(record['id'] == person_id):
                log_execution(f'Found person with id {person_id}')
                return record['name']
            else:
                log_execution(
                    f'Person with id {person_id} not found in current record'
                )
        log_execution(
            f'Person with id {person_id} not found in the file'
        )
        return 'person not found', 404

@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError):
    log_execution('Entered handle_exception function')
    original: Optional[Exception] = getattr(e, 'original_exception', None)
    log_execution(f'Original exception: {original}')

    if isinstance(original, FileNotFoundError):
        log_execution(f'FileNotFoundError: {original.filename}')
        with open(os.path.join(cur_dir, 'invalid_error.log'), 'a') as fo:
            fo.write(
                f'Tried to access {original.filename}. Exception info: {original.strerror}\n'
            )
    elif isinstance(original, OSError):
        log_execution(f'OSError: {original.strerror}')
        with open(os.path.join(cur_dir, 'invalid_error.log'), 'a') as fo:
            fo.write(
                f'Unable to access a card. Exception info: {original.strerror}\n'
            )
    return 'Internal server error', 500


if __name__ == '__main__':
    log_execution('Starting Flask application')
    app.run(debug=True)
