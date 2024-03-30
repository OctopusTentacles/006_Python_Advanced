import unittest

from social_status import get_social_status


class TestSocialStatus(unittest.TestCase):

    def test_can_get_child_age(self):
        age = 8
        expected_res = 'child'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_cannot_pass_str_as_age(self):
        age = 'old'
        with self.assertRaises(ValueError):
            get_social_status(age)

    def test_negative_age(self):
        age = -8
        expected_res = 'child'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)
