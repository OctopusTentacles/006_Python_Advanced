import json
from flask import Flask, request


app = Flask(__name__)

# хранилище логов:
log_storage = []


@app.route('/logs', methods=['POST'])
def log():
    """
    Записываем полученные логи которые пришли к нам на сервер
    return: текстовое сообщение об успешной записи, 
    статус код успешной работы

    """
    # получить данные в json формате:
    data = request.json
    print(f"Получены данные: {data}")  # Временный вывод для отладки

    if data:
        log_storage.append(data)
        return 'Логи получены', 201
    return 'Записи логирования не получены', 400
    


@app.route('/logs', methods=['GET'])
def logs():
    """
    Рендерим список полученных логов
    return: список логов обернутый в тег HTML <pre></pre>
    """
    log_text = '\n'.join(json.dumps(log, indent=2) for log in log_storage)
    
    return f'<pre>{log_text}</pre>', 200


# ===================================================================
if __name__ == '__main__':
    app.run(debug=True)
