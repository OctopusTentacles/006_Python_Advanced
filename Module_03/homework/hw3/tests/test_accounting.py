""" Тест для Учета финансов. """


import unittest

# from accounting import app
# from accounting import storage
from Module_03.homework.hw3.accounting import app
from Module_03.homework.hw3.accounting import storage
from Module_03.homework.hw3.accounting import add


class TestAccounting(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.app = app.test_client()

        # Инициализация данных
        storage.update({
            2023: {1: {1: 100, 'month_total': 100}, 'year_total': 100},
            2024: {4: {4: 200, 5: 300, 'month_total': 500}, 'year_total': 500}
        })

    def test_add_correct(self):
        responce = self.app.get('/add/20240506/200')
        self.assertEqual(responce.status_code, 200)
    
    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            add('yymmdd')

    # для этого теста в основном пролижении функции add()
    # закомментируем блок try-ecxept
    def test_add_value_error(self):
        with self.assertRaises(ValueError):
            add('20240232', 200)


# ===========================================================================
    def test_calculate_year(self):
        responce = self.app.get('/calculate/2023')  # 100
        self.assertEqual(responce.status_code, 200)

    # если в `storage` ничего нет и блок try-ecxept закомментирован - ERROR.
    def test_calculate_year_empty_storage(self):
        storage.clear()
        response = self.app.get('/calculate/2023')  
        self.assertEqual(response.status_code, 500)
    # если в `storage` ничего нет и блок try-ecxept в работе - 
    def test_calculate_year_empty_storage_with_try(self):
        storage.clear()
        response = self.app.get('/calculate/2023')
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('В эту дату нет трат!', response_text)



    def test_calculate_month(self):
        responce = self.app.get('/calculate/2023/01')   #100
        self.assertEqual(responce.status_code, 200)