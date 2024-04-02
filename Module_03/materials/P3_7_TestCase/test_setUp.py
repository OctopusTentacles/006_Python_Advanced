from unittest import TestCase
from models import Student
class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student()
    def test_default_name_is_none(self):
        self.asserIsNone(self.student.name)
    def test_set_invalid_age(self):
        with self.assertRaises(ValueError):
            self.student.set_age(-100)


# Метод assertIsNone проверяет, что значение переменной равно None. 
# Метод assertRaises проверяет, что определённое исключение было вызвано 
# в процессе выполнения программы. Вот перечень наиболее популярных 
# assert-методов:

# assertEqual(a, b)   a == b

# assertNotEqual(a, b)    a != b

# assertTrue(x)   bool(x) is True

# assertFalse(x)  bool(x) is False

# assertIs(a, b)  a is b    
            
# assertIsNot(a, b)   a is not b

# assertIsNone(x) x is None

# assertIsNotNone(x)  x is not None

# assertIn(a, b)  a in b

# assertNotIn(a, b)  a not in b

# assertIsInstance(a, b)  isinstance(a, b)

# assertNotIsInstance(a, b)   not isinstance(a, b)