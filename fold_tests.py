import unittest
from fold import *

class TestCases(unittest.TestCase):
    def test_sum_1(self):
        m = [4, 5]
        self.assertEqual(sum(m), 9)

    def test_sum_2(self):
        m = [1, 5, 4, 50]
        self.assertEqual(sum(m), 60)


    def test_small1(self):
        m = [4, 5, 0 ,2, 1]
        self.assertEqual(index_of_smallest(m), 2)

    def test_small2(self):
        m = [10, 0, 1, 4, 5, 0 ,2, 1]
        self.assertEqual(index_of_smallest(m), 1)

  


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

