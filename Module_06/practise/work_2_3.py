"""
Напишите Flask POST endpoint /calculate,
который принимает на вход арифметическое выражение и
вычисляет его с помощью eval (о безопасности думать не нужно,
работайте только над фукнционалом).

Поскольку наш Flask endpoint работает с арифметическими выражениями,
напишите 4 error_handler-а, которые будет обрабатывать
ArithmeticError, ZeroDivisionError, FloatingPointError и OverflowError
(о значении этих исключений вы можете посмотреть
вот на этой страничке https://docs.python.org/3/library/exceptions.html ).

Напишите по unit-тесту на каждую ошибку: 
тест должен проверять, что ошибка обрабатывается

Примечание: рекомендуется обрабатывать  ArithmeticError,
перехватывая InternalServerError ,
остальные классы ошибок можно обрабатывать напрямую.
"""

from flask import Flask
from flask import jsonify
from flask import request
from werkzeug.exceptions import InternalServerError


app = Flask(__name__)
@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json.get('expression')
    try:
        # eval принимает строку, интерпретирует её как 
        # арифметическое выражение и возвращает результат этого выражения:
        # # Вычисляем результат выражения:
        result = eval(expression)
        if isinstance(result, complex):
            result = str(result)
        # Возвращаем результат в формате JSON:
        return jsonify(result=result)
    except ZeroDivisionError as exc:
        raise ZeroDivisionError(str(exc))
    except OverflowError as exc:
        raise OverflowError(str(exc))
    except ArithmeticError as exc:
        raise InternalServerError(str(exc))
    except ValueError as exc:
        raise InternalServerError(str(exc))  
  
# Обработчик ошибок для ArithmeticError:
@app.errorhandler(InternalServerError)
def handle_arithmetic_error(exc):
    response = jsonify(error='Arithmetic Error: ' + str(exc))
    return response, 500

# Обработчик ошибок для ZeroDivisionError:
@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(exc):
    response = jsonify(error='Zero Division Error: ' + str(exc))
    return response, 400

# Обработчик ошибок для OverflowError:
@app.errorhandler(OverflowError)
def handle_overflow_error(exc):
    response = jsonify(error='Overflow Error: ' + str(exc))
    return response, 400


if __name__ == '__main__':
    app.run(debug=True)
