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
        super().__init__(stream)
