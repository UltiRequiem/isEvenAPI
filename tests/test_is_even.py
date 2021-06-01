import unittest
from is_even import is_even as ie

class TestEven(unittest.TestCase):
    def test_even_true(self):
        self.assertTrue(ie.is_even(2))

    def test_even_false(self):
        self.assertFalse(ie.is_even(7))



if __name__ == "__main__":
    unittest.main()
