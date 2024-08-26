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
import os
import re


#====================================================================

logger = logging.getLogger('password_checker')

# текущая директория:
cur_dir = os.path.dirname(os.path.abspath(__file__))

# путь к файлу со словами:
words_file_path = os.path.join(cur_dir, 'words.txt')

#====================================================================

# предобработка файла слов:
def load_words(file_path: str) -> set:
    words_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            # убираем пробелы и приводим к нижнему регистру:
            word = line.strip().lower()
            # берем слова длиной больше 4 символов:
            if len(word) > 4 and word.isalpha():
                words_set.add(word)
    return words_set

# загрузка слов в множество:
english_words = load_words(words_file_path)

#====================================================================

def is_strong_password(password: str) -> bool:
    # нижний регистр для пароля:
    password_lower = password.lower()
    # находим слова в пароле через re:
    found_words = re.findall(r'\b[a-z]+\b', password_lower)
    # проверяем слово:
    

    # Проверка на буквы:
    contains_letter = any(char.isalpha() for char in password)
    if not contains_letter:
        logger.debug('Пароль не содержит букв')
        return False
    
    # Проверка на цифры:
    contains_digit = any(char.isdigit() for char in password)
    if not contains_digit:
        logger.debug('Пароль не содержит цифры')
        return False

    
    for word in data_words:
        if len(word) > 4 and word in password_lower:
            logger.debug(f'Пароль содержит английское слово: {word}')
            return False
    return True

def input_and_check_password() -> bool:
    logger.info('===== START input_and_check_password =====')
    
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
        logger.warning("НЕВЕРНЫЙ ПАРОЛЬ!")
    except Exception as ex:
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
