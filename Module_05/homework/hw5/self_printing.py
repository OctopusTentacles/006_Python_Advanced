"""
Напишите код, который выводит сам себя.
Обратите внимание, что скрипт может быть расположен в любом месте.
"""

result = 0
for n in range(1, 11):
    result += n ** 2


# Secret magic code
import sys


with open(sys.argv[0], 'r') as py_file:
    py_file_content = py_file.read()

print(py_file_content)