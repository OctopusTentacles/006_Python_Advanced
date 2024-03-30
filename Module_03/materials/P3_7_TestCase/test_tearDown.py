import time

from unittest import TestCase


class PerformanceTest(TestCase):
    def setUp(self):
        self.start = time.perf_counter()

    def tearDown(self):
        self.end = time.perf_counter()
        print(self.id(), self.end - self.start)

    def test_million_appends(self):
        N = 1_000_000
        lst = []
        for i in range(N):
            lst.append(i)
        self.assertListEqual(lst, list(range(N)))

# time.perf_counter() возвращает текущее время с наибольшим 
# доступным разрешением.

# self.id() выдаст название текущего теста в таком формате: 
# __main__.PerformanceTest.test_million_appends