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
    print(args)

    # # Применяем shlex.quote:
    quote_args = [shlex.quote(arg) for arg in args]
    print(quote_args)

    # Строим команду ps с применением аргументов:
    command = f'ps {quote_args}'
    print(command)
    # clean_command = [shlex.quote(arg) for arg in command]

    # Вызываем команду:
    result = subprocess.run(command, capture_output=True)

    return f'<pre>{result.stdout}</pre>'


if __name__ == "__main__":
    app.run(debug=True)
