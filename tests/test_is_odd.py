import unittest
from is_even import is_odd


class TestEven(unittest.TestCase):
    def test_even_true(self):
        self.assertTrue(is_odd(3))

    def test_even_false(self):
        self.assertFalse(is_odd(4))


if __name__ == "__main__":
    unittest.main()
