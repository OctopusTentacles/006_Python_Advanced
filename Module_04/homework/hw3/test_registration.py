"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. 
Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1.registration import app



class TestRegistration(unittest.TestCase):
    def setUP(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_valid_registration(self):
        # Создаем корректные данные для регистрации
        data = {
            'email': 'test@example.com',
            'phone': 9876543210,
            'name': 'Test User',
            'address': 'Test address',
            'index': 111999,
            'comment': ''
        }

        




if __name__ == '__main__':
    unittest.main()
