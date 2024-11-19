import unittest
import numpy as np
from colour import Color
from manimlib.utils.color import (
    color_gradient,
    interpolate_color,
    interpolate_color_by_hsl,
    average_color,
    random_color,
    random_bright_color,
    get_colormap_list
)


class TestColorFunctions(unittest.TestCase):
    def test_color_gradient(self):
        # Arrange
        reference_colors = ["#FF0000", "#00FF00", "#0000FF"]
        length_of_output = 5

        # Act
        result = color_gradient(reference_colors, length_of_output)

        # Assert
        self.assertEqual(len(result), length_of_output)
        self.assertEqual(result[0], Color("#FF0000"))
        self.assertEqual(result[-1], Color("#0000FF"))

    def test_interpolate_color(self):
        # Arrange
        color1 = "#FF00FF"
        color2 = "#0000FF"
        alpha = 0.5

        # Act
        result = interpolate_color(color1, color2, alpha)

        # Assert
        rgb1 = np.array([1.0, 0.0, 1.0])  # RGB for #FF00FF
        rgb2 = np.array([0.0, 0.0, 1.0])  # RGB for #0000FF
        expected_rgb = np.sqrt((1 - alpha) * (rgb1**2) + alpha * (rgb2**2))
        expected_result = Color(rgb=expected_rgb)
        self.assertEqual(result.get_hex_l().upper(), expected_result.get_hex_l().upper())


    def test_interpolate_color_by_hsl(self):
        # Arrange
        color1 = "#FF0000"
        color2 = "#0000FF"
        alpha = 0.5

        # Act
        result = interpolate_color_by_hsl(color1, color2, alpha)

        # Assert
        self.assertTrue(isinstance(result, Color))

    def test_average_color(self):
        # Arrange
        colors = ["#FF0000", "#00FF00", "#0000FF"]

        # Act
        result = average_color(*colors)

        # Assert
        rgbs = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])  
        expected_rgb = np.sqrt((rgbs**2).mean(0))
        expected_result = Color(rgb=expected_rgb)
        self.assertEqual(result.get_hex_l().upper(), expected_result.get_hex_l().upper())


    def test_random_color(self):
        # Act
        result = random_color()

        # Assert
        self.assertTrue(isinstance(result, Color))

    def test_random_bright_color(self):
        # Act
        result = random_bright_color()

        # Assert
        self.assertTrue(isinstance(result, Color))

    def test_get_colormap_list(self):
        # Arrange
        map_name = "viridis"
        n_colors = 5

        # Act
        result = get_colormap_list(map_name, n_colors)

        # Assert
        self.assertEqual(len(result), n_colors)
        self.assertTrue(isinstance(result, np.ndarray))


if __name__ == "__main__":
    unittest.main()
