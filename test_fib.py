import unittest
from fib import fib

class TestFib(unittest.TestCase):
    def test_zero(self):
        res = fib(0)
