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
print(logs)

# ===================================================================
def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    pass


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    pass


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    pass


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    pass


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    pass


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
