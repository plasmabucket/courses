"""Tests for task 4."""

import unittest
import random
from task4 import Stack
from task4_2 import StackExtra, bracket_balance, calculator


class Task4MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    def test_push(self) -> None:
        """Tests that push() pushes elements on the stack."""
        stack: Stack = Stack()
        for i in range(10):
            stack.push(i)

        self.assertEqual(10, stack.size(),
            "Push() doesn't push elements on the stack correctly.")

    def test_pop(self) -> None:
        """Tests that pop() retrieves elements from the stack."""
        stack: Stack = Stack()
        for i in range(10):
            stack.push(i)

        for i in range(9, -1, -1):
            self.assertEqual(i, stack.pop(),
                "Push-pop pair retrieved incorrect element.")

    def test_peek(self) -> None:
        """Tests that peek() shows the top of the stack."""
        stack: Stack = Stack()

        for i in range(10):
            stack.push(i)
            self.assertEqual(i, stack.peek(),
                "Push-peek pair is inconsistent.")

        for i in range(9, -1, -1):
            self.assertEqual(i, stack.peek(),
                "Peek-pop pair is inconsistent.")
            stack.pop()

    def test_null(self) -> None:
        """Tests behavior of size(), pop(), and peek() on an empty stack."""
        stack: Stack = Stack()

        self.assertEqual(0, stack.size(),
            "Size() of the empty stack isn't zero.")
        self.assertIsNone(stack.pop(),
            "Pop() on an empty stack doesn't return None.")
        self.assertIsNone(stack.peek(),
            "Peek() on an empty stack doesn't return None.")


class Task4ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Tests for the bracket balance determination (ex 5.*, 6.*)
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
            "([)(])[{][}]",
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
        # No need to test as thoroughly since "{}" and "[]" brackets use
        # the same mechanism as "()" brackets which are tested well.
        brackets: list[str] = [
            "[", "]",
            "[]]", "[[]",
            "{", "}",
            "{{}", "{}}"
        ]
        for case in brackets:
            self.assertFalse(bracket_balance(case),
                f"Imbalanced brackets weren't caught. Case: {case}")

    # Tests for finding the minimal element of the stack (ex 7.*)
    def test_minimum(self) -> None:
        """Tests that the min() method finds the minimal element."""
        # Run 10000 times
        for i in range(10000):
            stack: StackExtra = StackExtra()
            sequence: list[int] = random.choices(range(1, 1000), k=1000)
            for j in range(1000):
                stack.push(sequence[j])
            tail_cut: int = random.randint(0, 999)
            for j in range(tail_cut):
                stack.pop()
            sequence = sequence[0:1000 - tail_cut]
            minimum: int = min(sequence)

            self.assertEqual(minimum, stack.min(),
                "Min() didn't return the minimal element.")

    def test_minimum_null(self) -> None:
        """Tests that the min() on an empty stack returns None."""
        stack: StackExtra = StackExtra()

        self.assertIsNone(stack.min(),
            "Min() on an empty stack doesn't return None.")

    # Tests for finding the average value of elements on the stack (ex 8.*)
    def test_average(self) -> None:
        """Tests that the average() method returns an average of elements."""
        # Run 10000 times
        for i in range(10000):
            stack: StackExtra = StackExtra()
            sequence: list[int] = random.choices(range(1, 1000), k=1000)
            for j in range(1000):
                stack.push(sequence[j])
            tail_cut: int = random.randint(0, 999)
            for j in range(tail_cut):
                stack.pop()
            sequence = sequence[0:1000-tail_cut]
            average: float | int = sum(sequence) / (1000 - tail_cut)

            self.assertEqual(average, stack.average(),
                "Average() didn't return the average of elements.")

    def test_average_null(self) -> None:
        """Tests that average() on an empty stack returns None."""
        stack: StackExtra = StackExtra()

        self.assertIsNone(stack.average(),
            "Average() on an empty stack doesn't return None.")

    # Test for the postfix notation calculator (ex 9.*)
    def test_calculator(self) -> None:
        """Simple test for the calculator function."""
        stack: Stack = Stack()
        sequence: list[int | str] = [8, 2, "+", 5, "*", 9, "+", "="]
        for i in range(len(sequence)):
            stack.push(sequence[-1-i])

        result: int = calculator(stack)
        expected: int = (8 + 2) * 5 + 9

        self.assertEqual(expected, result,
            "Calculator is incorrect.")


if __name__ == '__main__':
    unittest.main()



