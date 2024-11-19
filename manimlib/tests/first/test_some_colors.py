import unittest
import numpy as np
from colour import Color
from manimlib.utils.color import (
    invert_color,
    color_to_int_rgb,
    color_to_int_rgba,
    color_to_hex,
    hex_to_int,
    int_to_hex,
)

class TestColorFunctionsExtended(unittest.TestCase):
    def test_invert_color(self):
        color = "#123456"
        result = invert_color(color)
        expected_result = Color(rgb=(1.0 - 0.0706, 1.0 - 0.2039, 1.0 - 0.3373))
        self.assertEqual(result, expected_result)

    def test_color_to_int_rgb(self):
        color = "#123456"
        result = color_to_int_rgb(color)
        expected_result = np.array([18, 52, 86], dtype=np.uint8)
        np.testing.assert_array_equal(result, expected_result)

    def test_color_to_int_rgba(self):
        color = "#123456"
        opacity = 0.5
        result = color_to_int_rgba(color, opacity=opacity)
        expected_result = np.array([18, 52, 86, 127], dtype=np.uint8)
        np.testing.assert_array_equal(result, expected_result)

    def test_color_to_hex(self):
        color = Color(rgb=(0.1, 0.2, 0.3))
        result = color_to_hex(color)
        expected_result = "#19334C"
        self.assertEqual(result, expected_result)

    def test_hex_to_int(self):
        hex_code = "#1A334D"
        result = hex_to_int(hex_code)
        expected_result = int("1A334D", 16)
        self.assertEqual(result, expected_result)

    def test_int_to_hex(self):
        rgb_int = 0x1A334D
        result = int_to_hex(rgb_int)
        expected_result = "#1A334D"
        self.assertEqual(result, expected_result)

    def test_invert_color_edge_case(self):
        color = "#000000"
        result = invert_color(color)
        expected_result = Color(rgb=(1.0, 1.0, 1.0))
        self.assertEqual(result, expected_result)

    def test_color_to_int_rgba_full_opacity(self):
        color = "#123456"
        result = color_to_int_rgba(color)
        expected_result = np.array([18, 52, 86, 255], dtype=np.uint8)
        np.testing.assert_array_equal(result, expected_result)

    def test_hex_to_int_edge_case(self):
        hex_code = "#FFFFFF"
        result = hex_to_int(hex_code)
        expected_result = 0xFFFFFF
        self.assertEqual(result, expected_result)

    def test_int_to_hex_edge_case(self):
        rgb_int = 0x000000
        result = int_to_hex(rgb_int)
        expected_result = "#000000"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
