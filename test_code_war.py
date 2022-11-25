from unittest import TestCase

from code_war import returns_odd


class Test(TestCase):
    def test_returns_odd(self):
        x = [2, 4, 6, 7, 8, 10]
        self.assertEqual(returns_odd(x), 7)
