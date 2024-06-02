
import json
import logging
import unittest

from remote_execution import app


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)


class RemoteExecution(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def test_timeout(self):
        response = self.client.post(
            '/run_code', 
            data = dict(
                code = 'import time; print("Start"); time.sleep(5), print("Stop")',
                timeout = 3
            )
        )
        self.assertEqual(response.status_code, 200)
        logging.debug("Response status code: %s", response.status_code)
        
        data = json.loads(response.data)
        self.assertIsNone(data['output'])
        self.assertEqual(data['error'], 'Execution timed out')
        





if __name__ == '__main__':
    unittest.main()
