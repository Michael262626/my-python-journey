contacts = {}


def add_contact(name, numbers):
    contacts[name] = numbers


def display_contacts():
    for name, numbers in contacts.items():
        print(f"Name: {name}\n Number: {numbers}")


def search_contact(name):
    if name in contacts:
        return f"Name: {name}\n Number: {contacts[name]}"
    else:
        return "Not found"


def check_errors():
    for name, numbers in contacts.items():
        if not len(name) > 0:
            print("Error name can not be empty")
        elif not len(numbers) > 0:
            print("Error number can not be empty")
        elif name.isdigit():
            print("Error name cannot contain only digits")
        elif name.isalpha():
            print("Error name cannot contain only letters")


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted")
    else:
        print(f"{name} not found")


def edit_contact(name, new_numbers):
    if name in contacts:
        contacts[name] = new_numbers
        print(f'Edited: {name} to {new_numbers:}')
    else:
        print(f"{name} not found")


def main():
    print(">>>Welcome to Phone Book<<<")
    while True:
        print("\n1. Add a contact: \n2. Search contact: \n3. Delete contact: \n4. Edit a contact:\n5. "
              "display contact:\n6."
              "Exit...")
        choice = input("Enter your choice: ").lower()

        if choice == "1":
            name = input("\nEnter the name of the contact:")
            numbers = input("Enter the phone numbers of the contact:\n")
            add_contact(name, numbers)
            check_errors()
            again = input("\nDo you want to perform more actions? (y/n)\n")
            if again.lower() != "y":
                break
        elif choice == "2":
            name = input("Enter the name of the contact:")
            search_contact(name)

        elif choice == "3":
            name = input("Enter the name of the contacts you want to delete:\n")
            delete_contact(name)
        elif choice == "4":
            name = input("Enter the name of the contacts you want to edit\n")
            new_numbers = input("Enter the new phone number")
            edit_contact(name, new_numbers)
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            print("Thank you for using this app")
            break
        else:
            print("Invalid")


if __name__ == '__main__':
    main()
