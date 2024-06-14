import os
import logging
import sys
import unittest

from redirect import Redirect


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)

# текущая дирректория для файлов:
cur_dir = os.path.dirname(__file__)


class TestRedirect(unittest.TestCase):

    def setUp(self):
        """Сохраняем оригинальные значения потоков."""
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr

    def test_redirect_stdout(self):
        with open(os.path.join(cur_dir, 'stdout.txt'), 'w') as f_out:
            with Redirect(stdout=f_out):
                print('Это стандартный поток вывода')
                # проверяем, что sys.stdout был перенаправлен:
                self.assertNotEqual(sys.stdout, self.original_stdout)
                logging.debug(
                    f'\nCurrent stdout: {sys.stdout}\n'
                    f'Original stdout: {self.original_stdout}'
                )
        # выход из контекст-менеджера,
        # проверяем что sys.stdout восстановлен:
        self.assertEqual(sys.stdout, self.original_stdout)
        logging.debug(
            f'\nstdout: {sys.stdout}\n'
            f'Original stdout: {self.original_stdout}'
        )
    
    def test_redirect_stderr(self):
        with open(os.path.join(cur_dir, 'stderr.txt'), 'w') as f_err:
            with Redirect(stderr=f_err):
                try: 
                    raise Exception('Это стандартный поток ошибок')
                except Exception:
                    # Записываем трассировку стека в stderr:
                    import traceback
                    traceback.print_exc(file=sys.stderr)
                    # проверяем, что sys.stderr был перенаправлен:
                    self.assertNotEqual(sys.stderr, self.original_stderr)
                    logging.debug(
                        f'\nCurrent stderr: {sys.stderr}\n'
                        f'Original stderr: {self.original_stderr}'
                    )

                

        # выход из контекст-менеджера,
        # проверяем что sys.stdout восстановлен:
        self.assertEqual(sys.stderr, self.original_stderr)
        logging.debug(
            f'\nstderr: {sys.stderr}\n'
            f'Original stderr: {self.original_stderr}'
        )



if __name__ == '__main__':
    unittest.main()
    # with open('test_results.txt', 'a') as test_file_stream:
    #     runner = unittest.TextTestRunner(stream=test_file_stream)
    #     unittest.main(testRunner=runner)
