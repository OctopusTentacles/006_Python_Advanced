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
# from Module_04.homework.hw1 import my_validators



# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class TestRegistration(unittest.TestCase):
    email = 'test@example.com'
    phone = 7774442288
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
        client = self.app.test_client()
        response = client.post('/registration_hw1', data = dict(
            email=self.email,
            phone=self.phone,
            name=self.name,
            address=self.address,
            index=self.index,
            comment=self.comment
        ))
        self.assertEqual(response.status_code, 200)
        logging.debug("Response status code: %s", response.status_code)

        self.assertIn('Successfully registered user', response.data.decode())
        logging.debug("Response data: %s", response.data.decode())




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
