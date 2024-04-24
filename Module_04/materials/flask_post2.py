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
    prices = data_object.get('nums', [])

    # Находим сдвиг, при котором массив вновь станет отсортированным:
    rotation_point = search_shift(prices)

    # Отсортированный массив с учетом сдвига:
    sorted_array = sorted(prices[rotation_point:] + prices[:rotation_point])

    return f'rotation point = {rotation_point}, Sorted array = {sorted_array}'


def search_shift(nums):
    """Двоичный поиск для нахождения сдвига массива.

    Args:
        nums (int): массив, который был подвергнут циклическому сдвигу.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        # находим средний элемент массива:
        mid = (left + right) // 2

        # сравниваем средний элемент с первым элементом:
        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == '__main__':
    app.run(debug=True)
