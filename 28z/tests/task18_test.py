"""Tests for task 18."""

import unittest
import random
import task18


class Task18Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        data_true: list[int] = [1, 3, 4, 5, 6, 2, 7]
        self.assertTrue(task18.MisterRobot(len(data_true), data_true),
                        "Solution is incorrect. "
                        "Sortable list returns false.")
        data_false: list[int] = [1, 3, 4, 5, 6, 7, 2]
        self.assertFalse(task18.MisterRobot(len(data_false), data_false),
                         "Solution is incorrect. "
                         "Unsortable list returns true.")

    def test_null(self) -> None:
        """Tests solution on shortest lists."""
        self.assertTrue(task18.MisterRobot(4, [1, 2, 3, 4]),
                        "Already sorted list is unhandled.")
        self.assertFalse(task18.MisterRobot(4, [1, 2, 4, 3]),
                         "Short list is unhandled.")

    def test_side_effects(self) -> None:
        """Tests if the solution changes it's parameters."""
        # Make 100 runs
        for i in range(100):
            length: int = random.randint(4, 100)
            data_original: list[int] = list(range(1, length + 1))
            random.shuffle(data_original)
            data_copy = data_original.copy()
            task18.MisterRobot(length, data_copy)
            self.assertEqual(data_original, data_copy,
                             "Solution has side effects.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 10000 runs
        for i in range(10000):
            # Create a list of numbers
            length: int = random.randint(4, 100)
            data: list[int] = list(range(1, length + 1))
            sortable: bool = bool(random.randint(0, 1))
            if not sortable:
                data[0], data[1] = data[1], data[0]
            # Scramble the list
            for j in range(random.randint(0, 1000)):
                ind: int = random.randint(1, length - 2)
                data[ind-1], data[ind], data[ind+1] = (data[ind],
                                                       data[ind+1],
                                                       data[ind-1])
            # Compare the results
            self.assertIs(sortable, task18.MisterRobot(length, data),
                          f"Solution failed on random data. Run №{i}")


if __name__ == '__main__':
    unittest.main()



