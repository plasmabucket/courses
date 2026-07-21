"""Tests for task 28."""

import unittest
import random
import math
import task28


class Task28Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertEqual("10010", task28.Keymaker(5),
                         "Solution is incorrect.")
        self.assertEqual("1001000010", task28.Keymaker(10),
                         "Solution is incorrect.")

    def test_null(self) -> None:
        """Tests solution on minimum values."""
        self.assertEqual("", task28.Keymaker(0),
                         "Empty list is unhandled.")
        self.assertEqual("1", task28.Keymaker(1),
                         "List of size 1 is unhandled.")

    def test_large(self) -> None:
        """Tests solution on a large value."""
        expected_list: list[str] = ["0"] * 10000
        for i in range(100):
            expected_list[(i + 1) ** 2 - 1] = "1"
        expected: str = "".join(expected_list)
        self.assertEqual(expected, task28.Keymaker(10000),
                         "Large values are unhandled.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 10000 runs
        for i in range(10000):
            expected_len: int = random.randint(1, 1000)
            expected_list: list[str] = ["0"] * expected_len
            for i in range(math.isqrt(expected_len)):
                expected_list[(i + 1) ** 2 - 1] = "1"
            expected: str = "".join(expected_list)
            self.assertEqual(expected, task28.Keymaker(expected_len),
                             f"Solution failed on random data."
                             f"len: {expected_len}")


if __name__ == '__main__':
    unittest.main()



