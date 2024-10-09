"""
    Для реализации собственного StreamHandler, создадим новый класс, 
    который будет наследовать logging.StreamHandler. 
    Этот класс будет принимать поток на вход, 
    а если поток не указан, будет использовать sys.stderr.
"""


import logging
import sys


class MyStreamHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        if stream is None:
            stream = sys.stderr
        super().__init__(stream) # Вызов конструктора родителя для инициализации

    def emit(self, record):
        # Здесь можно обработать запись лога (record) перед выводом, если нужно
        super().emit(record)  
        # Используем родительский emit для стандартного поведения

# Если вы не вызовете super().__init__(stream), 
# то поток не будет передан в родительский класс StreamHandler, 
# и логирование может не работать корректно, 
# так как не будет задан поток для вывода логов.