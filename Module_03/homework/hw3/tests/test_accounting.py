""" Тест для Учета финансов. """


import unittest

from accounting import app
from accounting import storage
# from Module_03.homework.hw3.accounting import app
# from Module_03.homework.hw3.accounting import storage


class TestAccounting(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.app = app.test_client()

        # Инициализация данных
        storage.update({
            2023: {1: {1: 100, 'month_total': 100}, 'year_total': 100},
            2024: {4: {4: 200, 5: 300, 'month_total': 500}, 'year_total': 500}
        })

    def test_add(self):
        responce = self.app.get('/add/20240506/200')
        self.assertEqual(responce.status_code, 200)