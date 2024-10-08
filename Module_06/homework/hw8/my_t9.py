"""
У нас есть кнопочный телефон 
(например, знаменитая Nokia 3310), и мы хотим, чтобы пользователь 
мог проще отправлять СМС. Реализуем своего собственного 
клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, 
после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, 
состоящую из цифр 2–9,
и возвращает список слов английского языка, 
которые можно получить из этой последовательности цифр.

"""


import re
import os

from typing import List


cur_dir = os.path.dirname(os.path.abspath(__file__))

def my_t9(input_numbers: str) -> List[str]:
    t9_data = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    # составить рег.выражение соответствующее цифрам input_numbers:
    # 227 = [abc][abc][pqrs]
    pattern = ''.join([f'[{t9_data[num]}]' for num in input_numbers])
    reg_expression = re.compile(f'^{pattern}$')

    # прочитать файл со словами:
    with open(os.path.join(cur_dir, 'eng_words.txt')) as file:
        words_list = file.read().splitlines()
    
    # проверить список слов через рег.выражение:
    result = [word for word in words_list if reg_expression.match(word.lower())]
    return result


if __name__ == '__main__':
    numbers: str = input()
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
