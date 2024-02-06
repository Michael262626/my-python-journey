from unittest import TestCase

import Phone_book_app


class Test(TestCase):
    def test_add_contact(self):
        name = "michael"
        number = "07066993421"
        result = Phone_book_app.add_contact(name, number)

        self.assertEqual('michael', result)
        self.assertEqual('07066993421', result)


    def test_display_contacts(self):
        self.fail()

    def test_search_contact(self):
        self.fail()

    def test_check_errors(self):
        self.fail()

    def test_delete_contact(self):
        self.fail()

    def test_edit_contact(self):
        self.fail()

    def test_main(self):
        self.fail()
