import logging, unittest

from block_errors import BlockErrors


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class TestBlockErrors(unittest.TestCase):
    
    def test_ignor_error(self):
        """Ошибка игнорируется."""
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            a = 1 / 0
        print('Выполнено без ошибок')




if __name__ == '__main__':
    unittest.main()
