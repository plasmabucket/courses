"""Tests for task 21."""

import unittest
import task21


class Task21Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertEqual("", task21.BiggerGreater("fff"),
                         "Non-transformable words are unhandled.")
        self.assertEqual("nkml", task21.BiggerGreater("nklm"),
                         "Solution is incorrect.")
        self.assertEqual("ibck", task21.BiggerGreater("ckib"),
                         "Solution is incorrect.")

    def test_null(self) -> None:
        """Tests solution on shortest words."""
        self.assertEqual("za", task21.BiggerGreater("az"),
                         "Short words are unhandled.")
        self.assertEqual("", task21.BiggerGreater("za"),
                         "Short non-transformable words are unhandled.")

    def test_repeated_chars(self) -> None:
        """Tests solution on words with many repeated characters."""
        self.assertEqual("babbbb", task21.BiggerGreater("abbbbb"),
                         "Solution fails on repeated characters.")
        self.assertEqual("bbbbab", task21.BiggerGreater("bbbabb"),
                         "Solution fails on repeated characters.")
        self.assertEqual("", task21.BiggerGreater("bbbbba"),
                         "Non-transformable words with repeated characters "
                         "are unhandled")

    def test_long_word(self) -> None:
        """Tests solution on long words."""
        long_1: str = "a" + "b" * 1000
        long_2: str = "b" * 100 + "a" + "b" * 900
        long_3: str = "b" * 1000 + "a"
        expected_1: str = "b" + "a" + "b" * 999
        expected_2: str = "b" * 101 + "a" + "b" * 899
        expected_3: str = ""
        self.assertEqual(expected_1, task21.BiggerGreater(long_1),
                         "Solution fails on long words.")
        self.assertEqual(expected_2, task21.BiggerGreater(long_2),
                         "Solution fails on long words.")
        self.assertEqual(expected_3, task21.BiggerGreater(long_3),
                         "Long non-transformable words are unhandled.")


if __name__ == '__main__':
    unittest.main()



