"""Tests for task 19."""
import string
import unittest
import random
import task19


class Task19Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        data: list[str] = ["dress1 5",
                           "bag32 2",
                           "dress1 1",
                           "bag23 2",
                           "bag128 4"]
        expected: list[str] = ["dress1 6",
                               "bag128 4",
                               "bag23 2",
                               "bag32 2"]
        self.assertEqual(expected, task19.ShopOLAP(len(data), data),
                         "Solution is incorrect.")

    def test_null(self) -> None:
        """Tests solution on the shortest list."""
        data: list[str] = ["a 1"]
        expected: list[str] = ["a 1"]
        self.assertEqual(expected, task19.ShopOLAP(len(data), data),
                         "Solution failed on the list of size 1.")

    def test_ordering(self) -> None:
        """Tests how solution handles ordering of the list."""
        # Only lexicographical ordering
        data_lex: list[str] = [char + " 1" for char in
                               reversed(string.ascii_lowercase)]
        expected_lex: list[str] = list(reversed(data_lex))
        self.assertEqual(expected_lex, task19.ShopOLAP(len(data_lex), data_lex),
                         "Solution foiled on lexicographic ordering.")

        # Only numerical ordering
        data_num: list[str] = [char + " " + str(i) for i, char in
                               enumerate(string.ascii_lowercase)]
        expected_num: list[str] = list(reversed(data_num))
        self.assertEqual(expected_num, task19.ShopOLAP(len(data_num), data_num),
                         "Solution failed on numerical ordering.")

        # Numerical and lexicographical ordering
        data_mixed: list[str] = [char + " " + str(i % 2 + 1) for i, char in
                                 enumerate(string.ascii_lowercase)]
        expected_mixed: list[str] = []
        for i in range(1, len(string.ascii_lowercase), 2):
            expected_mixed.append(string.ascii_lowercase[i] + " 2")
        for i in range(0, len(string.ascii_lowercase), 2):
            expected_mixed.append(string.ascii_lowercase[i] + " 1")
        self.assertEqual(expected_mixed, task19.ShopOLAP(len(data_mixed), data_mixed),
                         "Solution failed on mixed ordering.")

    def test_deduplication(self) -> None:
        """Tests how solution sums duplicate entries."""
        # Make 1000 runs
        for i in range(1000):
            sum_a: int = 0
            sum_b: int = 0
            data: list[str] = ["a 0", "b 0"]
            for i in range(random.randint(0, 100)):
                rand_num: int = random.randint(1, 100)
                if random.randint(0, 1) == 0:
                    data.append("a " + str(rand_num))
                    sum_a += rand_num
                else:
                    data.append("b " + str(rand_num))
                    sum_b += rand_num
            actual: list[str] = task19.ShopOLAP(len(data), data)
            self.assertEqual(2, len(actual), "Deduplication failed.")
            self.assertEqual(max(sum_a, sum_b), int(actual[0].split()[1]),
                             "Summation failed during deduplication.")
            self.assertEqual(min(sum_a, sum_b), int(actual[1].split()[1]),
                             "Summation failed during deduplication.")

    def test_side_effects(self) -> None:
        """Tests if the solution mutates its parameters."""
        # Make 100 runs
        for i in range(100):
            data: list[str] = ["a 0", "b 0"]
            for i in range(random.randint(0, 100)):
                rand_num: int = random.randint(1, 100)
                if random.randint(0, 1) == 0:
                    data.append("a " + str(rand_num))
                else:
                    data.append("b " + str(rand_num))
            data_copy: list[str] = data.copy()
            task19.ShopOLAP(len(data), data)
            self.assertEqual(data_copy, data, "Solution mutates parameters.")


if __name__ == '__main__':
    unittest.main()



