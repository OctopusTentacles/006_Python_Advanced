"""
Напишите GET-эндпоинт /ps, 
который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""


import subprocess

from flask import Flask, request
from typing import List


app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    # Получаем аргументы из запроса:
    args: List[str] = request.args.getlist('arg')

    command = ['ps'] + args
    ...


if __name__ == "__main__":
    app.run(debug=True)
