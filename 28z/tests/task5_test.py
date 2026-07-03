"""Tests for task 5."""

import unittest
import random
import task5


class Task5Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        n: int = 3
        ids: list[int] = [50, 1, 1024]
        salaries: list[int] = [20000, 100000, 90000]
        self.assertEqual([90000, 20000, 100000],
                         task5.SynchronizingTables(n, ids, salaries),
                         "Solution is incorrect.")

    def test_argument_mutation(self) -> None:
        """Tests if a solution mutates its parameters."""
        n: int = 3
        ids: list[int] = [50, 1, 1024]
        salaries: list[int] = [20000, 100000, 90000]
        task5.SynchronizingTables(n, ids, salaries)
        self.assertEqual([50, 1, 1024], ids,
                         "List of ids got mutated.")
        self.assertEqual([20000, 100000, 90000], salaries,
                         "List of salaries got mutated.")

    def test_null(self) -> None:
        """Tests solution on a zero- and one-length lists."""
        n: int = 0
        ids: list[int] = []
        salaries: list[int] = []
        self.assertEqual([], task5.SynchronizingTables(n, ids, salaries),
                         "Zero-length list is unhandled.")
        n = 1
        ids = [1]
        salaries = [2]
        self.assertEqual([2], task5.SynchronizingTables(n, ids, salaries),
                         "One-length list is unhandled.")

    def test_big_list(self) -> None:
        """Tests solution on a huge list."""
        n: int = 10000  # Size of list
        commutation_list: list[int] = random.sample(range(n), n)
        ids: list[int] = []
        salaries: list[int] = []
        i: int
        for i in range(n):
            ids.append(1 + commutation_list[i])
            salaries.append((1 + commutation_list[i]) * 1000)
        salaries_shuffled: list[int] = random.sample(salaries, n)
        result: list[int] = task5.SynchronizingTables(n, ids,
                                                      salaries_shuffled)
        self.assertEqual(salaries, result,
                         "Big list is unhandled")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 10000 runs
        for i in range(10000):
            # Number of elements in lists
            n: int = random.randint(1, 500)
            # Create sorted lists for correct 1-1 correspondence
            ids_clear: list[int] = list(range(1, n + 1))
            salaries_clear: list[int] = [100 * random.randint(1, n)
                                         for k in range(n)]
            salaries_clear.sort()
            # From sorted lists create randomly sorted ones
            ids: list[int] = []
            salaries: list[int] = []
            commutation_list: list[int] = random.sample(range(n), n)
            j: int
            for j in range(n):
                # Use commutation list to keep element correspondence
                # between two lists
                ids.append(ids_clear[commutation_list[j]])
                salaries.append(salaries_clear[commutation_list[j]])
            # Shuffle the salary list before sending it to the solution
            salaries_shuffled: list[int] = random.sample(salaries, n)
            # The answer should be a salary list before the shuffle
            result: list[int] = task5.SynchronizingTables(n, ids,
                                                          salaries_shuffled)
            self.assertEqual(salaries, result,
                             f"Solution failed on random data. Run №{i}")


if __name__ == '__main__':
    unittest.main()



