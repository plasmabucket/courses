"""Tests for task 25."""

import unittest
import task25


class Task25Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_transform(self) -> None:
        """Tests transformation on a known case."""
        data: list[int] = [2, 1, 3]
        expected: list[int] = [2, 1, 3, 2, 3, 3]
        self.assertEqual(expected, task25.transform(data),
                         "Transformation function is incorrect.")

    def test_transform_output_len(self) -> None:
        """Tests that transformation creates a list of predicted length."""
        # Make 10 runs
        for i in range(1, 11):
            data: list[int] = [1] * i
            result: list[int] = task25.transform(data)
            self.assertEqual((i * (i + 1)) // 2, len(result),
                             "Unexpected list length after transformation.")

    def test_transform_null(self) -> None:
        """Tests transformation on the shortest list."""
        data: list[int] = [1]
        expected: list[int] = [1]
        self.assertEqual(expected, task25.transform(data),
                         "Transformation of the shortest list is unhandled.")

    def test_transform_side_effects(self) -> None:
        """Tests if transformation function mutates its parameters."""
        data: list[int] = [1, 2, 3, 4, 5]
        expected: list[int] = data.copy()
        task25.transform(data)
        self.assertEqual(expected, data,
                         "Transformation function mutates its parameters.")

    def test_tt(self) -> None:
        """Tests solution on known cases."""
        data: list[int] = [2, 1, 3]
        # Intermediate lists should be:
        # [2, 1, 3, 2, 3, 3]
        # [2, 1, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        # Sum should be:
        # 58
        self.assertTrue(task25.TransformTransform(data, len(data)),
                        "Key parity is determined incorrectly.")

        data = [2, 1, 4]
        # Intermediate lists should be:
        # [2, 1, 4, 2, 4, 4]
        # [2, 1, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        # Sum should be:
        # 75
        self.assertFalse(task25.TransformTransform(data, len(data)),
                         "Key parity is determined incorrectly.")

    def test_tt_null(self) -> None:
        """Tests solution on the shortest list."""
        data: list[int] = [1]
        self.assertFalse(task25.TransformTransform(data, len(data)),
                         "Shortest list is unhandled in key calculation.")


if __name__ == '__main__':
    unittest.main()



