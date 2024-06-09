import logging, unittest

from block_errors import BlockErrors


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class TestBlockErrors(unittest.TestCase):
    
    def test_ignor_error(self):
        """Ошибка игнорируется."""
        ignor_errors = {ZeroDivisionError, TypeError}
        with BlockErrors(ignor_errors):
            a = 1 / 0
        logging.debug(
            f'Выполнено без ошибок (ошибка игнорируется)!'
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
    
    def test_external_error(self):
        """
        Ошибка прокидывается выше во внутреннем блоке и 
        игнорируется во внешнем.
        """
        try:
            external_ignor = {TypeError}
            with BlockErrors(external_ignor):
                internal_ignor = {ZeroDivisionError}
                with BlockErrors(internal_ignor):
                    a = 1 / '0'
                logging.debug('Ошибка прокидывается во внешний блок')
        except Exception as exc:
            self.fail(f'Ошибка не игнорируется во внешнем блоке: {type(exc).__name__}')
        logging.debug('Внешний блок: выполнено без ошибок.')
            




if __name__ == '__main__':
    unittest.main()
