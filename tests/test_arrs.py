import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_get_negative_index(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "default_value"), "default_value")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_my_slice_empty_list(self):
        self.assertEqual(arrs.my_slice([], 1, 3), [])

    def test_get_index_out_of_bounds(self):
        self.assertEqual(arrs.get([1, 2, 3], 5, "default"), "default")

    def test_get_negative(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "default"), "default")


    def test_get_within_bounds(self):
        # Test when the index is within the bounds of the array
        self.assertEqual(arrs.get([1, 2, 3], 1, "default"), 2)


    def test_slice_start_none(self):
        # Test when start is None
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], None, 3), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], None), [1, 2, 3])