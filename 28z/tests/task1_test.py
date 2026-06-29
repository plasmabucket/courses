"""Tests for task 1."""

import unittest
import math
from random import randint
import task1


class Task1Tests(unittest.TestCase):
    """Unittest class"""

    def test_zero_to_five(self) -> None:
        """Tests factorial calculation of numbers from 0 to 5."""
        i: int
        for i in range(5):
            fact: int = math.factorial(i)
            first_digit: int = int(str(fact)[0])
            self.assertEqual(task1.squirrel(i), first_digit,
                             f"Factorial of {i} is {fact}")

    def test_random(self) -> None:
        """Tests results on random numbers."""
        i: int
        for i in range(1000):
            random_num: int = randint(0, 1000)
            fact: int = math.factorial(random_num)
            first_digit: int = int(str(fact)[0])
            self.assertEqual(task1.squirrel(random_num), first_digit,
                             "First digit of the factorial is not correct")


if __name__ == '__main__':
    unittest.main()


