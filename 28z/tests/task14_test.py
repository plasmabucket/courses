"""Tests for task 14."""

import unittest
import task14


class Task14Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertEqual(12, task14.Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]),
                         "Solution is incorrect.")

    def test_null(self) -> None:
        """Tests solution on case with no streetlights."""
        self.assertEqual(1, task14.Unmanned(1, 0, []),
                         "Case with no streetlights is unhandled.")

    def test_streetlight_on_start(self) -> None:
        """A case where a streetlight is encountered immediately."""
        self.assertEqual(20, task14.Unmanned(10, 1, [[0, 10, 1]]),
                         "Immediate streetlight is unhandled.")

    def test_many_streetlights(self) -> None:
        """A case where a streetlight is placed at every point."""
        streetlights: list[list[int]] = [[1, 10, 10],
                                         [2, 9, 9],
                                         [3, 8, 8],
                                         [4, 7, 7],
                                         [5, 6, 6],
                                         [6, 5, 5],
                                         [7, 4, 4],
                                         [8, 3, 3],
                                         [9, 2, 2]]
        self.assertEqual(23, task14.Unmanned(10, 9, streetlights),
                         "Solution failed on a case with many streetlights.")

    def test_green_light_end(self) -> None:
        """Tests behavior at the end of the green light period."""
        self.assertEqual(13, task14.Unmanned(10, 1, [[6, 3, 3]]),
                         "If the car comes at the end of the green period, "
                         "the red period is skipped.")


if __name__ == '__main__':
    unittest.main()



