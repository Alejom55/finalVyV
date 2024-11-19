import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from PIL import Image
from manimlib.utils.images import (
    get_full_raster_image_path,
    get_full_vector_image_path,
    invert_image,
)

class TestImageFunctions(unittest.TestCase):
    @patch("manimlib.utils.images.find_file")
    @patch("manimlib.utils.images.get_raster_image_dir")
    def test_get_full_raster_image_path(self, mock_get_raster_image_dir, mock_find_file):
        # Arrange
        mock_get_raster_image_dir.return_value = "/mock/raster/dir"
        mock_find_file.return_value = "/mock/raster/dir/image.png"
        image_file_name = "image.png"

        # Act
        result = get_full_raster_image_path(image_file_name)

        # Assert
        mock_find_file.assert_called_once_with(
            image_file_name,
            directories=["/mock/raster/dir"],
            extensions=[".jpg", ".jpeg", ".png", ".gif", ""]
        )
        self.assertEqual(result, "/mock/raster/dir/image.png")

    @patch("manimlib.utils.images.find_file")
    @patch("manimlib.utils.images.get_vector_image_dir")
    def test_get_full_vector_image_path(self, mock_get_vector_image_dir, mock_find_file):
        # Arrange
        mock_get_vector_image_dir.return_value = "/mock/vector/dir"
        mock_find_file.return_value = "/mock/vector/dir/image.svg"
        image_file_name = "image.svg"

        # Act
        result = get_full_vector_image_path(image_file_name)

        # Assert
        mock_find_file.assert_called_once_with(
            image_file_name,
            directories=["/mock/vector/dir"],
            extensions=[".svg", ".xdv", ""]
        )
        self.assertEqual(result, "/mock/vector/dir/image.svg")

    def test_invert_image(self):
        # Arrange
        original_image = Image.fromarray(np.array([[0, 255], [128, 64]], dtype=np.uint8))

        # Act
        result = invert_image(original_image)

        # Assert
        expected_array = np.array([[255, 0], [127, 191]], dtype=np.uint8)
        result_array = np.array(result)
        np.testing.assert_array_equal(result_array, expected_array)


if __name__ == "__main__":
    unittest.main()
