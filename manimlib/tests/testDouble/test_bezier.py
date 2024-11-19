import unittest
import numpy as np
from manimlib.utils.bezier import bezier  # Reemplaza "your_module" con el nombre del archivo donde está la función


class TestBezierFunction(unittest.TestCase):
    def test_empty_points(self):
        with self.assertRaises(Exception) as context:
            bezier([])
        self.assertEqual(str(context.exception), "bezier cannot be calld on an empty list")

    def test_single_point(self):
        points = [np.array([1.0, 2.0])]
        curve = bezier(points)
        self.assertTrue(np.allclose(curve(0), points[0]))
        self.assertTrue(np.allclose(curve(0.5), points[0]))
        self.assertTrue(np.allclose(curve(1), points[0]))

    def test_two_points(self):
        points = [np.array([0.0, 0.0]), np.array([1.0, 1.0])]
        curve = bezier(points)
        self.assertTrue(np.allclose(curve(0), points[0]))  # t = 0
        self.assertTrue(np.allclose(curve(1), points[1]))  # t = 1
        self.assertTrue(np.allclose(curve(0.5), np.array([0.5, 0.5])))  # t = 0.5

    def test_three_points(self):
        points = [np.array([0.0, 0.0]), np.array([1.0, 2.0]), np.array([2.0, 0.0])]
        curve = bezier(points)
        self.assertTrue(np.allclose(curve(0), points[0]))  # t = 0
        self.assertTrue(np.allclose(curve(1), points[2]))  # t = 1
        midpoint = np.array([1.0, 1.0])
        self.assertTrue(np.allclose(curve(0.5), midpoint))

    def test_t_values(self):
        points = [np.array([0.0, 0.0]), np.array([1.0, 1.0])]
        curve = bezier(points)
        self.assertTrue(np.allclose(curve(0), points[0]))  # t = 0
        self.assertTrue(np.allclose(curve(1), points[1]))  # t = 1


if __name__ == "__main__":
    unittest.main()
