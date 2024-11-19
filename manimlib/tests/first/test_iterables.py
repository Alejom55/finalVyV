import unittest
import numpy as np
from colour import Color
from manimlib.utils.iterables import (
    remove_list_redundancies,
    list_update,
    list_difference_update,
    adjacent_n_tuples,
    adjacent_pairs,
    batch_by_property,
    listify,
    shuffled,
    resize_array,
    resize_preserving_order,
    resize_with_interpolation,
    make_even,
    arrays_match,
    array_is_constant,
    cartesian_product,
    hash_obj
)


class TestUtilities(unittest.TestCase):
    def test_remove_list_redundancies(self):
        lst = [1, 2, 3, 1, 2, 4]
        result = remove_list_redundancies(lst)
        self.assertEqual(result, [3, 1, 2, 4])

    def test_list_update(self):
        l1, l2 = [1, 2, 3], [3, 4, 5]
        result = list_update(l1, l2)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_list_difference_update(self):
        l1, l2 = [1, 2, 3, 4], [2, 4]
        result = list_difference_update(l1, l2)
        self.assertEqual(result, [1, 3])

    def test_adjacent_n_tuples(self):
        objects = [1, 2, 3, 4]
        result = list(adjacent_n_tuples(objects, 3))
        expected = [(1, 2, 3), (2, 3, 4), (3, 4, 1), (4, 1, 2)]
        self.assertEqual(result, expected)

    def test_adjacent_pairs(self):
        objects = [1, 2, 3]
        result = list(adjacent_pairs(objects))
        expected = [(1, 2), (2, 3), (3, 1)]
        self.assertEqual(result, expected)

    def test_batch_by_property(self):
        items = [1, 1, 2, 2, 3, 1]
        result = batch_by_property(items, lambda x: x)
        expected = [([1, 1], 1), ([2, 2], 2), ([3], 3), ([1], 1)]
        self.assertEqual(result, expected)

    def test_listify(self):
        self.assertEqual(listify("abc"), ["abc"])
        self.assertEqual(listify([1, 2, 3]), [1, 2, 3])
        self.assertEqual(listify(42), [42])

    def test_shuffled(self):
        iterable = [1, 2, 3, 4, 5]
        result = shuffled(iterable)
        self.assertCountEqual(result, iterable)

    def test_resize_array(self):
        array = np.array([1, 2, 3])
        self.assertTrue(np.array_equal(resize_array(array, 5), np.array([1, 2, 3, 1, 2])))
        self.assertTrue(np.array_equal(resize_array(array, 2), np.array([1, 2])))

    def test_resize_preserving_order(self):
        array = np.array([10, 20, 30])
        result = resize_preserving_order(array, 6)
        expected = np.array([10, 10, 20, 20, 30, 30])
        np.testing.assert_array_equal(result, expected)

    def test_resize_with_interpolation(self):
        array = np.array([1, 3, 5])
        result = resize_with_interpolation(array, 5)
        expected = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        np.testing.assert_allclose(result, expected)

    def test_make_even(self):
        iterable_1 = [1, 2, 3]
        iterable_2 = [4, 5]
        result = make_even(iterable_1, iterable_2)
        expected = ([1, 2, 3], [4, 4, 5])
        self.assertEqual(result, expected)

    def test_arrays_match(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([1, 2, 3])
        self.assertTrue(arrays_match(arr1, arr2))

    def test_array_is_constant(self):
        array = np.array([5, 5, 5])
        self.assertTrue(array_is_constant(array))

    def test_cartesian_product(self):
        arrays = [np.array([1, 2]), np.array([3, 4])]
        result = cartesian_product(*arrays)
        expected = np.array([[1, 3], [1, 4], [2, 3], [2, 4]])
        np.testing.assert_array_equal(result, expected)

    def test_hash_obj(self):
        obj = {"a": 1, "b": 2}
        self.assertIsInstance(hash_obj(obj), int)

        obj = [1, 2, 3]
        self.assertIsInstance(hash_obj(obj), int)

        obj = Color("red")
        self.assertIsInstance(hash_obj(obj), int)


if __name__ == "__main__":
    unittest.main()
