"""
Ниже представлен endpoint, который принимают в POST массив чисел 
(в виде json), сортируют его одним из 3х алгоритмов и 
возвращают пользователю ответ.

Три применяемых алгоритма сортировки - сортировка пузырьком (bubble sort)
timsort (стандартная сортировка python) и сортировка кучей (heap sort).

Расставьте debug логирование в каждой функции логирования так,
чтобы по логам можно было понять сколько времени выполняется каждая функция.

Какая же сортировка в итоге выполняется быстрее?

"""


import heapq
import json
import logging

from typing import List
from flask import Flask
from flask import request


app = Flask(__name__)

logger = logging.getLogger('sort')


def bubble_sort(array: List[int]) -> List[int]:
    array_len = len(array)
    # Внешний цикл по всем элементам массива:
    for i in range(array_len):
        # Внутренний цикл, который проходит по неотсортированной части массива:
        for j in range()
            # Если текущий элемент больше следующего, меняем их местами:
    ...



def tim_sort():
    ...



def heap_sort():
    ...


algorithms = {
    'bubble': bubble_sort,
    'tim': tim_sort,
    'heap': heap_sort
}


@app.route('/<algorithm_name>/', methods=['POST'])
def sort_endpoint(algorithm_name: str):



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Start sort server!')

    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)