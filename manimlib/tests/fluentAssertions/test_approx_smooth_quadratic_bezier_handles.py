import unittest
import numpy as np
from manimlib.utils.bezier import approx_smooth_quadratic_bezier_handles  # Cambia "manimlib.utils.bezier" por el nombre de tu archivo

class TestApproxSmoothQuadraticBezierHandles(unittest.TestCase):
    def test_single_point(self):
        # Arrange
        points = np.array([[1, 1, 1]])

        # Act
        result = approx_smooth_quadratic_bezier_handles(points)

        # Assert
        np.testing.assert_array_equal(result, points[0], "The result for a single point should be the point itself.")

    def test_two_points(self):
        # Arrange
        points = np.array([[0, 0, 0], [2, 2, 2]])

        # Act
        result = approx_smooth_quadratic_bezier_handles(points)

        # Assert
        expected = np.array([1, 1, 1])
        np.testing.assert_array_equal(result, expected, "The result for two points should be their midpoint.")

    def test_four_points_linear(self):
        # Arrange
        points = np.array([
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3]
        ])

        # Act
        result = approx_smooth_quadratic_bezier_handles(points)

        # Assert
        self.assertEqual(result.shape[0], 3, f"The number of handles should match the number of segments.")


    def test_circle_points(self):
        # Arrange
        points = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [-1, 0, 0],
            [0, -1, 0],
            [1, 0, 0]  # Closing the circle
        ])

        # Act
        result = approx_smooth_quadratic_bezier_handles(points)

        # Assert
        self.assertEqual(result.shape[0], 4, "The number of handles should match the number of segments.")
        self.assertFalse(np.allclose(result[0], result[-1]), "Handles for closed loops should match.")

    def test_complex_shape(self):
        # Arrange
        points = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [-1, 0, 0]
        ])

        # Act
        result = approx_smooth_quadratic_bezier_handles(points)

        # Assert
        self.assertEqual(result.shape[0], 4, "The number of handles should match the number of segments.")
        self.assertTrue(result[0].shape == (3,), "Handles must be 3D vectors.")

if __name__ == "__main__":
    unittest.main()
