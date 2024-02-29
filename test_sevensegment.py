from unittest import TestCase

from python_code.InvalidInputError import InvalidInputError
from python_code.sevensegment import segment, first_method, second_method, third_method, fifth_method, fourth_method, \
    is_on


class Test(TestCase):
    def test_shape(self):
        first = '1'
        self.assertEqual('# # # #', first_method(first))

    def test_shape1(self):
        second = '0000001'
        self.assertEqual('# # # #', second_method(second))

    def test_shape3(self):
        third = '01000101'
        self.assertEqual('#     #', fourth_method(third))

    def test_input(self):
        fourth = '123456'
        with self.assertRaises(InvalidInputError):
            self.assertEqual('#     #', fifth_method(fourth))
