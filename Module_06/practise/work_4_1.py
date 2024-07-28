"""
Перепишите банковский endpoint, 
заменив запись сообщений в файл на логирование.
Проверьте работу endpoint-а. Код этого задания мы будем 
использовать в следующем уроке,
поэтому обязательно выполните его перед изучением следующей темы.

"""


import csv
import logging
import os

from flask import Flask
from typing import Optional
from werkzeug.exceptions import InternalServerError


cur_dir = os.path.dirname(__file__)
logger = logging.getLogger('bank_api')

app = Flask(__name__)

@app.route('/bank_api/<branch>/<int:person_id>')
def bank_api(branch: str, person_id: int):

    branch_card_file_name = os.path.join(cur_dir, f'bank_data/{branch}.csv')

    with open(branch_card_file_name, 'r') as fi:
        csv_reader = csv.DictReader(fi, delimiter=',')
        logger.debug(f'читаем файл: {branch_card_file_name}')

        for record in csv_reader:
            if int(record['id']) == person_id:
                logger.info(f'Найден пользователь с ID {person_id}')
                return record['name']
        logger.info(f'Пользователь с ID {person_id} не найден')
        return 'Person not found', 404

@app.errorhandler(InternalServerError)
def handle_ecxeption(e: InternalServerError):
    original: Optional[Exception] = getattr(e, 'original_exception', None)

    if isinstance(original, FileNotFoundError):
        logger.debug(f'Tried to access {original.filename}. Exception info: {original.strerror}\n')

    elif isinstance(original, OSError):
        logger.debug(f'Unable to access a card. Exception info: {original.strerror}\n')

    else:
        logger.error(f'An unexpected internal server error occurred: {e}')
    return 'Internal server error', 500


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename=os.path.join(cur_dir, 'banking.log')
        )
    app.run()
