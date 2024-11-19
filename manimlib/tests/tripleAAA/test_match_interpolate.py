import unittest
import numpy as np
from manimlib.utils.bezier import match_interpolate 

class TestMatchInterpolate(unittest.TestCase):
    def test_scalar_mapping(self):
        # Arrange
        new_start = 0
        new_end = 100
        old_start = 0
        old_end = 10
        old_value = 5

        # Act
        result = match_interpolate(new_start, new_end, old_start, old_end, old_value)

        # Assert
        expected_result = 50
        self.assertEqual(result, expected_result, f"Expected {expected_result}, but got {result}")

    def test_inverted_ranges(self):
        # Arrange
        new_start = 100
        new_end = 0
        old_start = 10
        old_end = 0
        old_value = 5

        # Act
        result = match_interpolate(new_start, new_end, old_start, old_end, old_value)

        # Assert
        expected_result = 50
        self.assertEqual(result, expected_result, f"Expected {expected_result}, but got {result}")

    def test_edges_mapping(self):
        # Arrange
        new_start = 0
        new_end = 100
        old_start = 0
        old_end = 10

        # Act & Assert
        result_start = match_interpolate(new_start, new_end, old_start, old_end, old_start)
        result_end = match_interpolate(new_start, new_end, old_start, old_end, old_end)

        # Assert
        self.assertEqual(result_start, new_start, f"Expected {new_start}, but got {result_start}")
        self.assertEqual(result_end, new_end, f"Expected {new_end}, but got {result_end}")

    def test_numpy_array_mapping(self):
        # Arrange
        new_start = np.array([0, 0])
        new_end = np.array([100, 200])
        old_start = np.array([0, 10])
        old_end = np.array([10, 20])
        old_value = np.array([5, 15])

        # Act
        result = match_interpolate(new_start, new_end, old_start, old_end, old_value)

        # Assert
        expected_result = np.array([50, 100])
        self.assertTrue(np.allclose(result, expected_result), f"Expected {expected_result}, but got {result}")


if __name__ == "__main__":
    unittest.main()
