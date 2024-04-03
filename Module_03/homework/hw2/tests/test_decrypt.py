""" Тест для задачи 2 - Дешифратор """


import unittest

from Module_03.homework.hw2.decrypt import decrypt


class TestDecrypt(unittest.TestCase):

    # отдельные функции____________________________________________________:
    def test_one_dot(self):
        encrypted_text = 'абра-кадабра.'
        expected_decrypted_text = 'абра-кадабра'
        self.assertEqual(decrypt(encrypted_text), expected_decrypted_text)

    def test_two_dots(self):
        encrypted_text = 'абраа..-кадабра'
        expected_decrypted_text = 'абра-кадабраы'
        self.assertEqual(decrypt(encrypted_text), expected_decrypted_text)


    # контекст-менеджер subTest___________________________________________:
    def test_decrypt(self):
        encrypted_texts = [
            ('абра-кадабра.', 'абра-кадабра'),
            ('абраа..-кадабра', 'абра-кадабра'),
            (' абраа..-.кадабра', ' абра-кадабра'),
            ('абра--..кадабра', 'абра-кадабра'),
            ('абрау...-кадабра', 'абра-кадабра'),
            ('абра........', ''),
            ('абр......a.', 'a'),
            ('1..2.3', '23'), 
            ('.', ''),
            ('1.......................', '')
        ]
        for encrypted_text, expected_text in encrypted_texts:
            with self.subTest(encrypted_text=encrypted_text):
                decrypted_text = decrypt(encrypted_text)
                self.assertEqual(decrypted_text, expected_text)


