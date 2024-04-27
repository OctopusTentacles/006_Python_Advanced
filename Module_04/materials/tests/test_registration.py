import unittest
from flask_testing import TestCase
from flask_wtform import app
# from forms import RegistrationForm


class BaseRegistrationTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.valid_data = {
        #     'email': 'test@example.com',
        #     'phone': '1234567890',
        #     'name': 'Ivanov Ivan',
        #     'address': 'Village Ave. My Home',
        #     'index': 001001,
        #     'comment': 'Test comment'
        # }
        pass

    def create_app(self):
        return app
    
    def test_email_required(self):
        response = self.client.post('/registration', data = dict(
            phone='1234567890',
            name='Ivanov Ivan',
            address='Village Ave. My Home',
            index=12345,
            comment='Test comment'
        ))
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.data.decode())

    def test_phone_required(self):
        ...