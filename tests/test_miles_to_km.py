import unittest

from solutions.miles_to_km import miles_to_km


class Test(unittest.TestCase):
    def test_miles_to_km(self):
        self.assertEqual(miles_to_km(1), 1.61)

    def test_miles_to_km_dict_type(self):
        with self.assertRaises(TypeError):
            miles_to_km({"a": 1, "b": 2})

    def test_miles_to_km_list_type(self):
        with self.assertRaises(TypeError):
            miles_to_km([1, 2, 3])
