"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, 
а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, 
что исполнение кода не уложилось в данное время.

"""


import subprocess


from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange


app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[NumberRange(min=1, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
    try:
        process = subprocess.Popen()

@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()

if __name__ == '__main__':
    app.run(debug=True)
