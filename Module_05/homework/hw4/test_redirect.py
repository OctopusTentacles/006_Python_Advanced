import os
import unittest
from redirect import Redirect


cur_dir = os.path.dirname(__file__)

class TestRedirect(unittest.TestCase):

    def test_redirect_stdout(self):
        with open(os.path.join(cur_dir, 'stdout.txt'), 'w') as f_out,\
            open(os.path.join(cur_dir, 'stderr.txt'), 'w') as f_err:
            with Redirect(stdout=f_out, stderr=f_err):
                print('Это стандартный поток вывода')




if __name__ == '__main__':
    unittest.main()
    # with open('test_results.txt', 'a') as test_file_stream:
    #     runner = unittest.TextTestRunner(stream=test_file_stream)
    #     unittest.main(testRunner=runner)
