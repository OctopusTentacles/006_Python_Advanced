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
import time

from typing import List
from flask import Flask
from flask import request


app = Flask(__name__)

logger = logging.getLogger('sort')


def bubble_sort(array: List[int]) -> List[int]:
    array_len = len(array)

    logger.debug(f'Начало выполнения bubble_sort:')
    start_time = time.time()

    # Внешний цикл по всем элементам массива:
    for i in range(array_len):
        # Внутренний цикл, который проходит по неотсортированной части массива:
        for j in range(0, array_len-i-1):
            # Если текущий элемент больше следующего, меняем их местами:
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    end_time = time.time()
    logger.debug(f'Время выполнения bubble_sort: {start_time - end_time:.3f} сек.')
    return array


def tim_sort(array: List[int]) -> List[int]:
    logger.debug(f'Начало выполнения tim_sort:')
    start_time = time.time()

    sorted_array = sorted(array)

    end_time = time.time()
    logger.debug(f'Время выполнения tim_sort {start_time - end_time:.3f} сек.')



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