"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""

import os


def get_summary_rss(ps_output_file_path: str) -> str:
    with open(ps_output_file_path, 'r') as output_file:
        lines = output_file.readlines()[1:]

        total_memory = 0

        for line in lines:
            columns = line.split()
            total_memory += int(columns[5])

    units = ['Б', 'Кб', 'Мб', 'Гб', 'Тб']
    cur_unit_index = 0
        
    return total_memory


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path: str = os.path.join(BASE_DIR, 'output_file.txt')
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
