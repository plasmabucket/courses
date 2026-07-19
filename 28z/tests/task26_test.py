"""Tests for task 26."""

import unittest
import task26


class Task26Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on known cases."""
        msg: str = "Solution is incorrect"
        self.assertTrue(task26.white_walkers("axxb6===4xaf5===eee5"), msg)
        self.assertTrue(task26.white_walkers("abc=7==hdjs=3gg1=======5"), msg)
        self.assertTrue(task26.white_walkers("9===1===9===1===9"), msg)
        self.assertFalse(task26.white_walkers("5==ooooooo=5=5"), msg)
        self.assertFalse(task26.white_walkers("aaS=8"), msg)

    def test_null(self) -> None:
        """Tests solution on shortest edge cases."""
        self.assertFalse(task26.white_walkers(""), "Empty string is unhandled.")
        self.assertFalse(task26.white_walkers("a"), "String with a single char is unhandled.")
        self.assertFalse(task26.white_walkers("1"), "String with a single digit is unhandled.")
        self.assertFalse(task26.white_walkers("="), "String with a single '=' is unhandled.")

    def test_large_string(self) -> None:
        """Tests solution on a large input string."""
        data: str = "5a==b=" * 100 + "5"
        self.assertTrue(task26.white_walkers(data), "Large string is unhandled.")

    def test_leading_trailing(self) -> None:
        """Tests solution in cases with leading or trailing characters."""
        self.assertTrue(task26.white_walkers("5===5"), "Fails on a leading/trailing digit.")

        self.assertFalse(task26.white_walkers("5==="), "Fails on a leading digit.")
        self.assertTrue(task26.white_walkers("a5===5"), "Fails on a leading char.")
        self.assertTrue(task26.white_walkers("=5===5"), "Fails on a leading '='.")

        self.assertFalse(task26.white_walkers("===5"), "Fails on a trailing digit.")
        self.assertTrue(task26.white_walkers("5===5a"), "Fails on a trailing char.")
        self.assertTrue(task26.white_walkers("5===5="), "Fails on a trailing '='.")


if __name__ == '__main__':
    unittest.main()



