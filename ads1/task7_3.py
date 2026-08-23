"""Tests for task 7."""

import unittest
import random
import string
from typing import Any
from task7 import Node, OrderedList, OrderedStringList
from task7_2 import list_merge, OrderedListExtra


def list_valid(linked: OrderedList) -> bool:
    """Function to help determine list validity."""
    # Head and tail nodes
    # Head and tail nodes should have None in one of their fields
    if linked.head is not None and linked.head.prev is not None:
        return False
    if linked.tail is not None and linked.tail.next is not None:
        return False
    # In an empty list both are None, in a non-empty list neither are None
    if (linked.head is None) ^ (linked.tail is None):
        return False
    # Middle nodes
    # Next node's previous node should be the current node
    if linked.head is None:  # Skip this check if the list is empty
        return True
    node: Node = linked.head
    while node.next is not None:
        if node.next.prev is not node:
            return False
        node = node.next
    return node is linked.tail  # We should end at the list tail


def lists_equal(lst: list[Any], ordered: OrderedList) -> bool:
    """Function to help compare a standard list to an ordered one."""
    if len(lst) != ordered.len():
        return False
    node: Node | None = ordered.head
    for element in lst:
        if element != node.value:
            return False
        node = node.next
    return True


class Task7MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Tests for addition of an element to the list (ex 3)
    def test_add_ascend(self) -> None:
        """Tests addition of an element on a common case."""
        ordered: OrderedList = OrderedList(True)
        for i in range(9, -1, -1):
            ordered.add(i)

        expected: list[int] = list(range(10))

        self.assertTrue(list_valid(ordered),
            "add() made list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "add() is incorrect.")

    def test_add_ascend_null(self) -> None:
        """Tests addition of an element to an empty list."""
        ordered: OrderedList = OrderedList(True)
        self.assertEqual(0, ordered.len(),
            "List is initialized as non-empty.")
        ordered.add(0)

        expected: list[int] = [0]

        self.assertTrue(list_valid(ordered),
            "add() made an empty list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "add() on an empty list is incorrect.")

    def test_add_ascend_single(self) -> None:
        """Tests addition of an element to a single-element list."""
        ordered: OrderedList = OrderedList(True)
        ordered.add(1)
        ordered.add(0)

        expected: list[int] = [0, 1]

        self.assertTrue(list_valid(ordered),
            "add() made a single-element list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "add() on a single-element list is incorrect.")

    def test_add_ascend_many(self) -> None:
        """Tests addition of an element to a large list."""
        ordered: OrderedList = OrderedList(True)

        expected: list[int] = []
        for i in range(1000):
            item: int = random.randint(0, 500)
            ordered.add(item)
            expected.append(item)

        expected.sort()

        self.assertTrue(list_valid(ordered),
            "add() made a large list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "add() on a large list is incorrect.")

    def test_add_descend(self) -> None:
        """Tests addition of an element on a common case (descend)."""
        ordered: OrderedList = OrderedList(False)
        for i in range(10):
            ordered.add(i)

        expected: list[int] = list(range(9, -1, -1))

        self.assertTrue(list_valid(ordered),
            "add() made list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "add() is incorrect. (descend)")

    def test_add_descend_null(self) -> None:
        """Tests addition of an element to an empty list. (descend)"""
        ordered: OrderedList = OrderedList(False)
        self.assertEqual(0, ordered.len(),
            "List is initialized as non-empty. (descend)")
        ordered.add(0)

        expected: list[int] = [0]

        self.assertTrue(list_valid(ordered),
            "add() made an empty list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "add() on an empty list is incorrect. (descend)")

    def test_add_descend_single(self) -> None:
        """Tests addition of an element to a single-element list. (descend)"""
        ordered: OrderedList = OrderedList(False)
        ordered.add(0)
        ordered.add(1)

        expected: list[int] = [1, 0]

        self.assertTrue(list_valid(ordered),
            "add() made a single-element list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "add() on a single-element list is incorrect. (descend)")

    def test_add_descend_many(self) -> None:
        """Tests addition of an element to a large list. (descend)"""
        ordered: OrderedList = OrderedList(False)

        expected: list[int] = []
        for i in range(1000):
            item: int = random.randint(0, 500)
            ordered.add(item)
            expected.append(item)

        expected.sort(reverse=True)

        self.assertTrue(list_valid(ordered),
            "add() made a large list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "add() on a large list is incorrect. (descend)")

    # Tests for deletion of an element from the list (ex 4)
    def test_del_ascend(self) -> None:
        """Tests deletion of an element on a common case."""
        ordered: OrderedList = OrderedList(True)
        for i in range(10):
            ordered.add(i)

        expected: list[int] = list(range(10))
        expected.pop(6)

        # Successful deletion
        ordered.delete(6)
        self.assertTrue(list_valid(ordered),
            "delete() made list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "delete() is incorrect.")

        # Unsuccessful deletion
        ordered.delete(11)
        self.assertTrue(list_valid(ordered),
            "Noop delete() made list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "Noop delete() is incorrect.")

    def test_del_ascend_null(self) -> None:
        """Tests deletion of an element from an empty list."""
        ordered: OrderedList = OrderedList(True)
        ordered.delete(6)

        expected: list[int] = []

        self.assertTrue(list_valid(ordered),
            "Noop delete() made an empty list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "Noop delete() on an empty list is incorrect.")

    def test_del_ascend_single(self) -> None:
        """Tests deletion of an element from a single-element list."""
        ordered: OrderedList = OrderedList(True)
        ordered.add(6)

        expected: list[int] = []

        # Unsuccessful deletion
        ordered.delete(11)
        self.assertTrue(list_valid(ordered),
            "Noop delete() made a single-element list invalid.")
        self.assertTrue(lists_equal([6], ordered),
            "Noop delete() onn a single-element list is incorrect.")

        # Successful deletion
        ordered.delete(6)
        self.assertTrue(list_valid(ordered),
            "delete() made a single-element list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "delete() on a single-element list is incorrect.")

    def test_del_ascend_many(self) -> None:
        """Tests deletion of an element from a large list."""
        ordered: OrderedList = OrderedList(True)

        expected: list[int] = []
        for i in range(1000):
            item: int = random.randint(0, 500)
            ordered.add(item)
            expected.append(item)

        expected.sort()
        item = expected.pop(600)

        # Successful deletion
        ordered.delete(item)
        self.assertTrue(list_valid(ordered),
            "delete() made a large list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "delete() on a large list is incorrect.")

        # Unsuccessful deletion
        ordered.delete(1100)
        self.assertTrue(list_valid(ordered),
            "Noop delete() made a large list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "Noop delete() on a large list is incorrect.")

    def test_del_descend(self) -> None:
        """Tests deletion of an element on a common case. (descend)"""
        ordered: OrderedList = OrderedList(False)
        for i in range(9, -1, -1):
            ordered.add(i)

        expected: list[int] = list(range(10))
        expected.pop(6)
        expected.reverse()

        # Successful deletion
        ordered.delete(6)
        self.assertTrue(list_valid(ordered),
            "delete() made list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "delete() is incorrect. (descend)")

        # Unsuccessful deletion
        ordered.delete(11)
        self.assertTrue(list_valid(ordered),
            "Noop delete() made list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "Noop delete() is incorrect. (descend)")

    def test_del_descend_null(self) -> None:
        """Tests deletion of an element from an empty list. (descend)"""
        ordered: OrderedList = OrderedList(False)
        ordered.delete(6)

        expected: list[int] = []

        self.assertTrue(list_valid(ordered),
            "Noop delete() made an empty list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "Noop delete() on an empty list is incorrect. (descend)")

    def test_del_descend_single(self) -> None:
        """Tests deletion of an element from a single-element list. (desc)"""
        ordered: OrderedList = OrderedList(False)
        ordered.add(6)

        expected: list[int] = []

        # Unsuccessful deletion
        ordered.delete(11)
        self.assertTrue(list_valid(ordered),
            "Noop delete() made a single-element list invalid. (descend)")
        self.assertTrue(lists_equal([6], ordered),
            "Noop delete() onn a single-element list is incorrect. (descend)")

        # Successful deletion
        ordered.delete(6)
        self.assertTrue(list_valid(ordered),
            "delete() made a single-element list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "delete() on a single-element list is incorrect. (descend)")

    def test_del_descend_many(self) -> None:
        """Tests deletion of an element from a large list. (descend)"""
        ordered: OrderedList = OrderedList(False)

        expected: list[int] = []
        for i in range(1000):
            item: int = random.randint(0, 500)
            ordered.add(item)
            expected.append(item)

        expected.sort()
        expected.reverse()
        item = expected.pop(600)

        # Successful deletion
        ordered.delete(item)
        self.assertTrue(list_valid(ordered),
            "delete() made a large list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "delete() on a large list is incorrect. (descend)")

        # Unsuccessful deletion
        ordered.delete(1100)
        self.assertTrue(list_valid(ordered),
            "Noop delete() made a large list invalid. (descend)")
        self.assertTrue(lists_equal(expected, ordered),
            "Noop delete() on a large list is incorrect. (descend)")

    # Tests for fining an element int the list (ex 6)
    def test_find_ascend(self) -> None:
        """Tests search on a common case."""
        ordered: OrderedList = OrderedList(True)
        for i in range(10):
            ordered.add(i)

        # Successful search
        found: Node | None = ordered.find(6)
        self.assertIsNotNone(found,
            "No matches found when one expected.")
        self.assertEqual(6, found.value,
            "find() is incorrect.")

        # Unsuccessful search
        found = ordered.find(11)
        self.assertIsNone(found,
            "Match found when none expected.")

    def test_find_ascend_null(self) -> None:
        """Tests search on an empty list."""
        ordered: OrderedList = OrderedList(True)

        found: Node | None = ordered.find(6)

        self.assertIsNone(found,
            "find() on an empty list is incorrect.")

    def test_find_ascend_single(self) -> None:
        """Tests search on a single-element list."""
        ordered: OrderedList = OrderedList(True)
        ordered.add(6)

        # Successful search
        found: Node | None = ordered.find(6)
        self.assertIsNotNone(found,
            "No matches found when one expected.")
        self.assertEqual(6, found.value,
            "find() on a single-element list is incorrect.")

        # Unsuccessful search
        found = ordered.find(11)
        self.assertIsNone(found,
            "find() on a single-element list is incorrect.")

    def test_find_ascend_many(self) -> None:
        """Tests search on a large list."""
        ordered: OrderedList = OrderedList(True)
        for i in range(1000):
            ordered.add(i)

        # Successful search
        found: Node | None = ordered.find(600)
        self.assertIsNotNone(found,
            "No matches found when one expected.")
        self.assertEqual(600, found.value,
            "find() on a large list is incorrect.")

        # Unsuccessful search
        found = ordered.find(1100)
        self.assertIsNone(found,
            "Match found when none expected.")

    def test_find_descend(self) -> None:
        """Tests search on a common case. (descend)"""
        ordered: OrderedList = OrderedList(False)
        for i in range(10):
            ordered.add(i)

        # Successful search
        found: Node | None = ordered.find(6)
        self.assertIsNotNone(found,
            "No matches found when one expected. (descend)")
        self.assertEqual(6, found.value,
            "find() is incorrect. (descend)")

        # Unsuccessful search
        found = ordered.find(11)
        self.assertIsNone(found,
            "Match found when none expected. (descend)")

    def test_find_descend_null(self) -> None:
        """Tests search on an empty list. (descend)"""
        ordered: OrderedList = OrderedList(False)

        found: Node | None = ordered.find(6)

        self.assertIsNone(found,
            "find() on an empty list is incorrect. (descend)")

    def test_find_descend_single(self) -> None:
        """Tests search on a single-element list. (descend)"""
        ordered: OrderedList = OrderedList(False)
        ordered.add(6)

        # Successful search
        found: Node | None = ordered.find(6)
        self.assertIsNotNone(found,
            "No matches found when one expected. (descend)")
        self.assertEqual(6, found.value,
            "find() on a single-element list is incorrect. (descend)")

        # Unsuccessful search
        found = ordered.find(11)
        self.assertIsNone(found,
            "find() on a single-element list is incorrect. (descend)")

    def test_find_descend_many(self) -> None:
        """Tests search on a large list. (descend)"""
        ordered: OrderedList = OrderedList(False)
        for i in range(1000):
            ordered.add(i)

        # Successful search
        found: Node | None = ordered.find(600)
        self.assertIsNotNone(found,
            "No matches found when one expected. (descend)")
        self.assertEqual(600, found.value,
            "find() on a large list is incorrect. (descend)")

        # Unsuccessful search
        found = ordered.find(1100)
        self.assertIsNone(found,
            "Match found when none expected. (descend)")

    # Tests for string comparison (ex 5)
    def test_str_compare(self) -> None:
        """Tests comparison of strings on random data."""
        ordered: OrderedStringList = OrderedStringList(True)
        # Run 1000 times
        for i in range(1000):
            str1: str = "".join(random.choices(string.ascii_letters, k=3))
            str2: str = "".join(random.choices(string.ascii_letters, k=3))

            expected: int = 0
            if str1 < str2:
                expected = -1
            if str1 > str2:
                expected = 1

            str1 = (" " * random.randint(0, 2) + str1
                    + " " * random.randint(0, 2))
            str2 = (" " * random.randint(0, 2) + str2
                    + " " * random.randint(0, 2))

            self.assertEqual(expected, ordered.compare(str1, str2),
                "String comparison is incorrect.")

    def test_str_list(self) -> None:
        """Tests if the OrderedStringList class is generally functional."""
        ordered: OrderedStringList = OrderedStringList(True)

        expected: list[str] = []
        for i in range(100):
            char: str = random.choice(string.ascii_letters)
            ordered.add(char)
            expected.append(char)

        expected.sort()

        self.assertTrue(list_valid(ordered),
            "add() on string list made list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "add() on string list is incorrect.")

        char = expected.pop(60)

        ordered.delete(char)
        self.assertTrue(list_valid(ordered),
            "delete() on string list made list invalid.")
        self.assertTrue(lists_equal(expected, ordered),
            "delete() on string list is incorrect.")


class Task7ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Tests for list merging (ex 9.*)
    def test_merge(self) -> None:
        """Tests merging on two regular lists."""
        linked1: OrderedList = OrderedList(True)
        linked2: OrderedList = OrderedList(True)
        for i in range(10):
            linked1.add(i + 1)
            linked2.add(i + 1)

        expected: list[int] = []
        for i in range(10):
            expected.append(i + 1)
            expected.append(i + 1)

        result: OrderedList = list_merge(linked1, linked2, True)
        self.assertTrue(list_valid(result),
            "Merged list is invalid.")
        self.assertTrue(lists_equal(expected, result),
            "Merged list is incorrect.")

    def test_merge_null(self) -> None:
        """Tests merging with an empty list."""
        empty: OrderedList = OrderedList(True)
        single: OrderedList = OrderedList(True)
        multi: OrderedList = OrderedList(True)
        single.add(1)
        for i in range(10):
            multi.add(i + 1)

        expected2: list[int] = []
        expected1: list[int] = []
        expected3: list[int] = []
        expected2.append(1)
        for i in range(10):
            expected3.append(i + 1)

        # Empty + empty
        result: OrderedList = list_merge(empty, empty, True)
        self.assertTrue(list_valid(result),
            "Empty + empty merged list is invalid.")
        self.assertTrue(lists_equal(expected1, result),
            "Empty + empty merged list is incorrect.")

        # Empty + single
        result = list_merge(empty, single, True)
        self.assertTrue(list_valid(result),
            "Empty + single merged list is invalid.")
        self.assertTrue(lists_equal(expected2, result),
            "Empty + single merged list is incorrect.")

        # Empty + multi
        result = list_merge(empty, multi, True)
        self.assertTrue(list_valid(result),
            "Empty + multi merged list is invalid.")
        self.assertTrue(lists_equal(expected3, result),
            "Empty + multi merged list is incorrect.")

    def test_merge_single(self) -> None:
        """Tests merging with a single-element list."""
        empty: OrderedList = OrderedList(True)
        single: OrderedList = OrderedList(True)
        multi: OrderedList = OrderedList(True)
        single.add(1)
        for i in range(10):
            multi.add(i + 1)

        expected1: list[int] = []
        expected2: list[int] = []
        expected3: list[int] = []
        expected1.append(1)
        expected2.append(1)
        expected2.append(1)
        expected3.append(1)
        for i in range(10):
            expected3.append(i + 1)

        # Single + empty
        result: OrderedList = list_merge(single, empty, True)
        self.assertTrue(list_valid(result),
            "Single + empty merged list is invalid.")
        self.assertTrue(lists_equal(expected1, result),
            "Single + empty merged list is incorrect.")

        # Single + single
        result = list_merge(single, single, True)
        self.assertTrue(list_valid(result),
            "Single + single merged list is invalid.")
        self.assertTrue(lists_equal(expected2, result),
            "Single + single merged list is incorrect.")

        # Single + multi
        result = list_merge(single, multi, True)
        self.assertTrue(list_valid(result),
            "Single + multi merged list is invalid.")
        self.assertTrue(lists_equal(expected3, result),
            "Single + multi merged list is incorrect.")

    def test_merge_multi(self) -> None:
        """Tests merging with a multi-element list."""
        empty: OrderedList = OrderedList(True)
        single: OrderedList = OrderedList(True)
        multi: OrderedList = OrderedList(True)
        single.add(1)
        for i in range(10):
            multi.add(i + 1)

        expected1: list[int] = []
        expected2: list[int] = []
        expected3: list[int] = []
        for i in range(10):
            expected1.append(i + 1)
        expected2.append(1)
        for i in range(10):
            expected2.append(i + 1)
        for i in range(10):
            expected3.append(i + 1)
            expected3.append(i + 1)

        # Multi + empty
        result: OrderedList = list_merge(multi, empty, True)
        self.assertTrue(list_valid(result),
            "Multi + empty merged list is invalid.")
        self.assertTrue(lists_equal(expected1, result),
            "Multi + empty merged list is incorrect.")

        # Multi + single
        result = list_merge(multi, single, True)
        self.assertTrue(list_valid(result),
            "Multi + single merged list is invalid.")
        self.assertTrue(lists_equal(expected2, result),
            "Multi + single merged list is incorrect.")

        # Multi + multi
        result = list_merge(multi, multi, True)
        self.assertTrue(list_valid(result),
            "Multi + multi merged list is invalid.")
        self.assertTrue(lists_equal(expected3, result),
            "Multi + multi merged list is incorrect.")

    def test_merge_many_descend(self) -> None:
        """Tests merging on two large lists. (descend)"""
        linked1: OrderedList = OrderedList(False)
        linked2: OrderedList = OrderedList(False)
        for i in range(1000):
            linked1.add(i + 1)
            linked2.add(i + 1)

        expected: list[int] = []
        for i in range(999, -1, -1):
            expected.append(i + 1)
            expected.append(i + 1)

        result: OrderedList = list_merge(linked1, linked2, False)
        self.assertTrue(list_valid(result),
            "Merged large list is invalid. (descend)")
        self.assertTrue(lists_equal(expected, result),
            "Merged large list is incorrect. (descend)")

    # Tests for removal of duplicates (ex 8.*)
    def test_dedup(self) -> None:
        """Tests removal of duplicates from a list on random data."""
        # Run 1000 times
        for i in range(1000):
            ordered: OrderedListExtra = OrderedListExtra(True)
            expected: list[int] = random.choices(range(0, 100), k=150)
            for item in expected:
                ordered.add(item)
            expected = list(set(expected))
            expected.sort()

            ordered.rm_duplicates()
            self.assertTrue(list_valid(ordered),
                "rm_duplicates() made list invalid.")
            self.assertTrue(lists_equal(expected, ordered),
                "rm_duplicates() is incorrect.")

    def test_dedup_descend(self) -> None:
        """Tests removal of duplicates from a list on random data. (descend)"""
        # Run 1000 times
        for i in range(1000):
            ordered = OrderedListExtra(False)
            expected: list[int] = random.choices(range(0, 100), k=150)
            for item in expected:
                ordered.add(item)
            expected = list(set(expected))
            expected.sort(reverse=True)

            ordered.rm_duplicates()
            self.assertTrue(list_valid(ordered),
                "rm_duplicates() made list invalid. (descend)")
            self.assertTrue(lists_equal(expected, ordered),
                "rm_duplicates() is incorrect. (descend)")

    # Tests for sub-list search (ex 10.*)
    def test_sublist(self) -> None:
        """Tests sub-list search on random data."""
        # Run 1000 times
        for i in range(1000):
            ordered: OrderedListExtra = OrderedListExtra(True)
            sequence: list[int] = random.choices(range(0, 100), k=150)
            for item in sequence:
                ordered.add(item)

            sub_list: OrderedListExtra = OrderedListExtra(True)
            start: int = random.randint(0, 150 - 15 - 1)
            sub_len: int = random.randint(0, 15)
            sequence.sort()
            subseq: list[int] = sequence[start: start + sub_len]
            for item in subseq:
                sub_list.add(item)

            self.assertTrue(ordered.find_sublist(sub_list),
                "Sub-list not found when its present.")

            if random.randint(0, 1) == 0 and len(subseq) != 0:
                element: int = random.choice(subseq)
                sub_list.delete(element)
            if random.randint(0, 1) == 0:
                sub_list.add(-1)
            sub_list.add(1000)

            self.assertFalse(ordered.find_sublist(sub_list),
                "Sub-list found when it's not present.")

    def test_sublist_descend(self) -> None:
        """Tests sub-list search on random data. (descend)"""
        # Run 1000 times
        for i in range(1000):
            ordered: OrderedListExtra = OrderedListExtra(False)
            sequence: list[int] = random.choices(range(0, 100), k=150)
            for item in sequence:
                ordered.add(item)

            sub_list: OrderedListExtra = OrderedListExtra(False)
            start: int = random.randint(0, 150 - 15 - 1)
            sub_len: int = random.randint(0, 15)
            sequence.sort()
            subseq: list[int] = sequence[start: start + sub_len]
            for item in subseq:
                sub_list.add(item)

            self.assertTrue(ordered.find_sublist(sub_list),
                "Sub-list not found when its present. (descend)")

            if random.randint(0, 1) == 0 and len(subseq) != 0:
                element: int = random.choice(subseq)
                sub_list.delete(element)
            if random.randint(0, 1) == 0:
                sub_list.add(-1)
            sub_list.add(1000)

            self.assertFalse(ordered.find_sublist(sub_list),
                "Sub-list found when it's not present. (descend)")

    # Test for search of the most common value (ex 11.*)
    def test_common(self) -> None:
        """Tests search for the most common value on random data."""
        # Run 1000 times
        for i in range(1000):
            ordered: OrderedListExtra = OrderedListExtra(True)
            sequence: list[int] = random.choices(range(0, 100), k=150)
            for item in sequence:
                ordered.add(item)

            sequence.sort()
            highest_count: int = 0
            current_count: int = 0
            most_common_val: int = 0
            current_val: int = 0
            for val in sequence:
                if current_val != val:
                    current_val = val
                    current_count = 0
                current_count += 1
                if current_count > highest_count:
                    highest_count = current_count
                    most_common_val = current_val

            self.assertEqual(most_common_val, ordered.most_common(),
                "most_common() is incorrect.")

    def test_common_descend(self) -> None:
        """Tests search for the most common value on random data. (descend)"""
        # Run 1000 times
        for i in range(1000):
            ordered: OrderedListExtra = OrderedListExtra(False)
            sequence: list[int] = random.choices(range(0, 100), k=150)
            for item in sequence:
                ordered.add(item)

            sequence.sort(reverse=True)
            highest_count: int = 0
            current_count: int = 0
            most_common_val: int = 0
            current_val: int = 0
            for val in sequence:
                if current_val != val:
                    current_val = val
                    current_count = 0
                current_count += 1
                if current_count > highest_count:
                    highest_count = current_count
                    most_common_val = current_val

            self.assertEqual(most_common_val, ordered.most_common(),
                "most_common() is incorrect. (descend)")

    # Tests for index search (ex 12.*)
    def test_index(self) -> None:
        """Tests element's index search on random data."""
        # Run 1000 times
        for i in range(1000):
            ordered: OrderedListExtra = OrderedListExtra(True)
            sequence: list[int] = random.choices(range(0, 100), k=90)
            for item in sequence:
                ordered.add(item)
            sequence.sort()

            target: int = random.randint(-5, 105)
            expected: list[int] = []
            for i in range(len(sequence)):
                if target == sequence[i]:
                    expected.append(i)
            if len(expected) == 0:
                expected.append(-1)

            self.assertTrue(ordered.find_index(target) in expected,
                "find_index() is incorrect.")

    def test_index_descend(self) -> None:
        """Tests element's index search on random data. (descend)"""
        # Run 1000 times
        for i in range(1000):
            ordered: OrderedListExtra = OrderedListExtra(False)
            sequence: list[int] = random.choices(range(0, 100), k=90)
            for item in sequence:
                ordered.add(item)
            sequence.sort(reverse=True)

            target: int = random.randint(-5, 105)
            expected: list[int] = []
            for i in range(len(sequence)):
                if target == sequence[i]:
                    expected.append(i)
            if len(expected) == 0:
                expected.append(-1)

            self.assertTrue(ordered.find_index(target) in expected,
                f"find_index() is incorrect. (descent)"
                f"{ordered.find_index(target)}, exp: {expected}")


if __name__ == '__main__':
    unittest.main()



