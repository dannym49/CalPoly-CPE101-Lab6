import unittest
from string_101 import *

class TestString(unittest.TestCase):
    def test_str_rot_13_1(self):
        self.assertEqual(str_rot_13('ab'), 'no')

    def test_str_rot_13_2(self):
        self.assertEqual(str_rot_13('DE'), 'QR')

    def test_str_translate_101_1(self):
        self.assertEqual(str_translate_101('abcdabcda', 'a', 'i'), 'ibcdibcdi')

    def test_str_translate_101_2(self):
        self.assertEqual(str_translate_101('i like icecream', 'i', 'z'), 'z lzke zcecream')


if __name__ == '__main__':
   unittest.main()

