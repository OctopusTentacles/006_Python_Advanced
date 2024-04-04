""" Тест для Учета финансов. """


import unittest

from accounting import app


class TestAccounting(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Инициализация данных
        cls.app = app.test_client()
        cls.storage = {
            2023: {1: {1: 100, 'month_total': 100}, 'year_total': 100},
            2024: {4: {4: 200, 5: 300, 'month_total': 500}, 'year_total': 500}
        }

    def test_add(self):
        responce = self.app.get('/add/20240406/200')
        self.assertEqual(responce.status_code, 200)