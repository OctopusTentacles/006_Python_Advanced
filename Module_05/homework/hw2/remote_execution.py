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


from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[NumberRange(min=1, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
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
            return f'output: {stdout}, error: {None}'
        else:
            return f'output: {None}, error: {stderr}'
        
    except subprocess.TimeoutExpired:
        process.kill()
        return f'outut: {None}, error: Execution time out!'


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()

    # проверяем данные формы:
    if form.validate():
        code = form.code.data
        timeout = form.timeout.data
        result = run_python_code_in_subproccess(code, timeout)

        return result
    return 'Error! Invalid input!'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
