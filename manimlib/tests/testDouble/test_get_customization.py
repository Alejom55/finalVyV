import unittest
from unittest.mock import patch, MagicMock
import os
import tempfile
from manimlib.utils.customization import get_customization, CUSTOMIZATION


class TestGetCustomization(unittest.TestCase):
    def setUp(self):
        # Limpia CUSTOMIZATION antes de cada prueba
        CUSTOMIZATION.clear()

    @patch("manimlib.utils.customization.get_custom_config")
    @patch("manimlib.utils.customization.get_manim_dir")
    def test_get_customization_with_default_values(self, mock_get_manim_dir, mock_get_custom_config):
        # Arrange
        mock_get_custom_config.return_value = {
            "directories": {
                "temporary_storage": "",
                "shaders": "",
            }
        }
        mock_get_manim_dir.return_value = "/mocked/manim/dir"

        # Act
        result = get_customization()

        # Assert
        expected_result = {
            "directories": {
                "temporary_storage": tempfile.gettempdir(),
                "shaders": os.path.join("/mocked/manim/dir", "manimlib", "shaders"),
            }
        }
        self.assertEqual(result, expected_result)
        mock_get_custom_config.assert_called_once()
        mock_get_manim_dir.assert_called_once()

    @patch("manimlib.utils.customization.get_custom_config")
    @patch("manimlib.utils.customization.get_manim_dir")
    def test_get_customization_with_user_defined_values(self, mock_get_manim_dir, mock_get_custom_config):
        # Arrange
        mock_get_custom_config.return_value = {
            "directories": {
                "temporary_storage": "/user/temp/dir",
                "shaders": "/user/shaders/dir",
            }
        }
        mock_get_manim_dir.return_value = "/mocked/manim/dir"
        # Act
        result = get_customization()
        # Assert
        expected_result = {
            "directories": {
                "temporary_storage": "/user/temp/dir",
                "shaders": "/user/shaders/dir",
            }
        }
        self.assertEqual(result, expected_result)
        mock_get_custom_config.assert_called_once()
        mock_get_manim_dir.assert_not_called()  # No need to call if user-defined shaders are set
    def test_get_customization_cached(self):
        # Arrange
        CUSTOMIZATION.update({
            "directories": {
                "temporary_storage": "/cached/temp/dir",
                "shaders": "/cached/shaders/dir",
            }
        })

        # Act
        result = get_customization()

        # Assert
        expected_result = {
            "directories": {
                "temporary_storage": "/cached/temp/dir",
                "shaders": "/cached/shaders/dir",
            }
        }
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()


# def get_customization():
#     if not CUSTOMIZATION:
#         CUSTOMIZATION.update(get_custom_config())
#         directories = CUSTOMIZATION["directories"]
#         # Unless user has specified otherwise, use the system default temp
#         # directory for storing tex files, mobject_data, etc.
#         if not directories["temporary_storage"]:
#             directories["temporary_storage"] = tempfile.gettempdir()

#         # Assumes all shaders are written into manimlib/shaders
#         directories["shaders"] = os.path.join(
#             get_manim_dir(), "manimlib", "shaders"
#         )
#     return CUSTOMIZATION