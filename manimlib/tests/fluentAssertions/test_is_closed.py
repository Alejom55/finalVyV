import unittest
import numpy as np
from manimlib.utils.bezier import is_closed

class TestIsClosed(unittest.TestCase):
    def test_closed_points(self):
        points = np.array([[1, 1], [2, 2], [1, 1]])
        result = is_closed(points)
        self.assertTrue(result)

    def test_not_closed_points(self):
        points = np.array([[1, 1], [2, 2], [3, 3]])
        result = is_closed(points)
        self.assertFalse(result)

    def test_single_point(self):
        points = np.array([[1, 1]])
        result = is_closed(points)
        self.assertTrue(result)

    def test_large_tolerance(self):
        points = np.array([[1, 1], [2, 2], [1.0001, 1.0001]])
        result = is_closed(points)
        self.assertFalse(result)

    def test_different_dimensions(self):
        points = np.array([[1, 1, 1], [2, 2, 2], [1, 1, 0]])
        result = is_closed(points)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
