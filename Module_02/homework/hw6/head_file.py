"""
Реализуйте endpoint, который показывает превью файла, 
принимая на вход два параметра: SIZE (int) и RELATIVE_PATH —
и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен вернуть страницу с двумя строками.
В первой строке будет содержаться информация о файле: 
его абсолютный путь и размер файла в символах,
а во второй строке — первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path — написанный жирным абсолютный путь до файла;
result_text — первые SIZE символов файла;
result_size — длина result_text в символах.

Перенос строки осуществляется с помощью HTML-тега <br>.

Пример:

docs/simple.txt:
hello world!

/preview/8/docs/simple.txt
/home/user/module_2/docs/simple.txt 8
hello wo

/preview/100/docs/simple.txt
/home/user/module_2/docs/simple.txt 12
hello world!
"""


import os

from flask import Flask


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    """
    Превью файла,

    Args:
        size (int): кол-во символов.
        relative_path (str): относительный путь к файлу.
    """
    path_file = os.path.join(BASE_DIR, relative_path)
    with open(path_file, 'r', encoding='utf8') as file:
        read_size = file.read(size)
    return f'<b>{path_file}</b> {len(read_size)}<br>{read_size}'


if __name__ == "__main__":
    app.run(debug=True)
