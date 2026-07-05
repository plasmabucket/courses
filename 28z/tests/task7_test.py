"""Tests for task 7."""

import unittest
import task7


class Task7Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        length: int = 12
        string: str = ("1) строка разбивается на набор строк "
                       "через выравнивание по заданной ширине.")
        substring: str = "строк"
        answer: list[int] = [0, 0, 0, 1, 0, 0, 0]
        result: list[int] = task7.WordSearch(length, string, substring)
        self.assertEqual(len(answer), len(result),
                         "Line separation is incorrect.")
        self.assertEqual(answer, result, "Solution is incorrect.")

    def test_long_word(self) -> None:
        """Tests ability to split up long words to fit in the line size."""
        length: int = 10
        string: str = "123456789_10 12345678910 123456789_10"
        substring: str = "10"
        answer: list[int] = [0, 1, 0, 0, 0, 1]
        result: list[int] = task7.WordSearch(length, string, substring)
        self.assertEqual(answer, result, "Long words aren't split properly.")

    def test_short_words(self) -> None:
        """Tests how solution forms lines with many words."""
        length: int = 10
        string: str = ("1 2 3 4 5 "
                       "6 7 8 9 10 "
                       "11 12 13 "
                       "14 15 16 "
                       "17 18 19 "
                       "20")
        substring: str = "6"
        answer: list[int] = [0, 1, 0, 0, 0, 0]
        result: list[int] = task7.WordSearch(length, string, substring)
        self.assertEqual(answer, result,
                         "Spaces in formed lines aren't counted properly.")
        substring = "11"
        answer = [0, 0, 1, 0, 0, 0]
        result = task7.WordSearch(length, string, substring)
        self.assertEqual(answer, result,
                         "Lines aren't being formed correctly.")
        substring = "14"
        answer = [0, 0, 0, 1, 0, 0]
        result = task7.WordSearch(length, string, substring)
        self.assertEqual(answer, result,
                         "Lines aren't being formed correctly.")

    def test_null(self) -> None:
        """Tests solution on a one-symbol long string."""
        length: int = 10
        string: str = "1"
        substring: str = "10"
        answer: list[int] = [0]
        result: list[int] = task7.WordSearch(length, string, substring)
        self.assertEqual(answer, result,
                         "One-symbol long string is unhandled.")
        substring = "1"
        answer = [1]
        result = task7.WordSearch(length, string, substring)
        self.assertEqual(answer, result, "One-symbol match doesn't work.")

    def test_not_a_full_word(self) -> None:
        """Tests if match detection searches for whole words."""
        length: int = 3
        string: str = "100 10 110"
        substring: str = "10"
        answer: list[int] = [0, 1, 0]
        result: list[int] = task7.WordSearch(length, string, substring)
        self.assertEqual(answer, result, "Word match detection is incorrect.")

    def test_space_at_the_end(self) -> None:
        """Tests how space at the end of a string is handled."""
        length: int = 3
        string: str = "123 "
        substring: str = "123"
        result: list[int] = task7.WordSearch(length, string, substring)
        self.assertEqual(1, len(result),
                         "Space at the end creates an empty line.")

    def test_everything_in_one_line(self) -> None:
        """Tests solution when line length is bigger than the whole string."""
        length: int = 1000
        string: str = ("1) строка разбивается на набор строк "
                       "через выравнивание по заданной ширине.")
        substring: str = "строк"
        answer: list[int] = [1]
        result: list[int] = task7.WordSearch(length, string, substring)
        self.assertEqual(answer, result,
                         "Wrong answer when no string splits are needed.")


if __name__ == '__main__':
    unittest.main()



