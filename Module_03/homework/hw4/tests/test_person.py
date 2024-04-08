""" Тестирование файла person.py """



import datetime
import unittest

# from person import Person
from Module_03.homework.hw4.person import Person


class TestPerson(unittest.TestCase):
    name = 'Boby'
    birth_year = 2000
    address = '17 Baker str.'
    person = Person(name, birth_year, address)

    def test_get_age(self):
        current_year = datetime.datetime.now().year
        expected_age = current_year - self.birth_year
        self.assertEqual(self.person.get_age(), expected_age)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), self.name)

    def test_set_name(self):
        new_name = self.person.set_name('Scooby')
        self.assertEqual(self.person.get_name(), new_name)
