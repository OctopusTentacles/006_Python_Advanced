"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, 
сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. 
Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""


import json
import os

from collections import Counter
from datetime import datetime
from typing import Dict


# текущая директория:
cur_dir = os.path.dirname(os.path.abspath(__file__))

# ===================================================================
# Файл с логами считывается только один раз.
def read_logs():
    logs = list()

    with open(os.path.join(cur_dir, 'skillbox_json_messages.log'), 'r') as file:
        for line in file:
            log = json.loads(line.strip())
            logs.append(log)
        return(logs)

logs = read_logs()

# ===================================================================
def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    # найдем в каждой строке значение ключа 'level'
    # и посчитаем через Counter
    level_count = Counter(log['level'] for log in logs)
    return dict(level_count)


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    # найдем в каждой строке значение ключа 'time'
    # преобразуем в объект datetime с формаотм '%H:%M:%S'
    # и возьмем только часы .hour -> список часов
    hours_list = [datetime.strptime(log['time'], '%H:%M:%S').hour for log in logs]
    # посчитаем через Counter
    hours_count = Counter(hours_list)
    # находим самое большое кол-во часов
    # и берем первый элемент из кортежа [0][0] - час
    hours_most_common = hours_count.most_common(1)[0][0]
    return hours_most_common


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    # временные границы
    start_time = datetime.strptime('05:00:00', '%H:%M:%S')
    end_time = datetime.strptime('05:20:00', '%H:%M:%S')
    # список логов по условию
    crittical_logs = [
        log for log in logs
        if log['level'] == 'CRITICAL' and (
            start_time <= datetime.strptime(log['time'], '%H:%M:%S') <= end_time
        )
    ]
    # кол-во логов - длина списка
    return len(crittical_logs)


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    # dog_message = [
    #     log['message'] for log in logs
    #     if 'dog' in log['message']
    # ]
    # return len(dog_message)
    dog_message = sum('dog' in log['message'] for log in logs)
    return dog_message


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    warning_messages = [
        log['message'] for log in logs
        if log['level'] == 'WARNING'
    ]
    count_words = Counter(warning_messages)
    print(count_words)
    return

if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
