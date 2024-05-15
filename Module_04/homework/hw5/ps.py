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
    print('1', args)

    # # Применяем shlex.quote:
    quote_args = [shlex.quote(arg) for arg in args]
    print('2', quote_args)

    clean_quote_args = ' '.join(quote_args)
    print('3', clean_quote_args)

    # Строим команду ps с применением аргументов:
    command = f'ps {clean_quote_args}'
    print('4', command)
    # clean_command = [shlex.quote(arg) for arg in command]

    # Вызываем команду:
    result = subprocess.run(command, capture_output=True)

    return f'<pre>{result.stdout}</pre>'


if __name__ == "__main__":
    app.run(debug=True)
