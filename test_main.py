from unittest import TestCase
import main
from main import multiple_of_three, average_numbers




class Test(TestCase):
    def test_get_length_of_a_list(self):
        num = [1, 2, 3, 5, 6, 7]
        result = 6
        actual = main.get_length_of_a_list(num)
        self.assertEqual(actual, result)

    def test_sum_even_positions(self):
        num = [1, 2, 3, 5, 6]
        result = 10
        actual = main.sum_even_positions(num)
        self.assertEqual(actual, result)

    def test_sum_odd_positions(self):
        num = [1, 2, 3, 5, 6]
        result = 10
        actual = main.sum_odd_positions(num)
        self.assertEqual(actual, result)

    def test_multiple_of_three(self):
        num = [1, 2, 3, 5, 6, 5, 7]
        result = 35
        actual = main.multiple_of_three(num)
        self.assertEqual(actual, result)

    def test_average_numbers(self):
        num = [1, 2, 3, 5, 6, 5,]
        result = 3.67
        actual = average_numbers(num)
        self.assertEqual(actual, result)

    def test_largest_elements(self):
        num = [1, 2, 3, 5, 6]
        result = 6
        actual = main.largest_elements(num)
        self.assertEqual(actual, result)

    def test_smallest_elements(self):
        num = [1, 2, 3, 5, 6]
        result = 1
        actual = main.smallest_elements(num)
        self.assertEqual(actual, result)

    def test_that_function_list_of_strings(self):
        strings = ['hannah', 'bob', 'cash', 'dee', 'elsa', 'frank']
        expected = ['hannah', 'bob']
        actual = main.that_function_list_of_strings(strings)
        self.assertEqual(actual, expected)



