import unittest
from char import *

class TestChar(unittest.TestCase):
    def test_is_lower_101_1(self):
        self.assertTrue(is_lower_101('a'))

    def test_is_lower_101_2(self):
        self.assertFalse(is_lower_101('M'))

    def test_is_lower_101_3(self):
        self.assertTrue(is_lower_101('o'))

    def test_char_rot_1(self):
        self.assertTrue(char_rot_13('a'), 'n')

    def test_char_rot_2(self):
        self.assertTrue(char_rot_13('d'), 'q')

    def test_char_rot_3(self):
        self.assertTrue(char_rot_13('D'), 'Q')

if __name__ == '__main__':
   unittest.main()

