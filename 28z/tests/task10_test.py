"""Tests for task 10."""

import unittest
import random
import task10


class Task10Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertEqual(210, task10.PrintingCosts(r"\Test string!"),
                         "Solution is incorrect.")

    def test_unknown_char(self) -> None:
        """Tests solution on a string with characters not in the table."""
        self.assertEqual(223, task10.PrintingCosts("Test string! №"),
                         "Unknown characters are unhandled.")

    def test_null(self) -> None:
        """Tests solution on strings of 0 and 1 length."""
        self.assertEqual(0, task10.PrintingCosts(""),
                         "String of zero length is unhandled.")
        self.assertEqual(19, task10.PrintingCosts("1"),
                         "String of length 1 is unhandled.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        cost_table: dict[str, int] = {
            " ": 0,  "!": 9,  '"': 6,  "#": 24, "$": 29, "%": 22, "&": 24,
            "'": 3,  "(": 12, ")": 12, "*": 17, "+": 13, ",": 7,  "-": 7,
            ".": 4,  "/": 10, "0": 22, "1": 19, "2": 22, "3": 23, "4": 21,
            "5": 27, "6": 26, "7": 16, "8": 23, "9": 26, ":": 8,  ";": 11,
            "<": 10, "=": 14, ">": 10, "?": 15, "@": 32, "A": 24, "B": 29,
            "C": 20, "D": 26, "E": 26, "F": 20, "G": 25, "H": 25, "I": 18,
            "J": 18, "K": 21, "L": 16, "M": 28, "N": 25, "O": 26, "P": 23,
            "Q": 31, "R": 28, "S": 25, "T": 16, "U": 23, "V": 19, "W": 26,
            "X": 18, "Y": 14, "Z": 22, "[": 18, "\\":10, "]": 18, "^": 7,
            "_": 8,  "`": 3,  "a": 23, "b": 25, "c": 17, "d": 25, "e": 23,
            "f": 18, "g": 30, "h": 21, "i": 15, "j": 20, "k": 21, "l": 16,
            "m": 22, "n": 18, "o": 20, "p": 25, "q": 25, "r": 13, "s": 21,
            "t": 17, "u": 17, "v": 13, "w": 19, "x": 13, "y": 24, "z": 19,
            "{": 18, "|": 12, "}": 18, "~": 9
        }
        # Make 1000 runs
        for i in range(1000):
            s_len: int = random.randint(0, 500)
            string: str = ""
            print_cost: int = 0
            for j in range(s_len):
                char: str = random.choice(list(cost_table))
                string += char
                print_cost += cost_table[char]
            self.assertEqual(print_cost, task10.PrintingCosts(string),
                             f"Solution failed on random data. Run №{i}")


if __name__ == '__main__':
    unittest.main()



