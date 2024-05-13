"""
Напишите GET-эндпоинт /uptime, 
который в ответ на запрос будет выводить строку вида 
f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, 
как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""


import subprocess
from flask import Flask


app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:

    # Выполнить команду uptime:
    result = subprocess.run(['uptime'], capture_output=True, text=True)
    uptime_info = result.stdout.strip()

    pattern = 

    return uptime_info

if __name__ == '__main__':
    app.run(debug=True)
