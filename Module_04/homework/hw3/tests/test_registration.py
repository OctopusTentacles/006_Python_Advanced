"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. 
Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""


import logging
import unittest

from homework.hw1.registration import app
from homework.hw1.registration import RegistrationForm
# from Module_04.homework.hw1.registration import app


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class TestRegistration(unittest.TestCase):
    email = 'test@example.com'
    phone = 7774442288
    name = 'Тест Т. Т.'
    address = 'Тест Тест Тест'
    index = 666666
    comment = 'Test comment'

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def setUp(self):
        self.app = self.create_app()    

# ===================================================================
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

    def test_invalid_email(self):
        client = self.app.test_client()
        response = client.post('/registration_hw1', data = dict(
            email='testexample.com',
            phone=self.phone,
            name=self.name,
            address=self.address,
            index=self.index,
            comment=self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug("Response status code: %s", response.status_code)

        self.assertIn('email', response.data.decode())
        logging.debug("Response data: %s", response.data.decode())

    def test_no_email(self):
        client = self.app.test_client()
        response = client.post('/registration_hw1', data = dict(
            phone=self.phone,
            name=self.name,
            address=self.address,
            index=self.index,
            comment=self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug("Response status code: %s", response.status_code)

        self.assertIn('email', response.data.decode())
        logging.debug("Response data: %s", response.data.decode())

# ===================================================================
    def test_valid_phone(self):
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

    def test_length_phone(self):
        client = self.app.test_client()
        response = client.post('/registration_hw1', data = dict(
            email=self.email,
            phone=999999999,
            name=self.name,
            address=self.address,
            index=self.index,
            comment=self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug("Response status code: %s", response.status_code)

        self.assertIn('phone', response.data.decode())
        logging.debug("Response data: %s", response.data.decode())

    def test_no_phone(self):
        client = self.app.test_client()
        response = client.post('/registration_hw1', data = dict(
            email=self.email,
            name=self.name,
            address=self.address,
            index=self.index,
            comment=self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug("Response status code: %s", response.status_code)

        self.assertIn('phone', response.data.decode())
        logging.debug("Response data: %s", response.data.decode())

# ===================================================================
    def test_valid_name(self):
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

    def test_wrong_name(self):
        client = self.app.test_client()
        response = client.post('/registration_hw1', data = dict(
            email=self.email,
            phone=self.phone,
            name='Тест Тестович',
            address=self.address,
            index=self.index,
            comment=self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug("Response status code: %s", response.status_code)

        self.assertIn('name', response.data.decode())
        logging.debug("Response data: %s", response.data.decode())
    
    def test_no_name(self):
        client = self.app.test_client()
        response = client.post('/registration_hw1', data = dict(
            email=self.email,
            phone=self.phone,
            address=self.address,
            index=self.index,
            comment=self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug("Response status code: %s", response.status_code)

        self.assertIn('name', response.data.decode())
        logging.debug("Response data: %s", response.data.decode())

# ===================================================================
    def test_valid_address(self):
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
        
    def test_no_address(self):
        client = self.app.test_client()
        response = client.post('/registration_hw1', data = dict(
            email=self.email,
            phone=self.phone,
            name=self.name,
            index=self.index,
            comment=self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug("Response status code: %s", response.status_code)

        self.assertIn('address', response.data.decode())
        logging.debug("Response data: %s", response.data.decode())

# ===================================================================
    def test_valid_index(self):
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

    def test_wrong_index(self):
        client = self.app.test_client()
        response = client.post('/registration_hw1', data = dict(
            email=self.email,
            phone=self.phone,
            name=self.name,
            address=self.address,
            index=999999999,
            comment=self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug("Response status code: %s", response.status_code)

        self.assertIn('index', response.data.decode())
        logging.debug("Response data: %s", response.data.decode())

        


if __name__ == '__main__':
    unittest.main()
