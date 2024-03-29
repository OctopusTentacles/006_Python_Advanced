"""
Реализуйте endpoint, начинающийся с /max_number, 
в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""


from flask import Flask


app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers: str) -> str:
    numbers_list = numbers.split('/')

    numbers_list = [float(elem) for elem in numbers_list if check_elem(elem) ]
    print(numbers_list)

    if not numbers_list:
        return f'Пожалуйста, введите <b>числа</b>!'

    max_num = max(numbers_list)
    
    return f'Максимальное число: <i>{max_num}</i>'

def check_elem(elem: str) -> bool:
    try:
        float(elem)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    app.run(debug=True)
