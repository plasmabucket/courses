"""Tests for task 16."""

import unittest
import random
import sys
import task16


class Task16Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        prices: list[int] = [400, 300, 250]
        self.assertEqual(250, task16.MaximumDiscount(len(prices), prices),
                         "Solution is incorrect.")
        prices2: list[int] = [400, 350, 300, 250, 200, 150, 100]
        self.assertEqual(450, task16.MaximumDiscount(len(prices2), prices2),
                         "Solution is incorrect.")

    def test_null(self) -> None:
        """Tests solution on empty list and a one-element list."""
        prices0: list[int] = []
        self.assertEqual(0, task16.MaximumDiscount(0, prices0),
                         "Empty list is unhandled.")
        prices1: list[int] = [100]
        self.assertEqual(0, task16.MaximumDiscount(1, prices1),
                         "List with one element is unhandled.")

    def test_max(self) -> None:
        """Test solution on a list with huge integers."""
        prices_huge: list[int] = [sys.maxsize + 3, sys.maxsize + 2,
                                  sys.maxsize + 1, 0]
        self.assertEqual(sys.maxsize + 1,
                         task16.MaximumDiscount(len(prices_huge), prices_huge),
                         "Big integers are unhandled.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 100 runs
        for i in range(100):
            # Create a list with random prices
            length: int = random.randint(1, 50)
            prices_rand: list[int] = []
            for j in range(length):
                prices_rand.append(random.randint(1, 1000))
            # Go through random combinations and determine their discount
            max_discount_found: int = 0
            for j in range(10000):
                random.shuffle(prices_rand)
                discount: int = 0
                for k in range(0, length - length % 3, 3):
                    discount += min(prices_rand[k],
                                    prices_rand[k+1],
                                    prices_rand[k+2])
                max_discount_found = max(max_discount_found, discount)
            # Compare what we found randomly to the solution
            self.assertLessEqual(max_discount_found,
                                 task16.MaximumDiscount(length, prices_rand),
                                 f"Solution isn't optimal. Run №{i}")


if __name__ == '__main__':
    unittest.main()



