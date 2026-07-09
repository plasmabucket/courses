"""Tests for task 12."""

import unittest
import random
import task12


class Task12Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        votes_1: list[int] = [60, 10,  10, 15, 5]
        self.assertEqual("majority winner 1",
                         task12.MassVote(len(votes_1), votes_1),
                         "Solution is incorrect. "
                         "Couldn't determine majority winner.")
        votes_2: list[int] = [10, 15, 10]
        self.assertEqual("minority winner 2",
                         task12.MassVote(len(votes_2), votes_2),
                         "Solution is incorrect. "
                         "Couldn't determine minority winner.")
        votes_3: list[int] = [111, 111, 110, 110]
        self.assertEqual("no winner",
                         task12.MassVote(len(votes_3), votes_3),
                         "Solution is incorrect. "
                         "Couldn't determine no-winners case.")

    def test_null(self) -> None:
        """Tests solution on a case with a single candidate."""
        self.assertEqual("majority winner 1", task12.MassVote(1, [146]),
                         "Solution doesn't work in North Korea.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 10000 runs
        for i in range(10000):
            # Create a list with random values
            length: int = random.randint(1, 1000)
            votes: list[int] = []
            for j in range(length):
                votes.append(random.randint(1, 1000))
            # Determine the highest vote count and how many leaders there are
            lead_count: int = max(votes)
            leader_count: int = votes.count(lead_count)
            if leader_count > 1:
                expected: str = "no winner"
            else:
                total_votes: int = sum(votes)
                leader_index: int = votes.index(lead_count) + 1
                if lead_count * 2 <= total_votes:
                    expected = "minority winner " + str(leader_index)
                else:
                    expected = "majority winner " + str(leader_index)
            self.assertEqual(expected, task12.MassVote(length, votes),
                             f"Solution failed on random data. Run №{i}")


if __name__ == '__main__':
    unittest.main()



