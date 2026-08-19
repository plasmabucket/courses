"""Tests for task 6."""

import unittest
import random
import string
from task6 import Deque
from task6_2 import is_palindrome, bracket_balance, DequeExtra, DequeDynamic


def deq_equal(deq1: Deque, deq2: Deque) -> bool:
    """Function to help determine deque equality. Also checks deque sizes."""
    if deq1.size() != deq2.size():
        return False
    for i in range(deq1.size()):
        if deq1.removeFront() != deq2.removeFront():
            return False
    return True


def dyn_deq_equal(deq1: Deque, deq2: DequeDynamic) -> bool:
    """Function to help compare deques and dynamic deques."""
    if deq1.size() != deq2.size:
        return False
    for i in range(deq1.size()):
        if deq1.removeFront() != deq2.remove_front():
            return False
    return True


class Task6MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Tests for the front addition
    def test_addFront(self) -> None:
        """Tests addition to the deque front on a regular and common case."""
        deque: Deque = Deque()
        for i in range(10):
            deque.addFront(i)

        self.assertEqual(10, deque.size(),
            "Deque size after addFront() is incorrect.")
        for i in range(10):
            self.assertEqual(9 - i, deque.removeFront(),
                "addFront() is incorrect.")

    def test_addFront_null(self) -> None:
        """Tests addition to the front of an empty deque."""
        deque: Deque = Deque()
        self.assertEqual(0, deque.size(),
            "Deque is initialized with non-zero size.")

        deque.addFront(6)
        self.assertEqual(1, deque.size(),
            "Empty deque size after addFront() is incorrect.")
        self.assertEqual(6, deque.removeFront(),
            "addFront() on an empty deque is incorrect.")

    def test_addFront_single(self) -> None:
        """Tests addition to the front of a single-element deque."""
        deque: Deque = Deque()
        deque.addFront(1)

        deque.addFront(2)

        self.assertEqual(2, deque.size(),
            "Single-element deque size after addFront() is incorrect.")
        self.assertEqual(2, deque.removeFront(),
            "addFront() an a single-element deque is incorrect.")

    def test_addFront_many(self) -> None:
        """Tests addition to the front of a large deque."""
        deque: Deque = Deque()
        size: int = 10000
        for i in range(size):
            deque.addFront(i)

        self.assertEqual(size, deque.size(),
            "Large deque size after addFront() is incorrect.")
        for i in range(size):
            self.assertEqual(size - 1 - i, deque.removeFront(),
                "addFront() on a large deque is incorrect.")

    # Tests for the front removal
    def test_removeFront(self) -> None:
        """Tests removal from the deque front on a regular and common case."""
        deque: Deque = Deque()
        for i in range(10):
            deque.addFront(i)

        result: int = deque.removeFront()

        self.assertEqual(9, deque.size(),
            "Deque size after removeFront() incorrect.")
        self.assertEqual(9, result,
            "removeFront() returned an incorrect element.")

    def test_removeFront_null(self) -> None:
        """Tests removal from the front of an empty deque."""
        deque: Deque = Deque()

        result: None = deque.removeFront()
        self.assertEqual(0, deque.size(),
            "Empty deque size after removeFront() is incorrect.")
        self.assertIsNone(result,
            "removeFront() on an empty deque didn't return None.")

    def test_removeFront_single(self) -> None:
        """Tests removal from the front of a single-element deque."""
        deque: Deque = Deque()
        deque.addFront(6)

        result: int = deque.removeFront()

        self.assertEqual(0, deque.size(),
            "Single-element deque size after removeFront() is incorrect.")
        self.assertEqual(6, result,
            "removeFront() on a single-element deque "
            "returned an incorrect element.")

    def test_removeFront_many(self) -> None:
        """Tests removal from the front of a large deque."""
        deque: Deque = Deque()
        size: int = 10000
        for i in range(10000):
            deque.addFront(i)

        result: int = deque.removeFront()

        self.assertEqual(size - 1, deque.size(),
            "Large deque size after removeFront() is incorrect.")
        self.assertEqual(size - 1, result,
            "removeFront() on a large deque returned an incorrect element.")

    # Tests for the tail addition
    def test_addTail(self) -> None:
        """Tests addition to the deque tail on a regular and common case."""
        deque: Deque = Deque()
        for i in range(10):
            deque.addFront(i)
        deque.addTail(6)

        expected: Deque = Deque()
        expected.addFront(6)
        for i in range(10):
            expected.addFront(i)

        self.assertTrue(deq_equal(expected, deque),
            "addTail() is incorrect.")

    def test_addTail_null(self) -> None:
        """Tests addition to the tail of an empty deque"""
        deque: Deque = Deque()
        deque.addTail(6)

        expected: Deque = Deque()
        expected.addFront(6)

        self.assertTrue(deq_equal(expected, deque),
            "addTail() on an empty deque is incorrect.")

    def test_addTail_single(self) -> None:
        """Tests addition to the tail of a single-element deque."""
        deque: Deque = Deque()
        deque.addFront(1)
        deque.addTail(0)

        expected: Deque = Deque()
        for i in range(2):
            expected.addFront(i)

        self.assertTrue(deq_equal(expected, deque),
            "addTail() on a single-element deque is incorrect.")

    def test_addTail_many(self) -> None:
        """Tests addition to the tail of a large deque."""
        deque: Deque = Deque()
        size: int = 10000
        for i in range(size):
            deque.addFront(i)
        deque.addTail(6)

        expected: Deque = Deque()
        expected.addFront(6)
        for i in range(size):
            expected.addFront(i)

        self.assertTrue(deq_equal(expected, deque),
            "addTail() on a large deque is incorrect.")

    # Tests for the tail removal
    def test_removeTail(self) -> None:
        """Tests removal from the deque tail on a regular and common case."""
        deque: Deque = Deque()
        for i in range(10):
            deque.addFront(i)
        result: int = deque.removeTail()

        expected: Deque = Deque()
        for i in range(1, 10):
            expected.addFront(i)

        self.assertEqual(0, result,
            "removeTail() returned an incorrect element.")
        self.assertTrue(deq_equal(expected, deque),
            "removeTail() is incorrect.")

    def test_removeTail_null(self) -> None:
        """Tests removal from tail of an empty deque."""
        deque: Deque = Deque()
        result: None = deque.removeTail()

        expected: Deque = Deque()

        self.assertIsNone(result,
            "removeTail() on an empty deque didn't return None.")
        self.assertTrue(deq_equal(expected, deque),
            "removeTail() on an empty deque is incorrect.")

    def test_removeTail_single(self) -> None:
        """Tests removal from tail of a single-element deque."""
        deque: Deque = Deque()
        deque.addFront(6)
        result: int = deque.removeTail()

        expected: Deque = Deque()

        self.assertEqual(6, result,
            "removeTail() on a single-element deque "
            "returned an incorrect element.")
        self.assertTrue(deq_equal(expected, deque),
            "removeTail() on a single-element deque is incorrect.")

    def test_removeTail_many(self) -> None:
        """Tests removal from the tail of a large deque."""
        deque: Deque = Deque()
        size: int = 10000
        for i in range(size):
            deque.addFront(i)
        result: int = deque.removeTail()

        expected: Deque = Deque()
        for i in range(1, size):
            expected.addFront(i)

        self.assertEqual(0, result,
            "removeTail() on a large deque returned an incorrect element.")
        self.assertTrue(deq_equal(expected, deque),
            "removeTail() on a large deque is incorrect.")


