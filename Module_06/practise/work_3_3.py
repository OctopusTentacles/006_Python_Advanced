"""
Хорошим паролем считается пароль, в котором есть
как минимум восемь символов, большие и маленькие буквы,
а также как минимум одна цифра и один символ из списка

!@#$%^&*()-+=_

Сделайте так, чтобы при вводе пароля проверялось, 
является ли пароль хорошим.
И если нет — предупредите пользователя (с помощью warning, конечно), 
что введённый пароль слабый. В идеале ещё и объясните почему.
"""


import getpass
import hashlib
import logging


logger = logging.getLogger('password_checker')

def is_good_password(password):
    
    
    ...


def input_and_check_password():
    logger.debug('Начало функции ввода пароля')
    password: str = getpass.getpass()

    if not password:
        logger.warning('Вы не ввели пароль!')
        return False
    
    if is_good_password(password):
        logger.warning('Введённый пароль слабый')
        return False
    
    try:
        hasher = hashlib.md5()
        logger.info(f'Мы создали объект hasher {hasher!r}')

        hasher.update(password.encode('latin-1'))
        logger.info('Пароль закодирован и обновлён в hasher')

        hashed_password = hasher.hexdigest()
        logger.info(f'Полученный хэш пароля: {hashed_password}')

        if hashed_password == '098f6bcd4621d373cade4e832627b4f6':
            logger.debug('Пароль совпадает с хэшем')
            return True
        else:
            logger.debug('Введен неверный пароль!')
    
    except ValueError as exc:
        logger.exception('Введен некорректный символ!')

    logger.info('Результат функции - False!')
    return False


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.debug('Вы пытаетесь авторизоваться')

    while True:
        try:
            count_number = int(input('Сколько попыток ввода: '))
            if 2 <= count_number <= 10:
                break
            else:
                logger.debug(f'Количество попыток должно быть от 2 до 10')
        except Exception:
            logger.exception('Ошибка ввода, введите целое число')
        
    logger.info(f'У вас {count_number} попыток')

    while count_number > 0:
        if input_and_check_password():
            logger.info('Аутентификация прошла успешно.')
            exit(0)
        count_number -= 1
        logger.debug(f'Осталось попыток: {count_number}')
    
    logger.error('Пользователь использовал все попытки!')
    exit(1)
