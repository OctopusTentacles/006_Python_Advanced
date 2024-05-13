"""
Напишите GET-эндпоинт /ps, 
который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""


import shlex, subprocess

from flask import Flask, request
from typing import List


app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    # Получаем аргументы из запроса:
    args: List[str] = request.args.getlist('arg')

    # Преобразуем аргументы в строку, разделяя их пробелами
    args_str = ' '.join(args)


    command = ['ps'] + args
    clean_command = [shlex.quote(arg) for arg in command]

    result = subprocess.run(clean_command, capture_output=True)

if __name__ == "__main__":
    app.run(debug=True)
