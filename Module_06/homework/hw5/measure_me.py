"""
Каждый лог содержит в себе метку времени, а значит, 
правильно организовав логирование,
можно отследить, сколько времени выполняется функция.

Программа, которую вы видите, по умолчанию пишет логи в stdout. 
Внутри неё есть функция measure_me,
в начале и в конце которой пишется "Enter measure_me" 
и "Leave measure_me".

Сконфигурируйте логгер, запустите программу, соберите логи 
и посчитайте среднее время выполнения функции measure_me.
"""


import json
import logging
import random
import re
import os

from datetime import datetime
from typing import List


# текущая директория:
cur_dir = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger(__name__)

# ===================================================================
# анализ логов:
def measure_log_time(log_file: str) -> float:
    enter_time = []
    leave_time = []

    # найти строки с "Enter measure_me" и "Leave measure_me":
    with open(log_file, 'r') as file:
        for line in file:
            if 'Enter measure_me' in line:
                # ищем время в этой строке через рег.выражения:
                match_time = re.search(
                    r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+',
                    line
                ).group(0)
                # добавляем в enter_time в формате datetime:
                enter_time.append(
                    datetime.strptime(match_time, '%Y-%m-%d %H:%M:%S.%f')
                )
            elif 'Leave measure_me' in line:
                # ищем время в этой строке через рег.выражения:
                match_time = re.search(
                    r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+',
                    line
                ).group(0)
                # добавляем в enter_time в формате datetime:
                leave_time.append(
                    datetime.strptime(match_time, '%Y-%m-%d %H:%M:%S.%f')
                )
    for enter, leave in zip(enter_time, leave_time):
        print('время выполнения:', leave - enter)


# ===================================================================
def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.debug("Leave measure_me")

    return results


if __name__ == "__main__":
    # ===============================================================
    # сконфигурировать логгер:
    logging.basicConfig(
        level="DEBUG",
        filename=os.path.join(cur_dir, 'stdout.log'),
        format='%(asctime)s.%(msecs)03d | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    for it in range(15):
        data_line = get_data_line(10 ** 3)
        measure_me(data_line)

    measure_log_time(os.path.join(cur_dir, 'stdout.log'))
