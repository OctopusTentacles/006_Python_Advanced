import json
from flask import Flask, request


app = Flask(__name__)
log_storage = []


@app.route('/log', methods=['POST'])
def log():
    """
    Записываем полученные логи которые пришли к нам на сервер
    return: текстовое сообщение об успешной записи, 
    статус код успешной работы

    """
    # получить данные в json формате:
    data = request.json
    if data:
        log_storage.append(data)
        return 'Логи получены', 201
    return 'Записи логирования не получены', 400
    ...


@app.route('/logs', methods=['GET'])
def logs():
    """
    Рендерим список полученных логов
    return: список логов обернутый в тег HTML <pre></pre>
    """
    ...


# ===================================================================
if __name__ == '__main__':
    app.run(debug=True)
