"""Tests for task 22."""

import unittest
import random
import string
import task22


class Task22Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertTrue(task22.SherlockValidString("xyz"),
                        "String with all valid chars is not valid.")
        self.assertTrue(task22.SherlockValidString("xyzaa"),
                        "Char count decrement is not valid.")
        self.assertTrue(task22.SherlockValidString("xxyyz"),
                        "Char removal is not valid.")

        self.assertFalse(task22.SherlockValidString("xyzzz"),
                         "Multi char count decrement is recognised as valid.")
        self.assertFalse(task22.SherlockValidString("xxyyza"),
                         "Multiple char removals are recognised as valid.")
        self.assertFalse(task22.SherlockValidString("xxyyzabc"),
                         "Multiple char frequencies are recognised as valid.")

    def test_short_string(self) -> None:
        """Tests solution on shortest strings."""
        self.assertTrue(task22.SherlockValidString("ab"),
                        "Shortest string is unhandled.")
        self.assertTrue(task22.SherlockValidString("aa"),
                        "Shortest string is unhandled.")

    def test_large_string(self) -> None:
        """Tests solution on large stings."""
        str_1: str = "a" * 1000 + "b"
        str_2: str = "a" * 1000 + "bb"
        self.assertTrue(task22.SherlockValidString(str_1),
                        "Large strings are unhandled.")
        self.assertFalse(task22.SherlockValidString(str_2),
                         "Large strings are unhandled.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 10000 runs
        for i in range(10000):
            # Generate a valid string
            char_count: int = random.randint(1, 26)
            chars: list[str] = random.sample(string.ascii_lowercase, char_count)
            segment_len: int = random.randint(1, 10)
            if char_count == 1:  # Min string length is 2
                segment_len = random.randint(2, 10)
            seq_1: str = ""  # Segment sequence
            for char in chars:
                seq_1 += char * segment_len
            # Add a single char in half of cases
            plus_one: int = bool(random.randint(0, 1))
            single_char: str = ""
            if plus_one:
                single_char = random.choice(string.ascii_lowercase)
            valid_list = list(seq_1 + single_char)
            random.shuffle(valid_list)
            valid_str: str = "".join(valid_list)

            self.assertTrue(task22.SherlockValidString(valid_str),
                            f"Solution failed on valid random data.\n"
                            f"{valid_str} was considered False")

            # Do not generate another sequence if all chars are used
            if char_count == 26:
                continue
            # Generate a second valid sequence with different segment length
            char_count_2: int = random.randint(1, 26 - char_count)
            free_chars: list[str] = []
            for char in string.ascii_lowercase:
                if char not in chars:
                    free_chars.append(char)
            chars_2: list[str] = random.sample(free_chars, char_count_2)
            # Segment length should be different from the original sequence
            segment_len_2: int = random.randint(1, 10)
            while segment_len_2 == segment_len:
                segment_len_2 = random.randint(1, 10)
            # Quit if we generated a single character
            if char_count_2 == 1 and segment_len_2 == 1:
                continue
            # Quit if the original sequence could be modified to make a string valid
            if char_count == 1 and segment_len == segment_len_2 + 1:
                continue
            # Quit if this sequence could be modified to make a string valid
            if char_count_2 == 1 and segment_len_2 == segment_len + 1:
                continue
            seq_2: str = ""
            for char in chars_2:
                seq_2 += char * segment_len_2
            invalid_list: list[str] = list(seq_1 + seq_2)
            random.shuffle(invalid_list)
            invalid_str: str = "".join(invalid_list)

            self.assertFalse(task22.SherlockValidString(invalid_str),
                             f"Solution failed on invalid random data.\n"
                             f"{invalid_str} was considered True")

    def test_errors(self) -> None:
        """Tests solution on error cases uncovered by random test."""
        self.assertTrue(task22.SherlockValidString("uusss"),
                        "target_len+1 is unhandled when target_len is formed "
                        "by a single char sequence.")


if __name__ == '__main__':
    unittest.main()



