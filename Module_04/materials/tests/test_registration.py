import unittest
import logging

from Module_04.materials.flask_wt_form import app

from Module_04.materials.flask_wt_form import RegistrationForm


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class BaseRegistrationTest(unittest.TestCase):
    email = 'test@example.com'
    phone = 1234567890
    name = 'Ivanov Ivan'
    address = 'Village Ave. My Home'
    index = 'A'
    comment = 'Test comment'

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def setUp(self):
        self.app = self.create_app()    

    def test_email_required(self):
        client = self.app.test_client()
        response = client.post('/registration', data = dict(
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


    def test_phone_required(self):
        client = self.app.test_client()
        response = client.post('/registration', data = dict(
            email = self.email,
            name = self.name,
            address = self.address,
            index = self.index,
            comment = self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug('Response status code: %s', response.status_code)

        self.assertIn('phone', response.data.decode())
        logging.debug('Response data: %s', response.data.decode())


    def test_name_required(self):
        client = self.app.test_client()
        response = client.post('/registration', data = dict(
            email = self.email,
            phone = self.phone,
            address = self.address,
            index = self.index,
            comment = self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug('Response status code: %s', response.status_code)

        self.assertIn('name', response.data.decode())
        logging.debug('Response data: %s', response.data.decode())


    def test_address_required(self):
        client = self.app.test_client()
        response = client.post('/registration', data = dict(
            email = self.email,
            phone = self.phone,
            name = self.name,
            index = self.index,
            comment = self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug('Response status code: %s', response.status_code)

        self.assertIn('address', response.data.decode())
        logging.debug('Response data: %s', response.data.decode())


    def test_index_required(self):
        client = self.app.test_client()
        response = client.post('/registration', data = dict(
            email = self.email,
            phone = self.phone,
            name = self.name,
            index = self.index,
            address = self.address,
            comment = self.comment
        ))
        self.assertEqual(response.status_code, 400)
        logging.debug('Response status code: %s', response.status_code)

        self.assertIn('index', response.data.decode())
        logging.debug('Response data: %s', response.data.decode())

    
    def test_valid_index(self):
        client = self.app.test_client()
        response = client.post('/registration', data = dict(
        email=self.email,
        phone=self.phone,
        name=self.name,
        index=123456,  # Указываем валидный индекс
        address=self.address,
        comment=self.comment
    ))
        # Ожидаем успешный статус код
        self.assertEqual(response.status_code, 200)
        logging.debug('Response status code: %s', response.status_code)





if __name__ == '__main__':
    unittest.main()