"""Tests for task 2."""

import unittest
from random import randint
import task2


class Task2Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertEqual(task2.odometer([10, 1, 20, 2]), 30,
                         "Solution is incorrect")

    def test_short_array(self) -> None:
        """Tests solution on minimal array length."""
        self.assertEqual(task2.odometer([1, 1]), 1,
                         "Short array isn't handled")

    def test_null(self) -> None:
        """Tests solution on an array full of zeroes."""
        self.assertEqual(task2.odometer([0, 0, 0, 0, 0, 0]), 0,
                         "Zeroes aren't handled properly.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Running our solution 1000 times
        for i in range(1000):
            array_len: int = randint(1, 20)  # Actual length will be doubled
            array: list[int] = []
            total_time: int = 0
            total_distance: int = 0  # This will be our answer
            # Filling our array with random data
            for j in range(array_len):
                speed: int = randint(0, 200)
                time: int = randint(0, 100)
                total_time += time
                array.append(speed)
                array.append(total_time)
                total_distance += speed * time
            self.assertEqual(task2.odometer(array), total_distance,
                             "Solution failed on random data.")


if __name__ == '__main__':
    unittest.main()



