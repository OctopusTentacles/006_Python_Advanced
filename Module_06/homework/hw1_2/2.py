"""
2. К нам пришли сотрудники отдела безопасности и сказали, что, 
согласно новым стандартам безопасности,
хорошим паролем считается такой пароль, 
который не содержит в себе слов английского языка,
так что нужно доработать программу из предыдущей задачи.

Напишите функцию is_strong_password, 
которая принимает на вход пароль в виде строки,
а возвращает булево значение, которое показывает, 
является ли пароль хорошим по новым стандартам безопасности.

"""


import getpass
import hashlib
import logging
import nltk
import os

from nltk.corpus import words

#====================================================================
import ssl
import certifi

# Настройка SSL контекста для использования certifi
ssl._create_default_https_context = ssl._create_unverified_context

cur_dir = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('password_checker')

# Создать папку nltk_data:
nltk_dir = os.path.join(cur_dir, 'nltk_data')
os.makedirs(nltk_dir, exist_ok=True)

# Указать путь к данным NLTK:
nltk.data.path.append(nltk_dir)

# Загрузка словаря английских слов:
nltk.download('words', download_dir=nltk_dir)

#====================================================================

def is_strong_password(password: str) -> bool:
    # Преобразуем список слов в множество для быстрого поиска:
    data_words = set(words.words())
    # Нижний регистр для пароля:
    password_lower = password.lower()
    for word in data_words:
        if word in password_lower:
            logger.debug(f'Пароль содержит английское слово: {word}')
            return False
    return True

def input_and_check_password() -> bool:
    logger.info('Начало input_and_check_password')
    
    password:  str = getpass.getpass()
    if not password:
        logger.warning('Вы не ввели пароль')
        return False
    elif not is_strong_password(password):
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
        datefmt='%H:%M:%S'
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
