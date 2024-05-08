"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. 
Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from Module_04.homework.hw1.registration import app



class TestRegistration(unittest.TestCase):
    def setUP(self):
        self.app = app.test_client()
        self.app.testing = True
    
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
