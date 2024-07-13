"""
В приложении для парольной аутентификации, которое мы рассматривали, 
недостаточно debug-сообщений. Добавим после каждой строки с кодом 
в функции input_and_check_password ещё по debug-сообщению, 
например:
f"Мы создали объект hasher {hasher!r}"
после строки:
"hasher = hashlib.md5()"
"""


import getpass
import hashlib
import logging


logger = logging.getLogger('password_checker')


def input_and_check_password():
    logger.debug('Начало input_and_check_password')

    password: str = getpass.getpass()
    logger.info('Ввели пароль')

    if not password:
        logger.warning('Вы не ввели пароль')
        return False
    



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Вы пытаетесь аутентифицироваться в Skillbox')

    count_number: int = 3
    logger.info(f'У вас есть {count_number} попыток')

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    logger.error('Пользователь трижды ввёл не правильный пароль!')
    exit(1)