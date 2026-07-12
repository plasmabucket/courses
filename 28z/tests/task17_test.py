"""Tests for task 17."""

import unittest
import random
import task17


class Task17Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on known cases."""
        msg = "Solution is incorrect."
        # Correct lines
        self.assertTrue(task17.LineAnalysis("*..*..*..*..*..*..*"), msg)
        self.assertTrue(task17.LineAnalysis("*.......*.......*"), msg)
        # Incorrect lines
        self.assertFalse(task17.LineAnalysis("*..*...*..*..*..*..*"), msg)
        self.assertFalse(task17.LineAnalysis("*..*..*..*..*..**..*"), msg)

    def test_null(self) -> None:
        """Tests solution on shortest lines."""
        self.assertTrue(task17.LineAnalysis("*"), "Single star is unhandled.")
        self.assertTrue(task17.LineAnalysis("**"), "Single empty segment is unhandled.")
        self.assertTrue(task17.LineAnalysis("*.*"), "Single segment is unhandled.")
        self.assertTrue(task17.LineAnalysis("***"), "Empty segments are unhandled.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 10000 runs
        for i in range(10000):
            segments: int = random.randint(1, 100)
            segment_len: int = random.randint(0, 100)
            line: str = "*" + ("." * segment_len + "*") * segments

            correct: bool = True
            # Corrupt the line pattern
            if random.randint(0, 1) == 0:
                correct = False
                wrong_len: int = random.randint(0, 100)
                while wrong_len == segment_len:
                    wrong_len = random.randint(0, 100)
                wrong_segment: str = "*" + "." * wrong_len + "*"
                insert_index: int = random.randint(0, len(line))
                line_list: list[str] = list(line)
                line_list.insert(insert_index, wrong_segment)
                line = "".join(line_list)

            self.assertEqual(correct, task17.LineAnalysis(line),
                             f"Solution failed on random data. Run №{i}")


if __name__ == '__main__':
    unittest.main()



