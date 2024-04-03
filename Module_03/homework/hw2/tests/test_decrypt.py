""" Тест для задачи 2 - Дешифратор """


import unittest

from Module_03.homework.hw2.decrypt import decrypt


class TestDecrypt(unittest.TestCase):

    def test_one_dot(self):
        encrypted_text = 'абра-кадабра.'
        expected_decrypted_text = 'абра-кадабра'
        self.assertEqual(decrypt(encrypted_text), expected_decrypted_text)

    def test_two_dots(self):
        encrypted_text = 'абраа..-кадабра'
        expected_decrypted_text = 'абра-кадабраы'
        self.assertEqual(decrypt(encrypted_text), expected_decrypted_text)




