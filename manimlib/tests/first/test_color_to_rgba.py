import unittest
import numpy as np
from unittest.mock import patch
from manimlib.utils.color import color_to_rgba

class TestColorToRgba(unittest.TestCase):
    @patch("manimlib.utils.color.color_to_rgb")
    def test_color_to_rgba_default_alpha(self, mock_color_to_rgb):
        # Arrange
        color = "#FF5733"
        mock_color_to_rgb.return_value = np.array([1.0, 0.3412, 0.2])
        alpha = 1.0

        # Act
        result = color_to_rgba(color)

        # Assert
        expected_result = np.array([1.0, 0.3412, 0.2, alpha])
        np.testing.assert_array_equal(result, expected_result)
        mock_color_to_rgb.assert_called_once_with(color)

    @patch("manimlib.utils.color.color_to_rgb")
    def test_color_to_rgba_custom_alpha(self, mock_color_to_rgb):
        # Arrange
        color = "#FF5733"
        mock_color_to_rgb.return_value = np.array([1.0, 0.3412, 0.2])
        alpha = 0.5

        # Act
        result = color_to_rgba(color, alpha=alpha)

        # Assert
        expected_result = np.array([1.0, 0.3412, 0.2, alpha])
        np.testing.assert_array_equal(result, expected_result)
        mock_color_to_rgb.assert_called_once_with(color)

    @patch("manimlib.utils.color.color_to_rgb")
    def test_invalid_color_type(self, mock_color_to_rgb):
        # Arrange
        color = 12345
        mock_color_to_rgb.side_effect = Exception("Invalid color type")

        # Act & Assert
        with self.assertRaises(Exception) as context:
            color_to_rgba(color)
        self.assertEqual(str(context.exception), "Invalid color type")
        mock_color_to_rgb.assert_called_once_with(color)

if __name__ == "__main__":
    unittest.main()
