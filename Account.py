from python_code.InsufficientFundError import InsufficientFundError
from python_code.InvalidAmountError import InvalidAmountError
from python_code.InvalidPinError import InvalidPinError


class Account:
    def __init__(self, first_name, second_name, account_number, balance, pin):
        self._account_number = account_number
        self._balance = balance
        self.pin = pin
        self.first_name = first_name
        self.second_name = second_name

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("invalid amount")
        self._balance += amount

    def withdraw(self, amount, pin):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise InsufficientFundError("Insufficient funds")
        if self.pin != pin:
            raise InvalidPinError("Invalid pin")
        self._balance -= amount

    def get_balance(self, pin):
        if self.pin == pin:
            return self._balance
        raise InvalidPinError("Incorrect pin.")

    def validate(self, enter_pin):
        if self._pin != enter_pin and enter_pin != 4:
            raise ValueError("invalid pin")
        return self._pin == enter_pin

    def get_account_number(self):
        return self._account_number

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, pin):
        self._pin = pin
