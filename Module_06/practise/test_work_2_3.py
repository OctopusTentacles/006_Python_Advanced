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
        response


    def test_zero_division_error(self):

    
    def test_floating_point_error(self):


    def test_overflow_error(self):
    



if __name__ == '__main__':
    unittest.main()