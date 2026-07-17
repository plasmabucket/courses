"""Tests for task 23."""

import unittest
import random
import task23


class Task23Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        height: int = 3
        width: int = 4
        years: int = 4
        tree: list[str] = [".+..",
                           "..+.",
                           ".+.."]
        expected: list[str] = [".+..",
                               "..+.",
                               ".+.."]
        self.assertEqual(expected,
                         task23.TreeOfLife(height, width, years, tree),
                         "Solution is incorrect.")

    def test_even_year(self) -> None:
        """Tests that on every "even" year the tree is full ."""
        # Make 100 runs
        for i in range(100):
            height: int = random.randint(1, 10)
            width: int = random.randint(1, 10)
            tree: list[str] = []
            expected: list[str] = []
            for j in range(height):
                tree.append("".join(random.choices(".+", k=width)))
                expected.append("+" * width)

            for year in range(1, 100, 2):
                self.assertEqual(expected,
                                 task23.TreeOfLife(height, width, year, tree),
                                 "Tree isn't full on an 'even' year.")

    def test_small_tree(self) -> None:
        """Tests solution a tree of smallest size."""
        height: int = 1
        width: int = 1
        years: int = 4
        tree: list[str] = ["."]
        expected: list[str] = ["."]
        self.assertEqual(expected,
                         task23.TreeOfLife(height, width, years, tree),
                         "Smallest tree is unhandled.")
        tree = ["+"]
        expected = ["+"]
        self.assertEqual(expected,
                         task23.TreeOfLife(height, width, years, tree),
                         "Smallest tree is unhandled.")

    def test_grow_sequence(self) -> None:
        """Tests how solution calculates branch growth year by year."""
        # Initial tree contains a branch which affects all 4 neighbors
        # and a cell which has only branches as neighbors
        height: int = 5
        width: int = 5
        year: int = 0
        tree: list[str] = [".....",
                           ".+...",
                           ".....",
                           "....+",
                           "...+."]
        expected: list[str] = [".....",
                               ".+...",
                               ".....",
                               "....+",
                               "...+."]
        self.assertEqual(expected,
                         task23.TreeOfLife(height, width, year, tree),
                         f"Sequence: year {year} failed.")
        year += 2
        expected = ["+.+++",
                    "...++",
                    "+.++.",
                    "+++..",
                    "++..."]
        self.assertEqual(expected,
                         task23.TreeOfLife(height, width, year, tree),
                         f"Sequence: year {year} failed.")
        year += 2
        expected = [".....",
                    ".+...",
                    ".....",
                    "....+",
                    "...++"]
        self.assertEqual(expected,
                         task23.TreeOfLife(height, width, year, tree),
                         f"Sequence: year {year} failed.")
        year += 2
        expected = ["+.+++",
                    "...++",
                    "+.++.",
                    "+++..",
                    "++..."]
        self.assertEqual(expected,
                         task23.TreeOfLife(height, width, year, tree),
                         f"Sequence: year {year} failed.")
        year += 2
        expected = [".....",
                    ".+...",
                    ".....",
                    "....+",
                    "...++"]
        self.assertEqual(expected,
                         task23.TreeOfLife(height, width, year, tree),
                         f"Sequence: year {year} failed.")


if __name__ == '__main__':
    unittest.main()



