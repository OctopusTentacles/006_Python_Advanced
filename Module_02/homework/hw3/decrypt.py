"""
Вася решил передать Пете шифрограмму.
Поскольку о промышленных шифрах Вася ничего не знает,
он решил зашифровать сообщение следующим образом: он посылает Пете строку.

Каждый символ строки — либо буква, либо пробел, либо точка «.», либо две точки «..».
Если после какой-то буквы стоит точка, значит, мы оставляем букву без изменений
(об одной точке Вася задумался, чтобы усложнить расшифровку). Саму точку при этом надо удалить.
Если после какой-то буквы стоят две точки, то предыдущий символ надо стереть. Обе точки при этом тоже нужно удалить.
Возможна ситуация, когда сообщение после расшифровки будет пустым.
В качестве результата можно вернуть просто пустую строку.

Примеры шифровок-расшифровок:

абра-кадабра. → абра-кадабра
абраа..-кадабра → абра-кадабра
абраа..-.кадабра → абра-кадабра
абра--..кадабра → абра-кадабра
абрау...-кадабра → абра-кадабра (сначала срабатывает правило двух точек, потом правило одной точки)
абра........ → <пустая строка>
абр......a. → a
1..2.3 → 23
. → <пустая строка>
1....................... → <пустая строка>

Помогите Пете написать программу для расшифровки.
Напишите функцию decrypt, которая принимает на вход шифр в виде строки, а возвращает расшифрованное сообщение.

Программа должна работать через конвейер (pipe):

$ echo  ‘абраа..-.кадабра’ | python3 decrypt.py
абра-кадабра

Команда echo выводит текст (в стандартный поток вывода).
"""


import re
import sys


# logical =============================================================
# def decrypt(encryption: str) -> str:
#     decrypted_message = ''
#     flag = False

#     for char in encryption:
#         if char != '.':
#             if flag:
#                decrypted_message = decrypted_message[:-1] + char
#                flag = False
#             else:
#                 decrypted_message += char
#         else:
#             if flag:
#                 decrypted_message = decrypted_message[:-2]
#                 flag = False
#             else:
#                 decrypted_message += char
#                 flag = True

#     if decrypted_message.endswith('.'):
#          decrypted_message = decrypted_message[:-1]

#     return (decrypted_message)


# if __name__ == '__main__':
#     data: str = sys.stdin.read()
#     decryption: str = decrypt(data)
#     print(decryption)


# regular ===========================================================
def decrypt(encryption: str) -> str:

    pattern = r'(^|[^.])(\.{1,2})'

    def remove_dots(match):
        char = match.group(1)
        dots = match.group(2)
        if dots == '..':
            return remove_dots(re.sub(pattern, r'', match.group(0)))
        elif dots == '.':
            return remove_dots(re.sub(pattern, char, match.group(0)))
        else:
            return match.group(0)

    decrypted_message = re.sub(pattern, remove_dots, encryption)
    return decrypted_message

if __name__ == '__main__':
    data: str = sys.stdin.read()
    decryption: str = decrypt(data)
    print(decryption)

