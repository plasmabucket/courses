"""Tests for task 3."""

import unittest
import task3


class Task3Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        result: int = task3.ConquestCampaign(3, 4, 2, [2, 2, 3, 4])
        self.assertEqual(result, 3,
                         "Solution is incorrect.")

    def test_small_field(self) -> None:
        """Edge case: field of minimal size."""
        result: int = task3.ConquestCampaign(1, 1, 1, [1, 1])
        # Answer should be 1 since the field is
        # instantly captured by a single battalion
        self.assertEqual(result, 1,
                         "Single-cell field is not handled.")

    def test_double_dispatch(self) -> None:
        """Edge case: two battalions are dispatched on a single cell."""
        result: int = task3.ConquestCampaign(3, 4, 2, [2, 2, 2, 2])
        self.assertEqual(result, 4,
                         "Double dispatch case is unhandled.")

    def test_captured_instantly(self) -> None:
        """Edge case: all cells are captured on day 1."""
        result: int = task3.ConquestCampaign(3, 4, 12,
            [1,1, 1,2, 1,3, 1,4, 2,1, 2,2, 2,3, 2,4, 3,1, 3,2, 3,3, 3,4])
        self.assertEqual(result, 1,
                         "Instant capture case is unhandled.")


if __name__ == '__main__':
    unittest.main()



