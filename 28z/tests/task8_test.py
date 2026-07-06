"""Tests for task 8."""

import unittest
import random
import sys
import task8


class Task8Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        data: list[int] = [10, -25, -45, -35, 5]
        self.assertEqual(-45, task8.SumOfThe(len(data), data),
                         "Solution is incorrect.")

    def test_null(self) -> None:
        """Tests solution on a list of minimal size."""
        data: list[int] = [10, 10]
        self.assertEqual(10, task8.SumOfThe(len(data), data),
                         "Short lists are unhandled.")

    def test_big_numbers(self) -> None:
        """Tests solution on a list containing big integers."""
        data: list[int] = [sys.maxsize + 1, -(sys.maxsize + 10), -9]
        self.assertEqual(-9, task8.SumOfThe(len(data), data),
                         "Big integers aren't handled.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 10000 runs
        for i in range(10000):
            n: int = random.randint(2, 1000)  # Number of elements
            expected_sum: int = 0
            data: list[int] = []
            for j in range(n - 1):  # -1 since we will add "total sum" element
                element: int = random.randint(-1000, 1000)
                expected_sum += element
                data.append(element)
            data.append(expected_sum)  # Add the "total sum" element
            random.shuffle(data)
            self.assertEqual(expected_sum, task8.SumOfThe(n, data),
                             f"Solution failed on random data. Run №{i}")


if __name__ == "__main__":
    unittest.main()



