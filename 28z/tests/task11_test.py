"""Tests for task 11."""

import unittest
import random
import task11


class Task11Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertEqual("1234567890", task11.BigMinus("1234567891", "1"),
                         "Solution is incorrect.")
        self.assertEqual("320", task11.BigMinus("1", "321"),
                         "Negative numbers aren't calculated properly.")

    def test_null(self) -> None:
        """Tests solution on one-character long strings."""
        self.assertEqual("0", task11.BigMinus("0", "0"),
                         "Short strings aren't handled properly.")

    def test_max(self) -> None:
        """Tests solution on maximum values."""
        self.assertEqual("0", task11.BigMinus(str(10 ** 16), str(10 ** 16)),
                         "Big values are unhandled.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 100000 runs
        for i in range(100000):
            num1: int = random.randint(0, 10 ** 16)
            num2: int = random.randint(0, 10 ** 16)
            expected: str = str(abs(num1 - num2))
            result: str = task11.BigMinus(str(num1), str(num2))
            self.assertEqual(expected, result,
                             "Solution failed on random data.")


if __name__ == '__main__':
    unittest.main()



