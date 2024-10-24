import unittest

from solutions.km_to_miles import km_to_miles


class Test(unittest.TestCase):
    def test_km_to_miles(self):
        # self.assertEqual(km_to_miles(1), 0.62)
        self.assertEqual(km_to_miles(1), 62)

    def test_km_to_miles_dict_type(self):
        with self.assertRaises(TypeError):
            km_to_miles({"a": 1, "b": 2})

    def test_km_to_miles_list_type(self):
        with self.assertRaises(TypeError):
            km_to_miles([1, 2, 3])
