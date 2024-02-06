from unittest import TestCase, main

from PhoneBook import PhoneBokkApp
from PhoneBook.PhoneBokkApp import add_contact, delete_contact, edit_contact, search_contact, display_contacts, \
    check_errors


class Test(TestCase):
    def setUp(self):
        self.contacts = {}

    def test_add_contact(self):
        self.contacts = {
            "Michael": "1234567890",
            "Kume": "9876543210"
        }
        add_contact("Michael", "1234567890")
        add_contact("Kume", "9876543210")
        self.assertEqual(self.contacts, {
            "Michael": "1234567890",
            "Kume": "9876543210"
        })

    def test_search_contact(self):
        self.contacts = {
            "Michael": "1234567890",
            "Kume": "9876543210"
        }
        self.assertEqual(search_contact("Michael"), "Name: Michael\n Number: 1234567890")
        self.assertEqual(search_contact("Kume"), "Name: Kume\n Number: 9876543210")
        self.assertEqual(search_contact("Not exist"), "Not found")

    def test_display_contacts(self):
        self.contacts = {
            "Michael": "1234567890",
            "Jane": "9876543210"
        }
        display_contacts()
        self.assertEqual(self.contacts, {
            "Michael": "1234567890",
            "Jane": "9876543210"
        })

    def test_delete_contact(self):
        self.contacts = {
            "John": "1234567890",
            "Jane": "9876543210"
        }
        result = "John not found"
        actual = PhoneBokkApp.delete_contact("John")
        self.assertEqual(actual, result)

    def test_edit_contact(self):
        self.contacts = {
            "Michael": "1234567890",
            "Jane": "9876543210"
        }

        actual = PhoneBokkApp.edit_contact("Michael", "09876543210")
        result = {"Michael": "09876543210",
                  "Jane": "9876543210"}
        self.assertEqual(actual, result)
