import logging, unittest

from block_errors import BlockErrors


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class TestBlockErrors(unittest.TestCase):
    
    def test_ignor_error(self):
        """Ошибка игнорируется."""
        ignor_errors = {ZeroDivisionError, TypeError}
        with BlockErrors(ignor_errors):
            a = 1 / '0'
        logging.debug(
            f'Ошибка игнорируется'
        )

    def test_above_error(self):
        """Ошибка прокидывается выше."""
        ignor_errors = {ZeroDivisionError}
        with self.assertRaises(TypeError) as exc:
            with BlockErrors(ignor_errors):
                a = 1 / '0'
                # вызывается TypeError, которого нет в игноре,
                # поэтому TypeError переходит выше где его ловит assertRaises
        logging.debug(
            f'Ошибка прокидывается выше: {type(exc.exception).__name__}'
        )




if __name__ == '__main__':
    unittest.main()
