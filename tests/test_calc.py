from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_acc():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3,2,5),
    (7,1,8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    assert add(num1,num2) == expected

def test_subtract():
    assert subtract(9,4) == 5

def test_divide():
    assert divide(10,5) == 2

def test_multiply():
    assert multiply(3,2) == 6

def test_bank_set_initial_amount():
    bank_acc = BankAccount(50)
    assert bank_acc.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw():
    bank_acc = BankAccount(50)
    bank_acc.withdraw(20)
    assert bank_acc.balance == 30

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)

])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected



