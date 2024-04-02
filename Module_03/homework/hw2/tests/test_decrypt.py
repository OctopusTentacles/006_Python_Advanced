""" Тест для задачи 2 - Дешифратор """


import unittest

from decrypt import decrypt


class TestDecrypt(unittest.TestCase):

    def test_one_dot(self):
        encrypted_text = "абра-кадабра."
        expected_decrypted_text = "абра-кадабра"
        self.assertEqual(decrypt(encrypted_text, expected_decrypted_text))