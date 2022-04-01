import unittest
from is_even import adverstiment


class TestEven(unittest.TestCase):
    def test_ad(self):
        self.assertIsInstance(adverstiment(), str)
