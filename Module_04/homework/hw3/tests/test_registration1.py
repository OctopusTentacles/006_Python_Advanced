"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. 
Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""


import logging
import unittest
from Module_04.homework.hw1.registration import app
from Module_04.homework.hw1.registration import RegistrationForm


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class TestRegistration(unittest.TestCase):
    email = 'test@example.com'
    phone = 1234567890
    name = 'Тест Т. Т.'
    address = 'Тест Тест Тест'
    index = 111111
    comment = 'Test comment'


    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def setUp(self):
        self.app = self.create_app()    


    def test_valid_email(self):
        email = 'test@example.com'
        # Отправляем POST-запрос с корректными данными
        response = self.app.post('/registration_hw1', email)
        # Проверяем, что статус код равен 200
        self.assertEqual(response.status_code, 200)
        # Проверяем, что ответ содержит сообщение об успешной регистрации
        self.assertIn('Successfully registered user', response.data.decode())




        # data = {
        #     'email': 'test@example.com',
        #     'phone': 9876543210,
        #     'name': 'Test User',
        #     'address': 'Test address',
        #     'index': 111999,
        #     'comment': ''
        # }






if __name__ == '__main__':
    unittest.main()
