"""Tests for task 27."""

import unittest
import random
import task27


class Task27Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertTrue(task27.Football([1, 3, 2],  3), "Solution is incorrect")
        self.assertTrue(task27.Football([3, 2, 1], 3), "Solution is incorrect.")
        self.assertTrue(task27.Football([1, 7, 5, 3, 9], 5), "Solution is incorrect.")
        self.assertFalse(task27.Football([9, 5, 3, 7, 1], 5), "Solution is incorrect.")
        self.assertTrue(task27.Football([1, 4, 3, 2, 5], 5), "Solution is incorrect.")

    def test_null(self) -> None:
        """Tests solution on shortest lists."""
        # I assume that on already sorted list we have to return False
        self.assertFalse(task27.Football([1], 1), "Shortest list is unhandled.")
        self.assertFalse(task27.Football([1, 2], 2), "List of size 2 is unhandled.")
        self.assertTrue(task27.Football([2, 1], 2), "List of size 2 is unhandled.")

    def test_sorted(self) -> None:
        """Tests solution on an already sorted list."""
        # It is not specified what the behavior should be
        # I will assume we should return False
        self.assertFalse(task27.Football([1, 2, 3, 4, 5], 5), "Sorted list is unhandled.")

    def test_param_mutation(self) -> None:
        """Tests if solution mutates its parameters."""
        data: list[int] = [1, 2, 3, 7, 6, 5, 4, 8, 9, 10]
        data_original: list[int] = data.copy()
        task27.Football(data, len(data))
        self.assertEqual(data_original, data, "Solution mutates its parameters.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 1000 runs
        for i in range(1000):
            sorted_data: list[int] = list(range(1, random.randint(3, 100)))

            # Test for swap recognition
            swapped: list[int] = sorted_data.copy()
            swap: list[int] = random.sample(range(0, len(sorted_data)), 2)
            swapped[swap[0]], swapped[swap[1]] = swapped[swap[1]], swapped[swap[0]]
            self.assertTrue(task27.Football(swapped, len(swapped)),
                            f"Valid swap is not recognised\n"
                            f"data: {swapped}")

            # Test for reversal recognition
            reverse: list[int] = sorted_data.copy()
            rev: list[int] = random.sample(range(0, len(sorted_data)), 2)
            rev.sort()
            subsequence: list[int] = reverse[rev[0]:rev[1]+1]
            subsequence.reverse()
            reverse[rev[0]:rev[1]+1] = subsequence
            self.assertTrue(task27.Football(reverse, len(reverse)),
                            f"Valid reverse is not recognised\n"
                            f"data: {reverse}")


if __name__ == '__main__':
    unittest.main()



