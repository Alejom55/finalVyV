import unittest
import numpy as np
from unittest.mock import MagicMock, patch
from manimlib.mobject.vector_field import (
    get_vectorized_rgb_gradient_function,
    get_rgb_gradient_function,
    move_along_vector_field,
    move_submobjects_along_vector_field,
    move_points_along_vector_field,
    get_sample_points_from_coordinate_system,
)


class TestUtilityFunctions(unittest.TestCase):
    def test_get_vectorized_rgb_gradient_function(self):
        # Arrange
        min_value = 0
        max_value = 10
        color_map = "viridis"

        # Act
        func = get_vectorized_rgb_gradient_function(min_value, max_value, color_map)
        result = func([0, 5, 10])

        # Assert
        self.assertEqual(result.shape, (3, 3))  # 3 colors (RGB)
        self.assertTrue((result >= 0).all() and (result <= 1).all())  # Valid RGB values

    def test_get_rgb_gradient_function(self):
        # Arrange
        min_value = 0
        max_value = 10
        color_map = "viridis"

        # Act
        func = get_rgb_gradient_function(min_value, max_value, color_map)
        result = func(5)

        # Assert
        self.assertEqual(result.shape, (3,))  # Single RGB value
        self.assertTrue((result >= 0).all() and (result <= 1).all())  # Valid RGB values

    def test_move_along_vector_field(self):
        # Arrange
        mobject = MagicMock()
        func = lambda pos: np.array([1, 0, 0])  # Simple constant vector field

        # Act
        result = move_along_vector_field(mobject, func)

        # Assert
        mobject.add_updater.assert_called_once()
        self.assertEqual(result, mobject)

    def test_move_submobjects_along_vector_field(self):
        # Arrange
        mobject = MagicMock()
        submob1 = MagicMock(get_center=MagicMock(return_value=np.array([1, 1, 0])))
        submob2 = MagicMock(get_center=MagicMock(return_value=np.array([2, 2, 0])))
        mobject.__iter__.return_value = [submob1, submob2]
        func = lambda pos: np.array([0.5, 0.5, 0])  # Constant vector field

        # Act
        result = move_submobjects_along_vector_field(mobject, func)

        # Assert
        mobject.add_updater.assert_called_once()
        self.assertEqual(result, mobject)

    def test_move_points_along_vector_field(self):
        # Arrange
        mobject = MagicMock()
        func = lambda x, y: [x + 1, y + 1]  # Simple shift function
        coordinate_system = MagicMock(
            p2c=MagicMock(side_effect=lambda p: (p[0], p[1])),
            c2p=MagicMock(side_effect=lambda x, y: np.array([x, y, 0])),
            get_origin=MagicMock(return_value=np.array([0, 0, 0]))
        )

        # Act
        result = move_points_along_vector_field(mobject, func, coordinate_system)

        # Assert
        mobject.add_updater.assert_called_once()
        self.assertEqual(result, mobject)

    def test_get_sample_points_from_coordinate_system(self):
        # Arrange
        coordinate_system = MagicMock(
            get_all_ranges=MagicMock(return_value=[
                (0, 1, 0.5),  # x-range
                (0, 1, 0.5)   # y-range
            ])
        )
        step_multiple = 1.0

        # Act
        result = list(get_sample_points_from_coordinate_system(coordinate_system, step_multiple))

        # Assert
        expected = [
            (0, 0),
            (0, 0.5),
            (0, 1),
            (0.5, 0),
            (0.5, 0.5),
            (0.5, 1),
            (1, 0),
            (1, 0.5),
            (1, 1),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
