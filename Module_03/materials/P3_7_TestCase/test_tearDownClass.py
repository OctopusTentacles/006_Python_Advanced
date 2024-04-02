import time

from unittest import TestCase


class PerformanceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file = open("test_log.txt", "a")
    def setUp(self):
        self.start = time.perf_counter()
    def test_million_appends(self):
        N = 1_000_000
        lst = []
        for i in range(N):
            lst.append(i)
        self.assertListEqual(lst, list(range(N)))
    def test_sum_of_numbers(self):
        N = 1_000_000
        self.assertEqual(sum(range(N)), N * (N + 1) // 2)
    def tearDown(self):
        self.end = time.perf_counter()
        print(self.id(), self.end - self.start, file=self.file)
    @classmethod
    def tearDownClass(cls):
        cls.file.close()

# setUp запускается перед каждым тестом;
# tearDown запускается после каждого теста;
# setUpClass запускается перед всеми тестами;
# tearDownClass запускается после всех тестов.