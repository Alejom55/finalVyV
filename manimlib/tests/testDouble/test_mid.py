import unittest
import numpy as np
from manimlib.utils.bezier import mid  # Cambia "manimlib.utils.bezier" por el nombre de tu archivo

class TestMidFunction(unittest.TestCase):
    def test_scalar_mid(self):
        start = 2.0
        end = 4.0
        result = mid(start, end)
        expected_result = 3.0
        self.assertEqual(result, expected_result, f"Expected {expected_result}, but got {result}")

    def test_numpy_array_mid(self):
        start = np.array([1.0, 2.0, 3.0])
        end = np.array([4.0, 5.0, 6.0])
        result = mid(start, end)
        expected_result = np.array([2.5, 3.5, 4.5])
        self.assertTrue(np.allclose(result, expected_result), f"Expected {expected_result}, but got {result}")

    def test_type_error_handling(self):
        start = "invalid_start"
        end = np.array([4.0, 5.0, 6.0])
        with self.assertRaises(TypeError):
            mid(start, end)


if __name__ == "__main__":
    unittest.main()
