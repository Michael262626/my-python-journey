import sys

from python_code import bank
from python_code.IncorrectAccountNumberError import IncorrectAccountNumberError
from python_code.InvalidPinError import InvalidPinError


def display_menu():
    main_menu = """Bank app
    1. Register Account
    2. Deposit
    3. Withdraw
    4. Transfer
    5. Check Balance
    6. Close Account
    7. Exit..."""

    return main_menu


def bank_app():
    uba_bank = bank.BankApp("Uba Bank")
    print("Welcome to Uba Bank App 🏦🏦")
    print(display_menu())
    option = input("    Select an option ⁉️")
    print()

    match option:
        case "1":
            first_name = input('Enter your first name: ')
            second_name = input('Enter your last name: ')
            pin = input('Enter your pin: ')
            print('Thanks for the provided information ✔ ️')
            the_account = uba_bank.register_account(first_name, second_name, 0, pin)
            print("Registration went successfully ✔")
            print(f"{first_name} {second_name} your account number is {the_account.get_account_number()}")
            print()
            bank_app()

        case "2":
            account_number = input("Enter your account number")
            deposit_amount = input("Enter the amount you want to deposit")
            try:
                print('verifying...🔃 \ntransaction was successful ✔✔')
                uba_bank.deposit_cash(account_number, deposit_amount)
            except ValueError as e:
                print(f"{e}")
                pass
            finally:
                bank_app()

        case "3":
            account_number = input('Enter your account number')
            withdraw_amount = input('Enter the amount you want to withdraw')
            user_pin = input('Enter pin')
            try:
                print('Verifying...🔃')
                uba_bank.withdraw_cash(account_number, withdraw_amount, user_pin)
                print('withdrawal went successfully ✔✔')
            except ValueError as e:
                print(f"{e}")
                pass
            finally:
                bank_app()

        case "4":
            from_account_number = input('Enter sender account number')
            to_account_number = input('Enter receiver account')
            transfer_amount = input('Enter amount')
            user_pin = input('Enter pin')
            try:
                print('Verifying')
                uba_bank.transfer_cash(from_account_number, to_account_number, transfer_amount, user_pin)
                print('Verifying....🔃\ntransferred successfully ✔✔')
            except ValueError as e:
                print(f"{e}")
                pass
            finally:
                bank_app()

        case "5":
            account_number = input('Enter account number: ')
            pin = input('Enter pin: ')
            try:
                account = uba_bank.check_balance(int(account_number), pin)
                print(f"Verifying🔃\nAccount found\nYour balance is {account}")
            except ValueError:
                print('Invalid input')
            except IncorrectAccountNumberError as e:
                print(f"{e}")
            except InvalidPinError as e:
                print(f'{e}')
            finally:
                bank_app()

        case "6":
            account_number = input('Enter account number')
            user_pin = input('Enter pin')
            try:
                print('Verifying🔃')
                uba_bank.delete_account(account_number, user_pin)
            except ValueError as e:
                print(f"{e}")
                pass
            finally:
                bank_app()

        case "7":
            sys.exit(0)


bank_app()
