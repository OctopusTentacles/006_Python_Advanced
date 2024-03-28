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
        self.base_url = '/'
        self.base_url = '/hello-world/'

    def test_has_username(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)
        
    # заморозим день 2024-04-01 - понедельник:
    @freeze_time('2024-04-01')
    def test_weekday(self):
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        expected_greeting = 'Хорошего понедельника'
        self.assertIn(expected_greeting, response_text)



