import unittest
import numpy as np
from manimlib.utils.bezier import quadratic_bezier_points_for_arc  

class TestQuadraticBezierPointsForArc(unittest.TestCase):
    def test_zero_angle(self):
        # Arrange
        angle = 0
        n_components = 8

        # Act
        result = quadratic_bezier_points_for_arc(angle, n_components)

        # Assert
        expected_result = np.array([[1, 0, 0]])
        self.assertTrue(np.allclose(result, expected_result), f"Expected {expected_result}, but got {result}")

    def test_quarter_circle(self):
        # Arrange
        angle = np.pi / 2
        n_components = 4

        # Act
        result = quadratic_bezier_points_for_arc(angle, n_components)

        # Assert
        n_points = 2 * n_components + 1
        self.assertEqual(result.shape, (n_points, 3), f"Expected shape {(n_points, 3)}, but got {result.shape}")
        self.assertTrue(np.allclose(result[0], [1, 0, 0]), f"Expected start point [1, 0, 0], but got {result[0]}")
        self.assertTrue(np.allclose(result[-1], [0, 1, 0]), f"Expected end point [0, 1, 0], but got {result[-1]}")

    def test_full_circle(self):
        # Arrange
        angle = 2 * np.pi
        n_components = 8

        # Act
        result = quadratic_bezier_points_for_arc(angle, n_components)

        # Assert
        n_points = 2 * n_components + 1
        self.assertEqual(result.shape, (n_points, 3), f"Expected shape {(n_points, 3)}, but got {result.shape}")
        self.assertTrue(np.allclose(result[0], [1, 0, 0]), f"Expected start point [1, 0, 0], but got {result[0]}")
        self.assertTrue(np.allclose(result[-1], [1, 0, 0], atol=1e-6), f"Expected end point [1, 0, 0], but got {result[-1]}")

    def test_handle_adjustment(self):
        # Arrange
        angle = np.pi / 2
        n_components = 2

        # Act
        result = quadratic_bezier_points_for_arc(angle, n_components)

        # Assert
        theta = angle / n_components
        adjusted_handle = np.cos(theta / 2)
        self.assertFalse(np.allclose(result[1], result[1] * adjusted_handle), "Handle adjustment is incorrect")

    def test_number_of_points(self):
        # Arrange
        angle = np.pi
        n_components = 5

        # Act
        result = quadratic_bezier_points_for_arc(angle, n_components)

        # Assert
        n_points = 2 * n_components + 1
        self.assertEqual(result.shape[0], n_points, f"Expected {n_points} points, but got {result.shape[0]}")


if __name__ == "__main__":
    unittest.main()
