""" Тест для Задачи 1 - Хорошего дня! 

TestCase - для проверки ожидаемых результатов.

setUp - для настройки тестового окружения перед выполнением каждого теста. 
        Этот метод будет вызван перед каждым тестом, и вы можете использовать
        его для инициализации состояния или ресурсов, 
        необходимых для выполнения тестов.

Каждый метод начинается с префикса test_, 
что позволяет unittest обнаруживать эти методы как тесты автоматически. 
Внутри каждого метода выполняются проверки 
с использованием методов assert* из unittest.

..F. -  каждая точка представляет успешно пройденный тест, 
        а F представляет неудачный (тест с ошибкой).
"""


import unittest


from Module_03.homework.hw1.hello_word_with_day import app
from freezegun import freeze_time


class TestHelloWordWithDay(unittest.TestCase):
    """
    TestHelloWordWithDay является подклассом unittest.TestCase, 
    что обеспечивает его совместимость с фреймворком для автоматизированного 
    тестирования unittest. 
    """
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_has_username(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_custom_greeting(self):
        username = 'Хорошей субботы'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        if username in response_text:
            self.fail('Предупреждение: Не рекомендуется вводить пожелания в поле имени')

        
    # заморозим день 2024-04-01 - понедельник:
    @freeze_time('2024-04-01')
    def test_monday(self):
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        expected_greeting = 'Хорошего понедельника'
        self.assertIn(expected_greeting, response_text)

    @freeze_time('2024-04-02')
    def test_tuesday(self):
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        expected_greeting = 'Хорошего вторника'
        self.assertIn(expected_greeting, response_text)

    @freeze_time('2024-04-03')
    def test_wednesday(self):
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        expected_greeting = 'Хорошего воскресенья'
        self.assertIn(expected_greeting, response_text)

    @freeze_time('2024-04-04')
    def test_thursday(self):
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        expected_greeting = 'Хорошего четверга'
        self.assertIn(expected_greeting, response_text)

    @freeze_time('2024-04-05')
    def test_fryday(self):
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        expected_greeting = 'Хорошей пятницы'
        self.assertIn(expected_greeting, response_text)

    @freeze_time('2024-04-06')
    def test_saturday(self):
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        expected_greeting = 'Хорошей субботы'
        self.assertIn(expected_greeting, response_text)

    @freeze_time('2024-04-03')
    def test_sunday(self):
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        expected_greeting = 'Хорошего воскресенья'
        self.assertIn(expected_greeting, response_text)
