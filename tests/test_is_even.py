import unittest
from is_even import is_even 


class TestEven(unittest.TestCase):
    def test_even_true(self):
        self.assertTrue(is_even(2))

    def test_even_false(self):
        self.assertFalse(is_even(7))


if __name__ == "__main__":
    unittest.main()
