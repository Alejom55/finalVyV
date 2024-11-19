import unittest
import numpy as np
from manimlib.utils.bezier import outer_interpolate

class TestOuterInterpolateFunction(unittest.TestCase):
    def test_scalar_interpolation(self):
        start = 0
        end = 10
        alpha = 0.5
        result = outer_interpolate(start, end, alpha)
        expected_result = np.array(5)
        self.assertTrue(np.allclose(result, expected_result), f"Expected {expected_result}, but got {result}")

    def test_vector_interpolation(self):
        start = np.array([1, 2])
        end = np.array([3, 4])
        alpha = 0.5
        result = outer_interpolate(start, end, alpha)
        expected_result = np.array([2, 3])
        self.assertTrue(np.allclose(result, expected_result), f"Expected {expected_result}, but got {result}")

    def test_alpha_array(self):
        start = np.array([1, 2])
        end = np.array([3, 4])
        alpha = np.array([0.0, 0.5, 1.0])
        result = outer_interpolate(start, end, alpha)
        expected_result = np.array([
            [1, 2],
            [2, 3],
            [3, 4],
        ])
        self.assertTrue(np.allclose(result, expected_result), f"Expected {expected_result}, but got {result}")

    def test_shape_consistency(self):
        start = np.array([1, 2, 3])
        end = np.array([4, 5, 6])
        alpha = np.array([0.2, 0.8])
        result = outer_interpolate(start, end, alpha)
        expected_shape = (2, 3)
        self.assertEqual(result.shape, expected_shape, f"Expected shape {expected_shape}, but got {result.shape}")

if __name__ == "__main__":
    unittest.main()
