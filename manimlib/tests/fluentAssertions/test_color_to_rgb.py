import unittest
import numpy as np
from colour import Color
from manimlib.utils.color import color_to_rgb

class TestColorToRgb(unittest.TestCase):
    def test_hex_color(self):
        color = "#FF5733"
        result = color_to_rgb(color)
        expected = np.array([1.0, 0.3412, 0.2])
        np.testing.assert_allclose(result, expected, rtol=1e-3)

    def test_colour_object(self):
        color = Color(rgb=(0.1, 0.2, 0.3))
        result = color_to_rgb(color)
        expected = np.array([0.1, 0.2, 0.3])
        np.testing.assert_allclose(result, expected, rtol=1e-6)

    def test_invalid_color_type(self):
        color = 12345
        with self.assertRaises(Exception) as context:
            color_to_rgb(color)
        self.assertEqual(str(context.exception), "Invalid color type")

if __name__ == "__main__":
    unittest.main()
