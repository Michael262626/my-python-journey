import unittest
import double_array


class MyTestCase(unittest.TestCase):
    def test_something(self):
        elements = [4, 5, 8]
        result = [0, 0, 0, 0, 0, 0]
        self.assertEqual(result, double_array.double_list_array(elements))
