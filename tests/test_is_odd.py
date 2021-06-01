import unittest
from is_even import is_even as ie


class TestEven(unittest.TestCase):
    def test_even_true(self):
        self.assertTrue(ie.is_odd(3))

    def test_even_false(self):
        self.assertFalse(ie.is_odd(4))


if __name__ == "__main__":
    unittest.main()
