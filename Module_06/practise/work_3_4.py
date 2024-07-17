"""
Опциональное задание

В примере с приложением, принимающем пароль,
у нас возникала ошибка, которую мы логировали через logger.exception(...) .
Более того, наш обработчик паролей не принимает ничего,
кроме латинских символов и цифр.

Подумайте, как можно исправить эту ошибку (подсказка: проблема в кодировке).

В качестве дополнения к заданию вы можете так же 
прочитать вот эту интересную статью:
https://habr.com/ru/post/312642/

"""


import getpass
import hashlib
import logging
import re


logger = logging.getLogger('password_checker')


def is_good_password(password):
    if len(password) < 8:
        logger.warning('Пароль слишком короткий. Минимальная длина пароля — 8 символов.')
        return False
    
    if not re.search(r'[A-Z]', password):
        logger.warning('Пароль должен содержать хотя бы одну заглавную букву.')
        return False

    if not re.search(r'[a-z]', password):
        logger.warning('Пароль должен содержать хотя бы одну строчную букву.')
        return False
    
    if not re.search(r'\d', password):
        logger.warning('Пароль должен содержать хотя бы одну цифру.')
        return False
    
    if not re.search(r'[!@#$%^&*()-+=_]', password):
        logger.warning('Пароль должен содержать хотя бы один специальный символ (!@#$%^&*()-+=_).')
        return False
    
    if not re.fullmatch(r'[A-Za-z0-9!@#$%^&*()-+=_]+', password):
        logger.warning('Пароль должен содержать только определенные символы!')
        return False
    
    return True


def input_and_check_password():
    logger.debug('Начало функции ввода пароля')
    password: str = getpass.getpass()

    if not password:
        logger.warning('Вы не ввели пароль!')
        return False
    
    if not is_good_password(password):
        logger.warning('Ваш пароль не надежный!')
        return False
    
    try:
        hasher = hashlib.md5()
        logger.info(f'Мы создали объект hasher {hasher!r}')

        hasher.update(password.encode('utf-8'))
        hashed_password = hasher.hexdigest()
        logger.info(f'Полученный хэш пароля: {hashed_password}')

        if hashed_password == '098f6bcd4621d373cade4e832627b4f6':
            logger.debug("Пароль совпадает с ожидаемым значением хэша.")
            return True
        else:
            logger.debug("Пароль не совпадает с ожидаемым значением хэша.")
    except ValueError as exc:
        logger.exception('Ошибка при обработке пароля', exc_info=exc)

    logger.debug("Конец input_and_check_password с результатом False")
    return False


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.debug('Придумайте надежный пароль')

    while True:
        try:
            count_number = int(input('Сколько попыток ввода: '))
            if 2 <= count_number <= 10:
                break
            else:
                logger.debug(f'Количество попыток должно быть от 2 до 10')
        except Exception:
            logger.exception('Ошибка ввода, введите целое число!')

    logger.info(f'У вас {count_number} попыток')

    while count_number > 0:
        if input_and_check_password():
            logger.info('Ваш пароль надежный. Можете его использовать!')
            exit(0)
        count_number -= 1
        logger.debug(f'Осталось {count_number} попыток!')

    logger.error('Пользователь использовал все попытки!')
    exit(1)
