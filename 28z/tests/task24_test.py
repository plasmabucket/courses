"""Tests for task 24."""

import unittest
import random
import string
import task24


class Task24Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        height: int = 4
        width: int = 6
        data: list[str] = ["123456", "234567", "345678", "456789"]
        expected: list[str] = ["212345", "343456", "456767", "567898"]

        task24.MatrixTurn(data, height, width, 1)
        self.assertEqual(expected, data, "Solution is incorrect")

    def test_null(self) -> None:
        """Tests solution on the smallest matrix."""
        height: int = 2
        width: int = 2
        data: list[str] = ["12", "43"]
        expected: list[str] = ["41", "32"]

        task24.MatrixTurn(data, height, width, 1)
        self.assertEqual(expected, data, "Smallest matrix is unhandled.")

    def test_random(self) -> None:
        """Tests solution by checking if chars get cycled."""
        # Make 10000 runs
        for i in range(10000):
            dim: list[int] = []
            dim.append(random.randint(1, 10) * 2)  # Even number
            dim.append(random.randint(dim[0], 20))  # dim[1] >= dim[0]
            random.shuffle(dim)

            data: list[str] = []
            for m in range(dim[0]):
                data.append("".join(random.sample(
                    string.ascii_lowercase, dim[1])))

            x_rand: int = random.randint(0, dim[1] - 1)
            y_rand: int = random.randint(0, dim[0] - 1)
            target_char: str = data[y_rand][x_rand]

            # Calculate how many cycles do we have to do to get a char
            # back into it's original position
            target_ring: int = min(x_rand, dim[1] - 1 - x_rand,
                y_rand, dim[0] - 1 - y_rand)
            cycles: int = (dim[0] + dim[1] - 2) * 2 - target_ring * 8

            task24.MatrixTurn(data, dim[0], dim[1], cycles)
            self.assertEqual(target_char, data[y_rand][x_rand],
                             "Char didn't get cycled in a random matrix.")


if __name__ == '__main__':
    unittest.main()



