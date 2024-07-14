"""
Количество попыток ввода неправильного пароля у нас 
строго зашито в коде программы, это плохо.
Пусть наша программа будет чуть более вежливой и спросит, 
сколько раз пользователь хочет ввести пароль.

Минимальное количество раз — два, максимальное — десять.

В случае возникновения ошибок нужно, конечно, 
правильным образом их залогировать.

"""


import getpass
import hashlib
import logging


logger = logging.getLogger('password_checker')

def input_and_check_password():
    logger.debug('Нчало функции ввода пароля\n')
    password: str = getpass.getpass()

    if not password:
        logger.warning('Вы не ввели пароль')
        return False
    
    try:
        hasher = hashlib.md5()
        



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.debug('Вы пытаетесь авторизоваться\n')
    
    count_number: int = 3
    logger.info(f'У вас {count_number} попыток\n')

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error('Пользователь использовал все попытки!\n')
    exit(1)