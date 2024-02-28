from python_code.InsufficientFundError import InsufficientFundError
from python_code.InvalidAmountError import InvalidAmountError
from python_code.InvalidPinError import InvalidPinError


class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        pass
        if amount <= 0:
            raise InvalidAmountError("invalid amount")
        self.balance += amount

    def withdraw(self, amount, pin):
        pass
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        if amount > self.balance:
            raise InsufficientFundError("Insufficient funds")
        if self.pin != pin:
            raise InvalidPinError("Invalid pin")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def validate(self, enter_pin):
        if enter_pin != self._pin and enter_pin != 4:
            raise ValueError("invalid pin")
        return self._pin == enter_pin

    def get_account_number(self):
        return self.account_number

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, pin):
        self._pin = pin
