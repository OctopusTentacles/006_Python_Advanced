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
@app.route('/caiculate/', methods=['POST'])
def calculate():
    expression = request.json.get('expression')
    try:
        # eval принимает строку, интерпретирует её как 
        # арифметическое выражение и возвращает результат этого выражения:
        # # Вычисляем результат выражения:
        result = eval(expression)
        # Возвращаем результат в формате JSON:
        return jsonify(result=result)
    except ZeroDivisionError as exc:
        raise ZeroDivisionError(str(exc))
    except FloatingPointError as exc:
        raise FloatingPointError(str(exc))
    except OverflowError as exc:
        raise OverflowError(str(exc))
    except ArithmeticError as exc:
        raise ArithmeticError(str(exc))
    
# Обработчик ошибок для ArithmeticError:


# Обработчик ошибок для ZeroDivisionError:


# Обработчик ошибок для FloatingPointError:


# Обработчик ошибок для OverflowError:



if __name__ == '__main__':
    app.run(debug=True)
