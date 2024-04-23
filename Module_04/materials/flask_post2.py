"""
Представьте, что у нас есть массив данных цен на товар Х за день. 
Выглядит он как отсортированный по неубыванию массив, 
который был подвергнут циклическому сдвигу. Например:
[1, 2, 3, 5, -8, -6, -1, 0] или [2, 3, 4, 5, 0, 1]
Найдите сдвиг, при котором массив вновь станет отсортированным.
"""


import json
from flask import Flask, request


app = Flask(__name__)


@app.route('/find_rotation_point', methods=['POST'])
def find_rotation_point():

    # Получаем данные из тела запроса:
    form_data = request.get_data(as_text=True)
    data_object = json.loads(form_data)

    # Извлекаем массив цен на товар из данных:
    prices = data_object.get('prices', [])

    # Находим сдвиг, при котором массив вновь станет отсортированным:
    ...

def search_shift(nums):
    left, right = 0, len(nums) - 1
    ...



if __name__ == '__main__':
    app.run(debug=True)
