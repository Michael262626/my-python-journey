import random

from python_code.Account import Account
from python_code.IncorrectAccountNumberError import IncorrectAccountNumberError
from python_code.InvalidPinError import InvalidPinError


class BankApp:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def register_account(self, first_name, second_name, initial_balance, pin):
        account_number = self.generate_account_number
        account_object = Account(account_number, initial_balance, pin)
        self.accounts.append(account_object)
        return account_object

    @property
    def generate_account_number(self):
        return random.randint(1_000_000_000, 1_999_999_999)

    def deposit_cash(self, account_number, amount):
        if self.find_account_number(account_number) is None:
            raise IncorrectAccountNumberError("Account not found")
        account = self.find_account_number(account_number)
        account.deposit(amount)

    def find_account_number(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account

    def withdraw_cash(self, account_number, amount, pin):
        account_num = self.find_account_number(account_number)
        account_num.withdraw(amount, pin)

    def transfer_cash(self, from_account_number, to_account_number, amount, pin):
        from_account = self.find_account_number(from_account_number)
        to_account = self.find_account_number(to_account_number)
        from_account.withdraw(amount, pin)
        to_account.deposit(amount)

    def check_balance(self, account_number):
        if self.find_account_number(account_number) is None:
            raise IncorrectAccountNumberError("Account not found")
        account = self.find_account_number(account_number)
        return account.get_balance()

    def delete_account(self, account_number, pin):
        if self.find_account_number(account_number) is None:
            raise IncorrectAccountNumberError("Account not found")
        account = self.find_account_number(account_number)
        if account.validate(pin) is False:
            raise InvalidPinError("Incorrect pin")
        return account.remove(account_number)
