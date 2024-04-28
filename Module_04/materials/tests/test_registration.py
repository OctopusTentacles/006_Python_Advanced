import unittest

from Module_04.materials.flask_wt_form import app

from Module_04.materials.flask_wt_form import RegistrationForm


class BaseRegistrationTest(unittest.TestCase):
    email = 'test@example.com',
    phone = '1234567890',
    name = 'Ivanov Ivan',
    address = 'Village Ave. My Home',
    index = 001001,
    comment = 'Test comment'

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


if __name__ == '__main__':
    unittest.main()