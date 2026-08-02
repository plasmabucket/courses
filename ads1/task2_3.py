"""Tests for task 2."""

import unittest
import random
from task2 import Node, LinkedList2
from task2_2 import LinkedList2Ext, LinkedListDummy


def list_valid(linked: LinkedList2) -> bool:
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


def lists_equal(ll_1: LinkedList2, ll_2: LinkedList2) -> bool:
    """Function to help compare list equality."""
    length: int = ll_1.len()
    if length != ll_2.len():
        return False
    node1: Node | None = ll_1.head
    node2: Node | None = ll_2.head
    for i in range(length):
        if node1.value != node2.value:
            return False
        node1 = node1.next
        node2 = node2.next
    return True


class Task2Tests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Tests for single-match search (ex 2.1)
    def test_find_regression(self) -> None:
        """Tests correctness of a search on a known and common case."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))

        # Successful search
        found: Node | None = linked.find(6)
        self.assertIsNotNone(found,
            "No matches found when one expected.")
        self.assertEqual(6, found.value,
            "Wrong match found.")

        # Unsuccessful search
        found = linked.find(11)
        self.assertIsNone(found,
            "Match found when none expected.")

    def test_find_null(self) -> None:
        """Tests single-element search on an empty list."""
        linked: LinkedList2 = LinkedList2()

        found: Node | None = linked.find(6)
        self.assertIsNone(found,
            "A match found when searching an empty list.")

    def test_find_single(self) -> None:
        """Tests single-element search on a single-element list."""
        linked: LinkedList2 = LinkedList2()
        linked.add_in_tail(Node(6))

        # Successful search
        found: Node | None = linked.find(6)
        self.assertIsNotNone(found,
            "No matches found when one expected.")
        self.assertEqual(6, found.value,
            "Wrong match found.")

        # Unsuccessful search
        found = linked.find(11)
        self.assertIsNone(found,
            "Match found when none expected.")

    def test_find_many(self) -> None:
        """Tests single-element search on a large list."""
        linked: LinkedList2 = LinkedList2()
        for i in range(1000):
            linked.add_in_tail(Node(i + 1))

        # Successful search
        found: Node | None = linked.find(600)
        self.assertIsNotNone(found,
            "No matches found when one expected.")
        self.assertEqual(600, found.value,
            "Wrong match found.")

        # Unsuccessful search
        found = linked.find(1001)
        self.assertIsNone(found,
            "Match found when none expected.")

    # Tests for full node search (ex 2.2)
    def test_find_all_regression(self) -> None:
        """Tests correctness of a search on a known and common case."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))
            linked.add_in_tail(Node(i + 1))

        # Successful search
        found: list[Node] = linked.find_all(6)
        self.assertEqual(2, len(found),
            "Found more or less elements than expected.")
        self.assertEqual(6, found[0].value,
            "Wrong element got found.")
        self.assertEqual(6, found[1].value,
            "Wrong element got found.")

        # Unsuccessful search
        found = linked.find_all(11)
        self.assertEqual(0, len(found),
            "Element found when none expected.")

    def test_find_all_null(self) -> None:
        """Tests search on an empty list."""
        linked: LinkedList2 = LinkedList2()

        found: list[Node] = linked.find_all(6)
        self.assertEqual([], found,
            "Element found when none expected.")

    def test_find_all_single(self) -> None:
        """Tests search on a list with a single element."""
        linked: LinkedList2 = LinkedList2()
        linked.add_in_tail(Node(6))

        # Successful search
        found: list[Node] = linked.find_all(6)
        self.assertEqual(1, len(found),
            "Only a single match was expected.")
        self.assertEqual(6, found[0].value,
            "Incorrect element got found.")

        # Unsuccessful search
        found = linked.find_all(11)
        self.assertEqual([], found,
            "Element found when none expected.")

    def test_find_all_many(self) -> None:
        """Tests search on a list with many elements."""
        linked: LinkedList2 = LinkedList2()
        for i in range(1000):
            linked.add_in_tail(Node(6))

        # Successful search
        found: list[Node] = linked.find_all(6)
        self.assertEqual(1000, len(found),
            "1000 matches were expected.")
        for i in range(1000):
            self.assertEqual(6, found[i].value,
                "Incorrect element got found.")

        # Unsuccessful search
        found = linked.find_all(11)
        self.assertEqual([], found,
            "Element found when none expected.")

    # Tests for deletion (ex 2.3, 2.4)
    def test_delete_regression(self) -> None:
        """Tests correctness of deletion on a known and common case."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))

        expected: LinkedList2 = LinkedList2()
        for i in range(10):
            if i + 1 == 6:
                continue
            expected.add_in_tail(Node(i + 1))

        # Successful deletion
        linked.delete(6, False)
        self.assertTrue(list_valid(linked),
            "Deletion made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Wrong element got deleted.")

        # Unsuccessful deletion
        linked.delete(11, False)
        self.assertTrue(list_valid(linked),
            "Noop deletion made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Noop deletion changed list.")

    def test_delete_tail(self) -> None:
        """Tests deletion on the last element."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))
        linked.delete(10, False)

        expected: LinkedList2 = LinkedList2()
        for i in range(9):
            expected.add_in_tail(Node(i + 1))

        self.assertTrue(list_valid(linked),
            "Deletion of the tail made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Deletion of the tail deleted something else.")

    def test_delete_head(self) -> None:
        """Tests deletion on the first element."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))
        linked.delete(1, False)

        expected: LinkedList2 = LinkedList2()
        for i in range(1, 10):
            expected.add_in_tail(Node(i + 1))

        self.assertTrue(list_valid(linked),
            "Deletion of the head made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Deletion of the head deleted something else.")

    def test_delete_null(self) -> None:
        """Tests deletion on an empty list."""
        linked: LinkedList2 = LinkedList2()
        linked.delete(6, True)

        expected: LinkedList2 = LinkedList2()

        self.assertTrue(list_valid(linked),
            "Noop deletion left empty list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Noop deletion changed empty list.")

    def test_delete_single(self) -> None:
        """Tests deletion of the only element in the list."""
        linked: LinkedList2 = LinkedList2()
        linked.add_in_tail(Node(1))
        linked.delete(1, True)

        expected: LinkedList2 = LinkedList2()

        self.assertTrue(list_valid(linked),
            "Deletion of the only element made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Deletion of the only element didn't leave an empty list.")

    def test_delete_multiple(self) -> None:
        """Tests deletion of multiple elements."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))
        for i in range(9, 0, -1):
            linked.add_in_tail(Node(i + 1))
        linked.delete(6, True)

        expected: LinkedList2 = LinkedList2()
        for i in range(10):
            if i + 1 == 6:
                continue
            expected.add_in_tail(Node(i + 1))
        for i in range(9, 0, -1):
            if i + 1 == 6:
                continue
            expected.add_in_tail(Node(i + 1))

        self.assertTrue(list_valid(linked),
            "Deletion of multiple elements made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Deletion of multiple elements deleted wrong elements.")

    def test_delete_many(self) -> None:
        """Tests deletion of many elements in a huge list."""
        linked: LinkedList2 = LinkedList2()
        for i in range(1000):
            linked.add_in_tail(Node(6))
        linked.delete(6, True)

        expected: LinkedList2 = LinkedList2()

        self.assertTrue(list_valid(linked),
            "Deletion of all elements made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Deletion of all elements didn't leave an empty list.")

    # Tests for element insertion (ex 2.5)
    def test_insert_regression(self) -> None:
        """Tests correctness of insertion on a known and common case."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))
        node: Node | None = linked.find(6)
        insertion: Node = Node(-1)
        linked.insert(node, insertion)

        expected: LinkedList2 = LinkedList2()
        for i in range(10):
            if i + 1 == 7:
                expected.add_in_tail(Node(-1))
            expected.add_in_tail(Node(i + 1))

        self.assertTrue(list_valid(linked),
            "Insertion made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Insertion is incorrect.")

    def test_insert_null(self) -> None:
        """Tests insertion on an empty list."""
        linked: LinkedList2 = LinkedList2()
        insertion: Node = Node(-1)
        linked.insert(None, insertion)

        expected: LinkedList2 = LinkedList2()
        expected.add_in_tail(Node(-1))

        self.assertTrue(list_valid(linked),
            "Insertion in the empty list made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Insertion in the empty list is incorrect.")

    def test_insert_single_none(self) -> None:
        """Tests insertion on a single element list using None."""
        linked: LinkedList2 = LinkedList2()
        linked.add_in_tail(Node(1))
        insertion: Node = Node(-1)
        linked.insert(None, insertion)

        expected: LinkedList2 = LinkedList2()
        expected.add_in_tail(Node(1))
        expected.add_in_tail(Node(-1))

        self.assertTrue(list_valid(linked),
            "Insertion using None made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Insertion using None is incorrect.")

    def test_insert_single(self) -> None:
        """Tests insertion on a single element list."""
        linked: LinkedList2 = LinkedList2()
        linked.add_in_tail(Node(1))
        insertion: Node = Node(-1)
        linked.insert(linked.head, insertion)

        expected: LinkedList2 = LinkedList2()
        expected.add_in_tail(Node(1))
        expected.add_in_tail(Node(-1))

        self.assertTrue(list_valid(linked),
            "Insertion in a single element list made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Insertion in a single element list is incorrect.")

    def test_insert_many(self) -> None:
        """Tests insertion on a large list."""
        linked: LinkedList2 = LinkedList2()
        node: Node | None = None
        for i in range(1000):
            linked.add_in_tail(Node(i + 1))
            if i + 1 == 600:
                node = linked.tail
        insertion: Node = Node(-1)
        linked.insert(node, insertion)

        expected: LinkedList2 = LinkedList2()
        for i in range(1000):
            expected.add_in_tail(Node(i + 1))
            if i + 1 == 600:
                expected.add_in_tail(Node(-1))

        self.assertTrue(list_valid(linked),
            "Insertion in a large list made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Insertion in a large list is incorrect.")

    # Tests for head insertion (ex. 2.6)
    def test_add_head_regression(self) -> None:
        """Tests head insertion on a known and common case."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_head(Node(i + 1))

        expected: LinkedList2 = LinkedList2()
        for i in range(10, 0, -1):
            expected.add_in_tail(Node(i))

        self.assertTrue(list_valid(linked),
            "Head insertion made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Head insertion is incorrect.")

    def test_add_head_null(self) -> None:
        """Tests head insertion on an empty list."""
        linked: LinkedList2 = LinkedList2()
        linked.add_in_head(Node(1))

        expected: LinkedList2 = LinkedList2()
        expected.add_in_tail(Node(1))

        self.assertTrue(list_valid(linked),
            "Head insertion in the empty list made list invalid.")

    def test_add_head_not_null(self) -> None:
        """Tests head insertion on a non-empty list."""
        linked: LinkedList2 = LinkedList2()
        linked.add_in_tail(Node(2))
        linked.add_in_head(Node(1))

        expected: LinkedList2 = LinkedList2()
        expected.add_in_tail(Node(1))
        expected.add_in_tail(Node(2))

        self.assertTrue(list_valid(linked),
            "Head insertion in a non-empty list made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Head insertion in a non-empty list is incorrect.")

    # Tests for cleaning (ex 2.7)
    def test_clean_regression(self) -> None:
        """Tests if clean() clears non-empty list."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))
        linked.clean()

        expected: LinkedList2 = LinkedList2()

        self.assertTrue(list_valid(linked),
            "Clean operation on a non-empty list made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Clean operation didn't clean the list.")

    def test_clean_null(self) -> None:
        """Tests if clean() works on an empty list."""
        linked: LinkedList2 = LinkedList2()
        linked.clean()

        expected: LinkedList2 = LinkedList2()

        self.assertTrue(list_valid(linked),
            "Clean operation on an empty list made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Clean operation on an empty list made list non-empty.")

    # Tests for list length counting (ex 2.8)
    def test_len_regression(self) -> None:
        """Tests correctness of length counting on a known and common case."""
        linked: LinkedList2 = LinkedList2()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))

        self.assertEqual(10, linked.len(),
            "List length was determined incorrectly.")

    def test_len_sizes(self) -> None:
        """Tests length counting on lists of different sizes."""
        # Empty list
        linked: LinkedList2 = LinkedList2()
        self.assertEqual(0, linked.len(),
            "Empty list length was determined incorrectly.")

        # Single-element list
        linked.clean()
        linked.add_in_tail(Node(6))
        self.assertEqual(1, linked.len(),
            "Single element list length was determined incorrectly.")

        # Large list
        linked.clean()
        for i in range(1000):
            linked.add_in_tail(Node(i + 1))
        self.assertEqual(1000, linked.len(),
            "Large list length was determined incorrectly.")


class Task2ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Tests for list reversal (ex 2.10.*)
    def test_reverse_regression(self) -> None:
        """Tests reversal on a known and common case."""
        linked: LinkedList2Ext = LinkedList2Ext()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))
        linked.list_reverse()

        expected: LinkedList2 = LinkedList2()
        for i in range(10, 0, -1):
            expected.add_in_tail(Node(i))

        self.assertTrue(list_valid(linked),
            "Reversal made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Reversal is incorrect.")

    def test_reverse_null(self) -> None:
        """Tests reversal on an empty list."""
        linked: LinkedList2Ext = LinkedList2Ext()
        linked.list_reverse()

        expected: LinkedList2 = LinkedList2()

        self.assertTrue(list_valid(linked),
            "Reversal of an empty list made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Reversal of an empty list is incorrect.")

    def test_reverse_single(self) -> None:
        """Tests reversal on a single-element list."""
        linked: LinkedList2Ext = LinkedList2Ext()
        linked.add_in_tail(Node(1))
        linked.list_reverse()

        expected: LinkedList2 = LinkedList2()
        expected.add_in_tail(Node(1))

        self.assertTrue(list_valid(linked),
            "Reversal of a single-element list made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Reversal of a single-element list is incorrect.")

    def test_reverse_many(self) -> None:
        """Tests reversal on a large list."""
        linked: LinkedList2Ext = LinkedList2Ext()
        for i in range(1000):
            linked.add_in_tail(Node(i + 1))
        linked.list_reverse()

        expected: LinkedList2 = LinkedList2()
        for i in range(1000, 0, -1):
            expected.add_in_tail(Node(i))

        self.assertTrue(list_valid(linked),
            "Reversal of a large list made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "Reversal of a large list is incorrect.")

    # Tests for cycle determination (ex 2.11.*)
    def test_cycles_regression(self) -> None:
        """Tests cycle determination on a known and common case."""
        linked: LinkedList2Ext = LinkedList2Ext()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))

        # No cycles
        self.assertFalse(linked.has_cycles(),
            "Cycle found when none expected.")

        # One next-based cycle
        node1: Node | None = linked.find(3)
        node2: Node | None = linked.find(7)
        node2.next = node1
        self.assertTrue(linked.has_cycles(),
            "No cycle found when one expected.")

    def test_cycles_null(self) -> None:
        """Tests cycle determination on an empty list."""
        linked: LinkedList2Ext = LinkedList2Ext()

        self.assertFalse(linked.has_cycles(),
            "Cycle found in an empty list.")

    def test_cycles_single(self) -> None:
        """Tests cycle determination on a single-element list."""
        linked: LinkedList2Ext = LinkedList2Ext()
        linked.add_in_tail(Node(1))

        # No cycles
        self.assertFalse(linked.has_cycles(),
            "Cycle found in a single-element list when none expected.")

        # Self-cycle through prev
        linked.head.prev = linked.head
        self.assertTrue(linked.has_cycles(),
            "Prev- based cycle wasn't found in a single-element list.")

        # Self-cycle through next
        linked.head.prev = None  # Restore 'prev' field
        linked.head.next = linked.head
        self.assertTrue(linked.has_cycles(),
            "Next- based cycle wasn't found in a single-element list.")

        # Full self-cycle
        linked.head.prev = linked.head
        self.assertTrue(linked.has_cycles(),
            "Full cycle wasn't found in a single-element list.")

    def test_cycles_many(self) -> None:
        """Tests cycle determination on a large list."""
        linked: LinkedList2Ext = LinkedList2Ext()
        for i in range(1000):
            linked.add_in_tail(Node(i + 1))

        # No cycles
        self.assertFalse(linked.has_cycles(),
            "Cycle found in a large list when none expected.")

        # Cycle through next
        node1: Node | None = linked.find(250)
        node2: Node | None = linked.find(750)
        node3: Node | None = linked.find(751)
        node2.next = node1
        self.assertTrue(linked.has_cycles(),
            "Next- based cycle wasn't found in a large list.")

        # Cycle through prev
        node2.next = node3  # Restore 'next' field
        node1.prev = node2
        self.assertTrue(linked.has_cycles(),
            "Prev- based cycle wasn't found in a large list.")

        # Cycle through prev and next
        node2.next = node1
        self.assertTrue(linked.has_cycles(),
            "Next- and prev- based cycle wasn't found in a large list.")

    def test_cycle_full(self) -> None:
        """Tests cycle determination on a full-list cycle."""
        linked: LinkedList2Ext = LinkedList2Ext()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))

        linked.head.prev = linked.tail
        linked.tail.next = linked.head

        self.assertTrue(linked.has_cycles(),
            "Full-list cycle wasn't found.")

    # Tests for list sorting (ex 2.12.*)
    def test_sort_regression(self) -> None:
        """Tests list sort on a known and common case."""
        linked: LinkedList2Ext = LinkedList2Ext()
        for i in range(10):
            linked.add_in_head(Node(i + 1))
        linked.list_sort()

        expected: LinkedList2 = LinkedList2Ext()
        for i in range(10):
            expected.add_in_tail(Node(i + 1))

        self.assertTrue(list_valid(linked),
            "List sort made list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "List sort is incorrect.")

    def test_sort_sorted(self) -> None:
        """Tests list sort on an already sorted list."""
        linked: LinkedList2Ext = LinkedList2Ext()
        for i in range(10):
            linked.add_in_tail(Node(i + 1))
        linked.list_sort()

        expected: LinkedList2 = LinkedList2Ext()
        for i in range(10):
            expected.add_in_tail(Node(i + 1))

        self.assertTrue(list_valid(linked),
            "List sort made sorted list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "List sort on a sorted list is incorrect.")

    def test_sort_null(self) -> None:
        """Tests list sort on an empty list."""
        linked: LinkedList2Ext = LinkedList2Ext()
        linked.list_sort()

        expected: LinkedList2 = LinkedList2()

        self.assertTrue(list_valid(linked),
            "List sort made empty list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "List sort on an empty list is incorrect.")

    def test_sort_single(self) -> None:
        """Tests list sort on a single-element list."""
        linked: LinkedList2Ext = LinkedList2Ext()
        linked.add_in_tail(Node(1))
        linked.list_sort()

        expected: LinkedList2 = LinkedList2()
        expected.add_in_tail(Node(1))

        self.assertTrue(list_valid(linked),
            "List sort made single-element list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "list sort on a single-element list is incorrect.")

    def test_sort_many(self) -> None:
        """Tests list sort on a large list."""
        values: list[int] = random.choices(range(1, 1000), k=1000)
        linked: LinkedList2Ext = LinkedList2Ext()
        for i in range(1000):
            linked.add_in_tail(Node(values[i]))
        linked.list_sort()

        values.sort()
        expected: LinkedList2 = LinkedList2()
        for i in range(1000):
            expected.add_in_tail(Node(values[i]))

        self.assertTrue(list_valid(linked),
            "List sort made large list invalid.")
        self.assertTrue(lists_equal(expected, linked),
            "list sort on a large list is incorrect.")

    # Tests for list merging (ex 2.13.*)
    def test_merge_regression(self) -> None:
        """Tests merging on two regular lists."""
        linked1: LinkedList2 = LinkedList2()
        linked2: LinkedList2 = LinkedList2()
        for i in range(10):
            linked1.add_in_tail(Node(i + 1))
            linked2.add_in_tail(Node(i + 1))

        expected: LinkedList2 = LinkedList2()
        for i in range(10):
            expected.add_in_tail(Node(i + 1))
            expected.add_in_tail(Node(i + 1))

        result: LinkedList2 = LinkedList2Ext.list_merge(linked1, linked2)
        self.assertTrue(list_valid(result),
            "Merged list is invalid.")
        self.assertTrue(lists_equal(expected, result),
            "Merged list is incorrect.")

    def test_merge_null(self) -> None:
        """Tests merging with an empty list."""
        empty: LinkedList2 = LinkedList2()
        single: LinkedList2 = LinkedList2()
        multi: LinkedList2 = LinkedList2()
        single.add_in_tail(Node(1))
        for i in range(10):
            multi.add_in_tail(Node(i + 1))

        expected1: LinkedList2 = LinkedList2()
        expected2: LinkedList2 = LinkedList2()
        expected3: LinkedList2 = LinkedList2()
        expected2.add_in_tail(Node(1))
        for i in range(10):
            expected3.add_in_tail(Node(i + 1))

        # Empty + empty
        result: LinkedList2 = LinkedList2Ext.list_merge(empty, empty)
        self.assertTrue(list_valid(result),
            "Empty + empty merged list is invalid.")
        self.assertTrue(lists_equal(expected1, result),
            "Empty + empty merged list is incorrect.")

        # Empty + single
        result = LinkedList2Ext.list_merge(empty, single)
        self.assertTrue(list_valid(result),
            "Empty + single merged list is invalid.")
        self.assertTrue(lists_equal(expected2, result),
            "Empty + single merged list is incorrect.")

        # Empty + multi
        result = LinkedList2Ext.list_merge(empty, multi)
        self.assertTrue(list_valid(result),
            "Empty + multi merged list is invalid.")
        self.assertTrue(lists_equal(expected3, result),
            "Empty + multi merged list is incorrect.")

    def test_merge_single(self) -> None:
        """Tests merging with a single-element list."""
        empty: LinkedList2 = LinkedList2()
        single: LinkedList2 = LinkedList2()
        multi: LinkedList2 = LinkedList2()
        single.add_in_tail(Node(1))
        for i in range(10):
            multi.add_in_tail(Node(i + 1))

        expected1: LinkedList2 = LinkedList2()
        expected2: LinkedList2 = LinkedList2()
        expected3: LinkedList2 = LinkedList2()
        expected1.add_in_tail(Node(1))
        expected2.add_in_tail(Node(1))
        expected2.add_in_tail(Node(1))
        expected3.add_in_tail(Node(1))
        for i in range(10):
            expected3.add_in_tail(Node(i + 1))

        # Single + empty
        result: LinkedList2 = LinkedList2Ext.list_merge(single, empty)
        self.assertTrue(list_valid(result),
            "Single + empty merged list is invalid.")
        self.assertTrue(lists_equal(expected1, result),
            "Single + empty merged list is incorrect.")

        # Single + single
        result = LinkedList2Ext.list_merge(single, single)
        self.assertTrue(list_valid(result),
            "Single + single merged list is invalid.")
        self.assertTrue(lists_equal(expected2, result),
            "Single + single merged list is incorrect.")

        # Single + multi
        result = LinkedList2Ext.list_merge(single, multi)
        self.assertTrue(list_valid(result),
            "Single + multi merged list is invalid.")
        self.assertTrue(lists_equal(expected3, result),
            "Single + multi merged list is incorrect.")

    def test_merge_multi(self) -> None:
        """Tests merging with a multi-element list."""
        empty: LinkedList2 = LinkedList2()
        single: LinkedList2 = LinkedList2()
        multi: LinkedList2 = LinkedList2()
        single.add_in_tail(Node(1))
        for i in range(10):
            multi.add_in_tail(Node(i + 1))

        expected1: LinkedList2 = LinkedList2()
        expected2: LinkedList2 = LinkedList2()
        expected3: LinkedList2 = LinkedList2()
        for i in range(10):
            expected1.add_in_tail(Node(i + 1))
        expected2.add_in_tail(Node(1))
        for i in range(10):
            expected2.add_in_tail(Node(i + 1))
        for i in range(10):
            expected3.add_in_tail(Node(i + 1))
            expected3.add_in_tail(Node(i + 1))

        # Multi + empty
        result: LinkedList2 = LinkedList2Ext.list_merge(multi, empty)
        self.assertTrue(list_valid(result),
            "Multi + empty merged list is invalid.")
        self.assertTrue(lists_equal(expected1, result),
            "Multi + empty merged list is incorrect.")

        # Multi + single
        result = LinkedList2Ext.list_merge(multi, single)
        self.assertTrue(list_valid(result),
            "Multi + single merged list is invalid.")
        self.assertTrue(lists_equal(expected2, result),
            "Multi + single merged list is incorrect.")

        # Multi + multi
        result = LinkedList2Ext.list_merge(multi, multi)
        self.assertTrue(list_valid(result),
            "Multi + multi merged list is invalid.")
        self.assertTrue(lists_equal(expected3, result),
            "Multi + multi merged list is incorrect.")

    def test_merge_many(self) -> None:
        """Tests merging on two large lists."""
        linked1: LinkedList2 = LinkedList2()
        linked2: LinkedList2 = LinkedList2()
        for i in range(1000):
            linked1.add_in_tail(Node(i + 1))
            linked2.add_in_tail(Node(i + 1))

        expected: LinkedList2 = LinkedList2()
        for i in range(1000):
            expected.add_in_tail(Node(i + 1))
            expected.add_in_tail(Node(i + 1))

        result: LinkedList2 = LinkedList2Ext.list_merge(linked1, linked2)
        self.assertTrue(list_valid(result),
            "Merged large list is invalid.")
        self.assertTrue(lists_equal(expected, result),
            "Merged large list is incorrect.")

    # Test for the new linked list class (ex 2.14.*)
    def test_dummy(self) -> None:
        """Simple test for all class methods."""
        # __init__, head, and tail methods
        linked: LinkedListDummy = LinkedListDummy()
        self.assertIsNone(linked.head,
            "Head should be None in an empty list.")
        self.assertIsNone(linked.tail,
            "Tail should be None in an empty list")

        # add_in_tail
        for i in range(10):
            linked.add_in_tail(Node(i + 1))
        self.assertEqual(10, linked.tail.value,
            "add_in_tail() is incorrect.")

        # add_in_head
        for i in range(10):
            linked.add_in_head(Node(i + 1))
        self.assertEqual(10, linked.head.value,
            "add_in_head() is incorrect.")

        # delete
        node: Node | None = linked.head
        linked.delete(node)
        self.assertEqual(9, linked.head.value,
            "delete() is incorrect.")

        # insert
        node = linked.tail
        linked.insert(node, Node(11))
        self.assertEqual(11, linked.tail.value,
            "insert() is incorrect.")


if __name__ == '__main__':
    unittest.main()



