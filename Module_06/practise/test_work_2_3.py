import unittest
import json

from flask import Flask
from flask.testing import FlaskClient
from work_2_3 import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.testing = True

    
    def test_arithmetic_error(self):
        response = self.client.post(
            '/calculate', json={'expression': 'int("string")'}
        )
        self.assertEqual(response.status_code, 500)
        self.assertIn('Arithmetic Error', response.json['error'])


    def test_zero_division_error(self):
        response = self.client.post(
            '/calculate', json={'expression': '1 / 0'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('Zero Division Error', response.json['error'])

    
    def test_floating_point_error(self):
        response = self.client.post(
            '/calculate', json={'expression': 'float("inf") * float("inf")'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('Floating Point Error', response.json['error'])


    def test_overflow_error(self):
        response = self.client.post(
            '/calculate', json={'expression': '1e308 * 1e308'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('Overflow Error', response.json['error'])
    

if __name__ == '__main__':
    unittest.main()