import unittest
from app import add_numbers


class TestAddition(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(add_numbers(0, 5), 5)


if __name__ == "__main__":
    unittest.main()
