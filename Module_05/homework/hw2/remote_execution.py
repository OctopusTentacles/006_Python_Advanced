"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, 
а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, 
что исполнение кода не уложилось в данное время.

"""


import subprocess
import shlex
import time


from flask import Flask, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, NumberRange


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = FloatField(validators=[NumberRange(min=0, max=30)])


def run_python_code_in_subproccess(code: str, timeout: float):
    command = f'python -c "{code}"'

    # токенизация команды:
    token_command = shlex.split(command)

    try:
        # запуск процесса с перенаправлением вывода и ошибок:
        process = subprocess.Popen(
            token_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # ожидание завершения процесса по timeout:
        stdout, stderr = process.communicate(timeout=timeout)

        # получение кода завершения процесса:
        code_process = process.returncode

        if code_process == 0:
            stdout = stdout.decode('utf-8').strip()
            return {'output': stdout, 'error': None}
        else:
            stderr = stderr.decode('utf-8').strip()
            return {'output': None, 'error': stderr}
        
    except subprocess.TimeoutExpired:
        process.kill()
        return f'output: {None}, error: Время вышло!'
    finally:
        if process.stdout:
            process.stdout.close()
        if process.stderr:
            process.stderr.close()



@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()

    # проверяем данные формы:
    if form.validate():
        code = form.code.data
        timeout = form.timeout.data

        result = run_python_code_in_subproccess(code, timeout)

        return jsonify(result)
    else:
        return jsonify({'error': 'Некорректный ввод данных!'}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5001)
