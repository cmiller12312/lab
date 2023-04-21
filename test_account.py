import pytest
from account import *

class Test():
    def setup_method(self):
        self.p1 = Account('john')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'john'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(-500) == False
        assert self.p1.deposit(0) == False
        assert self.p1.deposit(300) == True

    def test_withdraw(self):
        assert self.p1.withdraw(-300) == False
        assert self.p1.withdraw(0) == False
        self.p1.deposit(300)
        assert self.p1.withdraw(300) == True
        assert self.p1.withdraw(600) == False