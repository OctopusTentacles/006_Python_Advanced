""" Тест для Задачи 1 - Хорошего дня! """


import unittest

from hello_word_with_day import app
from datetime import datetime
from freezegun import freeze_time


class TestHelloWordWithDay(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        



