import unittest
import numpy as np
from manimlib.utils.bezier import inverse_interpolate


class TestInverseInterpolate(unittest.TestCase):
    def test_scalar_interpolation(self):
        # Arrange
        start = 0
        end = 10
        value = 5

        # Act
        result = inverse_interpolate(start, end, value)

        # Assert
        expected_result = 0.5
        self.assertEqual(result, expected_result, f"Expected {
                         expected_result}, but got {result}")

    def test_vector_interpolation(self):
        # Arrange
        start = np.array([0, 0])
        end = np.array([10, 20])
        value = np.array([5, 10])

        # Act
        result = inverse_interpolate(start, end, value)

        # Assert
        expected_result = np.array([0.5, 0.5])
        self.assertTrue(np.allclose(result, expected_result),
                        f"Expected {expected_result}, but got {result}")

    def test_division_by_zero(self):
        # Arrange
        start = 5
        end = 5
        value = 5

        # Act
        result = inverse_interpolate(start, end, value)

        # Assert
        self.assertTrue(np.isnan(result), f"Expected nan, but got {result}")

    def test_out_of_range_values(self):
        # Arrange
        start = 0
        end = 10
        value_below = -5
        value_above = 15

        # Act
        result_below = inverse_interpolate(start, end, value_below)
        result_above = inverse_interpolate(start, end, value_above)

        # Assert
        self.assertEqual(result_below, -0.5,
                         f"Expected -0.5, but got {result_below}")
        self.assertEqual(result_above, 1.5,
                         f"Expected 1.5, but got {result_above}")


if __name__ == "__main__":
    unittest.main()
