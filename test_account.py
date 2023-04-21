import unittest
from account import *


class MyTestCase(unittest.TestCase):
    def test_deposit(self):
        t = Account('John')
        self.assertFalse(t.deposit(-500))
        self.assertFalse(t.deposit(0))
        self.assertTrue(t.deposit(300))

    def test_withdraw(self):
        t = Account('john')
        self.assertFalse(t.withdraw(-500))
        self.assertFalse(t.withdraw(0))
        t.deposit(300)
        self.assertTrue(t.withdraw(300))
        self.assertFalse(t.withdraw(600))

    def test_init(self):
        t = Account('john')

        self.assertEqual(t.get_name(), 'john')
        self.assertEqual(t.get_balance(), 0)

if __name__ == '__main__':
    unittest.account()
