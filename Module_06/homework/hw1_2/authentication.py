"""
1. Сконфигурируйте логгер программы из темы 4 так, чтобы он:

* писал логи в файл stderr.txt;
* не писал дату, но писал время в формате HH:MM:SS,
  где HH — часы, MM — минуты, SS — секунды с ведущими нулями.
  Например, 16:00:09;
* выводил логи уровня INFO и выше.

"""

import getpass
import hashlib
import logging
import os


cur_dir = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('password_checker')


def is_strong_password(password: str) -> bool:
    return True

def input_and_check_password() -> bool:
    logger.info('Начало input_and_check_password')
    
    password:  str = getpass.getpass()
    if not password:
        logger.warning('Вы не ввели пароль')
        return False
    elif is_strong_password(password):
        logger.warning("Вы ввели слишком слабый пароль")
        return False
    
    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename=os.path.join(cur_dir, 'stderr.txt'),
        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt='%HH:%MM:%SS'
        )
    logger.info('Вы пытаетесь аутентифицироваться в Skillbox')

    count_number: int = 3
    logger.info(f'У вас есть {count_number} попыток')

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    logger.error('Пользователь трижды ввёл не правильный пароль!')
    exit(1)