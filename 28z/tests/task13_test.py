"""Tests for task 13."""

import unittest
import random
import task13


class Task13Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertEqual([4660, 6007], task13.UFO(2, [1234, 1777], False),
                         "Solution in hexadecimal mode is incorrect.")
        self.assertEqual([668, 1023], task13.UFO(2, [1234, 1777], True),
                         "Solution is octal mode is incorrect.")

    def test_null(self) -> None:
        """Tests solution on empty and one-element lists."""
        # Empty list
        self.assertEqual([], task13.UFO(0, [], False),
                         "Empty list in hexadecimal mode is unhandled.")
        self.assertEqual([], task13.UFO(0, [], True),
                         "Empty list in octal mode is unhandled.")
        # One-element list
        self.assertEqual([1], task13.UFO(1, [1], False),
                         "List of one element in hexadecimal mode is unhandled.")
        self.assertEqual([1], task13.UFO(1, [1], True),
                         "List of one element in octal mode is unhandled.")

    def test_max(self) -> None:
        """Tests solution on huge integers."""
        self.assertEqual([2 ** 64 + 1],
                         task13.UFO(1, [10000000000000001], False),
                         "Long integers are unhandled in hexadecimal mode.")
        self.assertEqual([2 ** 63 + 1],
                         task13.UFO(1, [1000000000000000000001], True),
                         "Long integers are unhandled in octal mode.")

    def test_random_hex(self) -> None:
        """Tests solution in hexadecimal mode on random data."""
        # Make 1000 runs
        BASE: int = 16
        for i in range(1000):
            length: int = random.randint(1, 1000)
            data: list[int] = []
            expected: list[int] = []
            for j in range(length):
                num_length: int = random.randint(1, 10)
                num_str: list[str] = []
                decoded_num: int = 0
                for k in range(num_length):
                    if k == 0:
                        digit: int = random.randint(1, 9)
                    else:
                        digit = random.randint(0, 9)
                    decoded_num += digit * BASE ** k
                    num_str.insert(0, str(digit))
                num: int = int("".join(num_str))
                expected.append(decoded_num)
                data.append(num)
            self.assertEqual(expected, task13.UFO(length, data, False),
                "Solution in hexadecimal mode failed on random data.")

    def test_random_octal(self) -> None:
        """Tests solution in octal mode on random data."""
        # Make 1000 runs
        BASE: int = 8
        for i in range(1000):
            length: int = random.randint(1, 1000)
            data: list[int] = []
            expected: list[int] = []
            for j in range(length):
                num_length: int = random.randint(1, 10)
                num_str: list[str] = []
                decoded_num: int = 0
                for k in range(num_length):
                    if k == 0:
                        digit: int = random.randint(1, 7)
                    else:
                        digit = random.randint(0, 7)
                    decoded_num += digit * BASE ** k
                    num_str.insert(0, str(digit))
                num: int = int("".join(num_str))
                expected.append(decoded_num)
                data.append(num)
            self.assertEqual(expected, task13.UFO(length, data, True),
                "Solution in octal mode failed on random data.")


if __name__ == '__main__':
    unittest.main()