class Task6ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Tests for the determination of palindromes (ex 7.3.*)
    def test_palindrome(self) -> None:
        """Tests palindrome determination on a common case."""
        words: list[str] = [
            "not_a_palindrome",
            "palindromeemordnilap",
            "palindromemordnilap"
        ]
        self.assertFalse(is_palindrome(words[0]),
            "Non-palindrome got flagged as a palindrome.")
        self.assertTrue(is_palindrome(words[1]),
            "Palindrome got flagged as a non-palindrome.")
        self.assertTrue(is_palindrome(words[2]),
            "Palindrome with odd amount of letters got flagged "
            "as a non-palindrome")

    def test_palindrome_null(self) -> None:
        """Tests palindrome determination on an empty string."""
        self.assertTrue(is_palindrome(""),
            "Empty string got flagged as a non-palindrome.")

    def test_palindrome_single(self) -> None:
        """Tests palindrome determination on a single-char string."""
        self.assertTrue(is_palindrome("a"),
            "Single-char string got flagged as non-palindrome.")

    def test_palindrome_many(self) -> None:
        """Tests palindrome determination on a large string."""
        # Run 1000 times
        for i in range(1000):
            length: int = random.randint(2, 52)
            word: str = "".join(random.sample(string.ascii_letters, length))
            self.assertFalse(is_palindrome(word * 100),
                "Large non-palindrome got flagged as a palindrome.")

            mirrored: list[str] = list(word)
            mirrored.reverse()
            word += "".join(mirrored)
            self.assertTrue(is_palindrome(word * 100),
                "Large palindrome got flagged as a non-palindrome.")

    # Tests for bracket balance determination (ex 7.6.*)
    def test_balance_balanced(self) -> None:
        """Tests determination of balance on a balanced case."""
        brackets: list[str] = [
            "()",
            "(())",
            "()()",
            "(()())",
            "()" * 100,
            "(" * 100 + ")" * 100
        ]
        for case in brackets:
            self.assertTrue(bracket_balance(case),
                f"Balanced brackets were flagged as imbalanced. Case: {case}")

    def test_balance_null(self) -> None:
        """Tests determination of balance on an empty string."""
        case: str = ""
        self.assertTrue(bracket_balance(case),
            "Empty string was flagged as imbalanced.")

    def test_balance_close(self) -> None:
        """Tests determination of imbalance on a close-imbalanced case."""
        brackets: list[str] = [
            ")",
            "())",
            ")()",
            ")("
            "())(",
            ")()(",
            "()" * 100 + ")",
            "(" * 100 + ")" * 101
        ]
        for case in brackets:
            self.assertFalse(bracket_balance(case),
                f"Imbalanced closing brackets weren't caught. Case: {case}")

    def test_balance_open(self) -> None:
        """Tests determination of imbalance on an open-imbalanced case."""
        brackets: list[str] = [
            "(",
            "()(",
            "(()",
            "((",
            "(())(",
            "(()()",
            "(" + "()" * 100,
            "(" * 101 + ")" * 100
        ]
        for case in brackets:
            self.assertFalse(bracket_balance(case),
                f"Imbalanced opening brackets weren't caught. Case: {case}")

    def test_balance_multi_balanced(self) -> None:
        """Tests determination of balance with multiple bracket types."""
        brackets: list[str] = [
            "()[]{}",
            "([{}])",
            "{([])}",
            "{([])[()]}",
            "[]" * 100,
            "[" * 100 + "]" * 100,
            "{}" * 100,
            "{" * 100 + "}" * 100
        ]
        for case in brackets:
            self.assertTrue(bracket_balance(case),
                f"Balanced brackets were flagged as imbalanced. Case: {case}")

    def test_balance_multi_imbalanced(self) -> None:
        """Tests determination of imbalance with multiple bracket types."""
        brackets: list[str] = [
            "[", "]",
            "[]]", "[[]",
            "{", "}",
            "{{}", "{}}",
            "([}{])",
            "(]",
            "[)(]",
            "([)(])[{][}]",
        ]
        for case in brackets:
            self.assertFalse(bracket_balance(case),
                f"Imbalanced brackets weren't caught. Case: {case}")

    # Tests for finding the minimal element of the deque (ex 7.4.*)
    def test_minimum(self) -> None:
        """Tests that the min_value() method finds the minimal element."""
        # Run 1000 times
        for i in range(1000):
            deque: DequeExtra = DequeExtra()
            sequence: list[int] = random.choices(range(1, 1000), k=1000)
            for j in range(1000):
                deque.add_front(sequence[j])
            tail_cut: int = random.randint(0, 999)
            for j in range(tail_cut):
                deque.remove_front()
            sequence = sequence[0:1000 - tail_cut]
            minimum: int = min(sequence)

            self.assertEqual(minimum, deque.min_value(),
                "min_value() didn't return the minimal element (front).")
        # Use tail methods for these runs
        for i in range(1000):
            deque = DequeExtra()
            sequence = random.choices(range(1, 1000), k=1000)
            for j in range(1000):
                deque.add_tail(sequence[j])
            tail_cut = random.randint(0, 999)
            for j in range(tail_cut):
                deque.remove_tail()
            sequence = sequence[0:1000 - tail_cut]
            minimum = min(sequence)

            self.assertEqual(minimum, deque.min_value(),
                "min_value() didn't return the minimal element (tail).")

    def test_minimum_null(self) -> None:
        """Tests that the min_value() on an empty deque returns None."""
        deque: DequeExtra = DequeExtra()

        self.assertIsNone(deque.min_value(),
            "min_value() on an empty deque doesn't return None.")

    # Tests for the dynamic deque (ex 7.5.*)
    def test_dyndeque_front_resize(self) -> None:
        """Tests front-triggered resize while having a tail."""
        deque: DequeDynamic = DequeDynamic()
        for i in range(100):
            deque.add_tail(i)
        self.assertEqual(128, deque.capacity,
            "Tail-resize is incorrect.")
        for i in range(100):
            deque.add_front(i)
        self.assertEqual(256, deque.capacity,
            "Front-with-tail resize is incorrect.")

        expected: Deque = Deque()
        for i in range(100):
            expected.addTail(i)
            expected.addFront(i)

        self.assertTrue(dyn_deq_equal(expected, deque),
            "Resize of a dynamic deque is incorrect. (front)")

    def test_dyndeque_tail_resize(self) -> None:
        """Tests tail-triggered resize while having a front."""
        deque: DequeDynamic = DequeDynamic()
        for i in range(100):
            deque.add_front(i)
        self.assertEqual(128, deque.capacity,
            "Front-resize is incorrect.")
        for i in range(100):
            deque.add_tail(i)
        self.assertEqual(256, deque.capacity,
            "Tail-with-front resize is incorrect.")

        expected: Deque = Deque()
        for i in range(100):
            expected.addTail(i)
            expected.addFront(i)

        self.assertTrue(dyn_deq_equal(expected, deque),
            "Resize of a dynamic deque is incorrect. (tail)")

    def test_dyndeque_front_shrink(self) -> None:
        """Tests front-triggered shrink while having a tail."""
        deque: DequeDynamic = DequeDynamic()
        for i in range(100):
            deque.add_tail(i)
        for i in range(100):
            deque.add_front(i)
        for i in range(80):
            deque.remove_front()
        self.assertEqual(170, deque.capacity,
            "Front-with-tail shrink is incorrect.")

        expected: Deque = Deque()
        for i in range(100):
            expected.addTail(i)
            if i < 20:
                expected.addFront(i)

        self.assertTrue(dyn_deq_equal(expected, deque),
            "Shrink of a dynamic deque is incorrect. (front)")

    def test_dyndeque_tail_shrink(self) -> None:
        """Tests tail-triggered shrink while having a front."""
        deque: DequeDynamic = DequeDynamic()
        for i in range(100):
            deque.add_front(i)
        for i in range(100):
            deque.add_tail(i)
        for i in range(80):
            deque.remove_tail()
        self.assertEqual(170, deque.capacity,
            "Tail-with-front shrink is incorrect.")

        expected: Deque = Deque()
        for i in range(100):
            if i < 20:
                expected.addTail(i)
            expected.addFront(i)

        self.assertTrue(dyn_deq_equal(expected, deque),
            "Shrink of a dynamic deque is incorrect. (tail)")

    def test_dyndeque_null(self) -> None:
        """Tests removal methods on an empty deque."""
        deque: DequeDynamic = DequeDynamic()

        self.assertIsNone(deque.remove_front(),
            "remove_front() an an empty dyn deque didn't return None.")
        self.assertIsNone(deque.remove_tail(),
            "remove_tail() on an empty dyn deque didn't return None.")


if __name__ == '__main__':
    unittest.main()



