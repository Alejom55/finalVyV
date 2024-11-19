import unittest
from colour import Color
from manimlib.utils.color import rgb_to_color
from manimlib.constants import WHITE

class TestRgbToColor(unittest.TestCase):
    def test_valid_rgb(self):
        # Arrange
        rgb = [0.1, 0.2, 0.3]

        # Act
        result = rgb_to_color(rgb)

        # Assert
        expected_result = Color(rgb=(0.1, 0.2, 0.3))
        self.assertEqual(result, expected_result)

    def test_invalid_rgb(self):
        # Arrange
        rgb = [1.5, 0.2, 0.3]  # Invalid RGB value (1.5 is out of range)

        # Act
        result = rgb_to_color(rgb)

        # Assert
        expected_result = Color(WHITE)
        self.assertEqual(result, expected_result)

    def test_empty_sequence(self):
        # Arrange
        rgb = []

        # Act
        result = rgb_to_color(rgb)

        # Assert
        expected_result = Color(WHITE)
        self.assertEqual(result, expected_result)

    def test_non_numeric_values(self):
        # Arrange
        rgb = ["a", 0.2, 0.3]  # Non-numeric value

        # Act
        result = rgb_to_color(rgb)

        # Assert
        expected_result = Color(WHITE)
        self.assertEqual(result, expected_result)

    def test_rgb_with_length_greater_than_three(self):
        # Arrange
        rgb = [0.1, 0.2, 0.3, 0.4]

        # Act
        result = rgb_to_color(rgb)

        # Assert
        expected_result = Color(WHITE)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
