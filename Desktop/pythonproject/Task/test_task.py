from unittest import TestCase

from classtasks.task import letters_digits


class Test(TestCase):
    def test_letters_digits(self):
        words = "i love coding 123"
        self.assertEqual("LETTERS 11 DIGITS 3",  letters_digits(words))
