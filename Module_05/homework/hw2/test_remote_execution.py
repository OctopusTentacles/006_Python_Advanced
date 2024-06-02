
import json
import logging
import unittest

from remote_execution import app


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class RemoteExecution(unittest.TestCase):
    code = ''
    timeout = None

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def setUp(self):
        self.app = self.create_app()

    def test_timeout(self):
        """Тайм-аут ниже, чем время исполнения."""

        client = self.app.test_client()
        response = client.post('/run_code', data = dict(
                code = 'print("Hello, World!")',
                timeout = 0.0001
            )
        )
        self.assertEqual(response.status_code, 200)
        logging.debug("Response status code: %s", response.status_code)
        
        self.assertIn('error: Execution time out!', json.loads(response.data))
        logging.debug('Response data: %s', response.data.decode())




if __name__ == '__main__':
    unittest.main()
