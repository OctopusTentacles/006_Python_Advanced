import unittest
import logging
from remote_execution import app


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class RemoteExecution(unittest.TestCase):
    code = print('Hello, World!')
    timeout = 3

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app


    def test_timeout(self):


if __name__ == '__main__':
    unittest.main()
