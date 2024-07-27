"""
Представим, что мы работаем в IT отделе крупной компании.
У HR отдела появилась гениальная идея - поздравлять сотрудников
в день рождения однодневным отгулом.

Для этого HR отделу надо предоставить данные на всех
сотрудников вместе с их датами рождения.
Сотрудники у нас работают либо в IT-, либо в PROD-отделе.
Идентификационным номером сотрудника является число,
анкеты сотрудников в формате json вы можете найти в папке fixtures.
В написанное приложение добавьте логи так,
чтобы они помогли найти ошибки со следующими сотрудниками
    отдел IT, сотрудники 1, 2, 3, 4, 5
    отдел PROD, сотрудники 1, 2, 3, 4, 5
"""


import json
import logging
import os

from flask import Flask


app = Flask(__name__)

logger = logging.getLogger('account_book')
currrent_dir = os.path.dirname(os.path.abspath(__file__))
fixtures_dir = os.path.join(currrent_dir, 'fixtures')

departments = {"IT": "it_dept", "PROD": "production_dept"}


@app.route('/account/<department>/<int:account_number>/')
def account(department: str, account_number: int):
    dept_directory_name = departments.get(department)
    if dept_directory_name is None:
        logger.error(f'\tОтдел {department} не найден')
        return 'Department not found', 404
    
    full_department_path = os.path.join(fixtures_dir, dept_directory_name)
    account_data_file = os.path.join(full_department_path, f'{account_number}.json')

    logger.info(f'\tЗапрашивается файл {account_data_file}')
    if not os.path.exists(account_data_file):
        logger.error(f'\tФайл {account_data_file} не найден')
        return 'Account not found', 404

    try:
        with open(account_data_file, 'r') as fi:
            account_data_txt = fi.read()
    except Exception as exc:
        logger.exception(f'\tОшибка чтения файла {account_data_file}: {exc}')
        return 'Error reading account data', 500
    
    try:
        account_data_json = json.loads(account_data_txt)
        name, birth_date = account_data_json['name'], account_data_json['birth_date']
    except json.JSONDecodeError as exc:
        logger.exception(f'\tОшибка декодирования JSON из файла {account_data_file}: {exc}')
        return 'Error decoding account data', 500
    except KeyError as e:
        logger.exception(f'\tОшибка ключа в данных аккаунта: {e}')
        return 'Error in account data', 500

    day, month, _ = map(int, birth_date.split('.'))
    if not (1 <= day <= 31):
        logger.error(f'\tНеверный день {day}')
        return 'Wrong day', 404
    elif not (1 <= month <= 12):
        logger.error(f'\tНеверный месяц {month}')
        return 'Wrong month', 404
    else:
        logger.info(
            f'\tИнформация о сотруднике {name} с идентификационным номером {account_number} получена успешно.'
        )
        return f'{name} was born on {day}.{month}'


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('\tStart account_book server!')
    app.run(debug=True)
