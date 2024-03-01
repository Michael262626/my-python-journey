import sys

from python_code import bank
from python_code.IncorrectAccountNumberError import IncorrectAccountNumberError
from python_code.InvalidPinError import InvalidPinError
from bank import BankApp

def display_menu():
    main_menu = """
    1. Register Account
    2. Deposit
    3. Withdraw
    4. Transfer
    5. Check Balance
    6. Close Account
    7. Exit..."""

    return main_menu


def bank_app(uba_bank: BankApp):
    print("Welcome to Uba Bank App 🏦🏦")
    print(display_menu())
    option = input("    Select an option ⁉️ ")
    print()

    match option:
        case "1":
            first_name = input('Enter your first name: ')
            last_name = input('Enter your last name: ')
            pin = input('Enter your pin: ')
            print('Thanks for the provided information ✔')
            the_account = uba_bank.register_account(first_name, last_name, 0, pin)
            print("Registration successful ✔")
            print(f"{first_name} {last_name}, your account number is {the_account.get_account_number()}")
            print()
            bank_app(uba_bank)

        case "2":
            account_number = int(input("Enter your account number: "))
            deposit_amount = int(input("Enter the amount you want to deposit: "))
            try:
                uba_bank.deposit_cash(account_number, deposit_amount)
                print('Deposit successful ✔')
            except ValueError as e:
                print(f"Error: {e}")
            finally:
                bank_app(uba_bank)

        case "3":
            account_number = int(input("Enter your account number: "))
            withdraw_amount = int(input("Enter the amount you want to Withdraw: "))
            pin = input("Enter pin: ")
            try:
                uba_bank.find_account_number(account_number)
                uba_bank.withdraw_cash(account_number, withdraw_amount, pin)
                print('Withdrawal successful ✔')
                print(
                    f"Account Balance :{uba_bank.find_account_number(account_number).check_balance(account_number, pin)}")
            except ValueError as e:
                print(f"Error: {e}")
            finally:
                bank_app(uba_bank)
        case "4":
            from_account_number = int(input('Enter sender account number: '))
            to_account_number = int(input('Enter receiver account: '))
            transfer_amount = int(input('Enter amount: '))
            user_pin = input('Enter pin: ')
            try:
                uba_bank.transfer_cash(from_account_number, to_account_number, transfer_amount, user_pin)
                print('Transfer successful ✔')
            except (ValueError, IncorrectAccountNumberError, InvalidPinError) as e:
                print(f"Error: {e}")
            finally:
                bank_app(uba_bank)
        case "5":
            account_number = int(input('Enter account number: '))
            pin = input('Enter pin: ')
            try:
                balance = uba_bank.check_balance(account_number, pin)
                print(f"Your balance is {balance}")
            except (IncorrectAccountNumberError, InvalidPinError) as e:
                print(f"Error: {e}")
            finally:
                bank_app(uba_bank)
        case "6":
            account_number = int(input('Enter account number: '))
            user_pin = input('Enter pin: ')
            try:
                uba_bank.delete_account(account_number, user_pin)
                print('Account closed successfully ✔')
            except (ValueError, IncorrectAccountNumberError, InvalidPinError) as e:
                print(f"Error: {e}")
            finally:
                bank_app(uba_bank)

        case "7":
            print("Thank you for using Uba Bank App 🏦🏦")
            sys.exit(0)


if __name__ == '__main__':
    bank = BankApp("UBA Bank")
    bank_app(bank)
