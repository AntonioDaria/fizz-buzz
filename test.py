import unittest

from fizzbuzz import *

class Fizzbuzz(unittest.TestCase):

    def test_is_divisible_by_three_return_true(self):
        self.assertEqual(is_divisible_by_three(3), True)


if __name__ == "__main__":
  unittest.main()
