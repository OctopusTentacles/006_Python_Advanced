import unittest

from Module_04.materials.flask_wt_form import app

from Module_04.materials.flask_wt_form import RegistrationForm


class BaseRegistrationTest(unittest.TestCase):
    email = 'test@example.com'
    phone = 1234567890
    name = 'Ivanov Ivan'
    address = 'Village Ave. My Home'
    index = 222111
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
        self.assertIn('email', response.data.decode())

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
        self.assertIn('phone', response.data.decode())


if __name__ == '__main__':
    unittest.main()