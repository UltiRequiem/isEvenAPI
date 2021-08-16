import unittest
from is_even import is_even as ie


class TestEven(unittest.TestCase):
    def test_ad(self):
        self.assertIsInstance(ie.ad(2), str)

    def test_ad_without_number(self):
        self.assertIsInstance(ie.ad_without_number(), str)


if __name__ == "__main__":
    unittest.main()
