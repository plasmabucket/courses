"""Tests for task 4."""

import unittest
import random
import task4


class Task4Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        result: list[int] = task4.MadMax(7, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual([1, 2, 3, 7, 6, 5, 4], result,
                         "Solution is incorrect.")

    def test_short_list(self) -> None:
        """Tests solution on a list of size 1."""
        random_element: int = random.randint(0, 255)
        result: list[int] = task4.MadMax(1, [random_element])
        self.assertEqual([random_element], result,
                         "List of size 1 is unhandled")

    def test_long_list(self) -> None:
        """Tests solution on a list of size 127."""
        n: int = 127
        tele: list[int] = random.sample(range(127), n)
        result: list[int] = task4.MadMax(n, tele)
        expected: list[int] = []
        for i in range(63):
            expected.append(i)
        for i in range(126, 62, -1):
            expected.append(i)
        self.assertEqual(expected, result,
                         "List of maximum size is unhandled.")

    def test_random(self) -> None:
        """Tests solution on a random data."""
        # Make 1000 runs
        for i in range(1000):
            n: int = random.randint(0, 63) * 2 + 1
            tele: list[int] = random.sample(range(255), n)
            result: list[int] = task4.MadMax(n, tele)
            self.assertEqual(max(tele), result[n // 2],
                             "Middle element is not the maximal one.")
            self.assertEqual(min(tele), result[0],
                             "Leftmost element is not the minimal one.")
            for j in range(n // 2 - 1):
                self.assertLess(result[j], result[j + 1],
                                "Left half is not in an ascending order.")
            for j in range(n // 2, n - 1):
                self.assertGreater(result[j], result[j + 1],
                                   "Right half is not in a descending order.")


if __name__ == '__main__':
    unittest.main()



