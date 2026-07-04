"""Tests for task 6."""

import unittest
import random
import math
from typing import Final
import task6


class Task6Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        result: str = task6.PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9])
        self.assertEqual("982843", result, "Solution is incorrect.")

    def test_null(self) -> None:
        """Tests solution on lists of 0, 1 and 2 elements."""
        result0: str = task6.PatternUnlock(0, [])
        result1: str = task6.PatternUnlock(1, [2])
        result2: str = task6.PatternUnlock(2, [2, 3])
        self.assertEqual("", result0, "Empty list is unhandled.")
        self.assertEqual("", result1, "List of 1 element is unhandled.")
        self.assertEqual("1", result2, "Single-length path is unhandled.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        ROOT_2: Final[float] = math.sqrt(2)  # Diagonal line length
        # Map of coordinates and numbers
        grid: dict[tuple[int, int], int] = {(0, 0): 6, (0, 1): 1, (0, 2): 9,
                                            (1, 0): 5, (1, 1): 2, (1, 2): 8,
                                            (2, 0): 4, (2, 1): 3, (2, 2): 7}
        # Make 10000 runs
        for i in range(10000):
            # Generate a number sequence
            sequence_len: int = random.randint(2, 200)
            generated_len: int = 0  # Counter for a while loop
            sequence: list[int] = []  # Stores button sequence
            line_len: float = 0.0  # Length of drawn line
            # Coordinates of a button on a grid
            # First button number is generated directly
            x_coord: int = random.randint(0, 2)
            y_coord: int = random.randint(0, 2)
            sequence.append(grid[(x_coord, y_coord)])
            generated_len += 1
            # Generate other button numbers through movement deltas
            while generated_len < sequence_len:
                # Movement is allowed only to adjacent buttons
                x_delta: int = random.randint(-1, 1)
                y_delta: int = random.randint(-1, 1)
                # Zero movement is not allowed
                # Movement beyond borders is not allowed
                if (x_delta == 0 and y_delta == 0 or
                        (x_coord + x_delta) < 0 or (x_coord + x_delta) > 2 or
                        (y_coord + y_delta) < 0 or (y_coord + y_delta) > 2):
                    continue
                # If deltas are correct, update coords
                x_coord += x_delta
                y_coord += y_delta
                # Correctly generated number is added to a sequences
                sequence.append(grid[(x_coord, y_coord)])
                # Line length is updated
                if abs(x_delta) + abs(y_delta) > 1:
                    line_len += ROOT_2
                else:
                    line_len += 1
                generated_len += 1
            # Password is obtained via line length
            password: str = str(round(line_len, 5)).replace(".", "")
            password = password.replace("0", "")
            self.assertEqual(password,
                             task6.PatternUnlock(sequence_len, sequence),
                             f"Solution failed on random data. Run №{i}")

    def test_big_list(self) -> None:
        """Tests solution on a big list."""
        ROOT_2: Final[float] = math.sqrt(2)  # Diagonal line length
        # Map of coordinates and numbers
        grid: dict[tuple[int, int], int] = {(0, 0): 6, (0, 1): 1, (0, 2): 9,
                                            (1, 0): 5, (1, 1): 2, (1, 2): 8,
                                            (2, 0): 4, (2, 1): 3, (2, 2): 7}
        # Generate a number sequence
        sequence_len: int = 10000  # Make a huge-sized list
        generated_len: int = 0  # Counter for a while loop
        sequence: list[int] = []  # Stores button sequence
        line_len: float = 0.0  # Length of drawn line
        # Coordinates of a button on a grid
        # First button number is generated directly
        x_coord: int = random.randint(0, 2)
        y_coord: int = random.randint(0, 2)
        sequence.append(grid[(x_coord, y_coord)])
        generated_len += 1
        # Generate other button numbers through movement deltas
        while generated_len < sequence_len:
            # Movement is allowed only to adjacent buttons
            x_delta: int = random.randint(-1, 1)
            y_delta: int = random.randint(-1, 1)
            # Zero movement is not allowed
            # Movement beyond borders is not allowed
            if (x_delta == 0 and y_delta == 0 or
                    (x_coord + x_delta) < 0 or (x_coord + x_delta) > 2 or
                    (y_coord + y_delta) < 0 or (y_coord + y_delta) > 2):
                continue
            # If deltas are correct, update coords
            x_coord += x_delta
            y_coord += y_delta
            # Correctly generated number is added to a sequences
            sequence.append(grid[(x_coord, y_coord)])
            # Line length is updated
            if abs(x_delta) + abs(y_delta) > 1:
                line_len += ROOT_2
            else:
                line_len += 1
            generated_len += 1
        # Password is obtained via line length
        password: str = str(round(line_len, 5)).replace(".", "")
        password = password.replace("0", "")
        self.assertEqual(password,
                         task6.PatternUnlock(sequence_len, sequence),
                         "Big list is unhandled.")


if __name__ == '__main__':
    unittest.main()



