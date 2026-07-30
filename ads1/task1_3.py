"""Tests for task 1."""

import unittest
from task1 import Node, LinkedList
from task1_2 import sum_lists


def lists_equal(ll_1: LinkedList, ll_2: LinkedList) -> bool:
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


class Task1Tests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Tests for deletion (ex 1.1, 1.2)
    def test_delete_regression(self) -> None:
        """Tests correctness of deletion on a known and common case."""
        linked_l: LinkedList = LinkedList()
        for i in range(10):
            linked_l.add_in_tail(Node(i + 1))
        linked_l.delete(6, False)

        expected_l: LinkedList = LinkedList()
        for i in range(10):
            if i + 1 == 6:
                continue
            expected_l.add_in_tail(Node(i + 1))

        self.assertTrue(lists_equal(expected_l, linked_l),
            "Deletion is incorrect.")

    def test_delete_tail(self) -> None:
        """Tests deletion on the last element."""
        linked_l: LinkedList = LinkedList()
        for i in range(10):
            linked_l.add_in_tail(Node(i + 1))
        linked_l.delete(10, False)

        expected_l: LinkedList = LinkedList()
        for i in range(9):
            expected_l.add_in_tail(Node(i + 1))

        self.assertTrue(lists_equal(expected_l, linked_l),
            "Deletion of the last element is incorrect")
        self.assertEqual(9, linked_l.tail.value,
            "Deletion of the last element left incorrect list tail")
        self.assertIsNone(linked_l.tail.next,
            "Deletion of the last element left incorrect list tail")

    def test_delete_head(self) -> None:
        """Tests deletion on the first element."""
        linked_l: LinkedList = LinkedList()
        for i in range(10):
            linked_l.add_in_tail(Node(i + 1))
        linked_l.delete(1, False)

        expected_l: LinkedList = LinkedList()
        for i in range(1, 10):
            expected_l.add_in_tail(Node(i + 1))

        self.assertTrue(lists_equal(expected_l, linked_l),
            "Deletion of the first element is incorrect.")
        self.assertEqual(2, linked_l.head.value,
            "Deletion of the first element left incorrect list head")
        self.assertIsNotNone(linked_l.head.next,
            "Deletion of the first element left incorrect list head")

    def test_delete_head_and_tail(self) -> None:
        """Tests deletion of the only element in the list."""
        linked_l: LinkedList = LinkedList()
        linked_l.add_in_tail(Node(1))
        linked_l.delete(1, True)
        expected_l: LinkedList = LinkedList()
        self.assertTrue(lists_equal(expected_l, linked_l),
            "Simultaneous deletion of head and tail is incorrect.")
        self.assertIsNone(linked_l.head,
            "Deletion of the only element left incorrect list head")
        self.assertIsNone(linked_l.tail,
            "Deletion of the last element left incorrect list tail")

    def test_delete_null(self) -> None:
        """Tests deletion on an empty list."""
        linked_l: LinkedList = LinkedList()
        linked_l.delete(6, True)
        self.assertIsNone(linked_l.head,
            "Deletion in the empty list left incorrect list head")
        self.assertIsNone(linked_l.tail,
            "Deletion in the empty list left incorrect list tail")

    def test_delete_multiple(self) -> None:
        """Tests deletion of multiple matches."""
        linked_l: LinkedList = LinkedList()
        for i in range(10):
            linked_l.add_in_tail(Node(i + 1))
        for i in range(9, 0, -1):
            linked_l.add_in_tail(Node(i + 1))
        linked_l.delete(6, True)

        expected_l: LinkedList = LinkedList()
        for i in range(10):
            if i + 1 == 6:
                continue
            expected_l.add_in_tail(Node(i + 1))
        for i in range(9, 0, -1):
            if i + 1 == 6:
                continue
            expected_l.add_in_tail(Node(i + 1))

        self.assertTrue(lists_equal(expected_l, linked_l),
            "Deletion of multiple matching nodes is incorrect.")

    def test_delete_many(self) -> None:
        """Tests deletion of many elements in a huge list."""
        linked_l: LinkedList = LinkedList()
        for i in range(1000):
            linked_l.add_in_tail(Node(6))
        linked_l.delete(6, True)
        self.assertIsNone(linked_l.head,
            "Not all elements were deleted")
        self.assertIsNone(linked_l.tail,
            "Deletion of all elements left incorrect list tail")

    # Tests for cleaning (ex 1.3)
    def test_clear(self) -> None:
        """Tests if clean() actually clears the list."""
        linked_l: LinkedList = LinkedList()
        for i in range(10):
            linked_l.add_in_tail(Node(i + 1))
        linked_l.clean()
        self.assertIsNone(linked_l.head,
            "Cleaning left incorrect list head")
        self.assertIsNone(linked_l.tail,
            "Cleaning left incorrect list tail")

    # Tests for full node search (ex 1.4)
    def test_find_all_regression(self) -> None:
        """Tests correctness of a search on a known and common case."""
        linked_l: LinkedList = LinkedList()
        for i in range(10):
            linked_l.add_in_tail(Node(i + 1))
            linked_l.add_in_tail(Node(i + 1))
        found: list[Node] = linked_l.find_all(6)

        self.assertEqual(2, len(found),
            "Found more or less elements than expected.")
        self.assertEqual(6, found[0].value,
            "Wrong element got found.")
        self.assertEqual(6, found[1].value,
            "Wrong element got found.")

    def test_find_all_none(self) -> None:
        """Tests search on a case with no matches."""
        linked_l: LinkedList = LinkedList()
        for i in range(10):
            linked_l.add_in_tail(Node(i + 1))
        found: list[Node] = linked_l.find_all(11)
        self.assertEqual(0, len(found),
            "Elements got found when none expected.")

    def test_find_all_null(self) -> None:
        """Tests search on an empty list."""
        linked_l: LinkedList = LinkedList()
        found: list[Node] = linked_l.find_all(6)
        self.assertEqual(0, len(found),
            "Elements got found when none expected.")

    def test_find_all_single(self) -> None:
        """Tests search on a list with a single element."""
        linked_l: LinkedList = LinkedList()
        linked_l.add_in_tail(Node(6))
        found: list[Node] = linked_l.find_all(6)
        self.assertEqual(1, len(found),
            "Only a single match was expected.")
        self.assertEqual(6, found[0].value,
            "Incorrect element got found.")

    def test_find_all_many(self) -> None:
        """Tests search on a list with many elements."""
        linked_l: LinkedList = LinkedList()
        for i in range(1000):
            linked_l.add_in_tail(Node(6))
        found: list[Node] = linked_l.find_all(6)
        self.assertEqual(1000, len(found),
            "1000 matches were expected.")
        for i in range(1000):
            self.assertEqual(6, found[i].value,
                "Incorrect element got found.")

    # Tests for list length counting (ex 1.5)
    def test_len_regression(self) -> None:
        """Tests correctness of length counting on a known and common case."""
        linked_l: LinkedList = LinkedList()
        for i in range(10):
            linked_l.add_in_tail(Node(i + 1))
        self.assertEqual(10, linked_l.len(),
            "List length was determined incorrectly.")

    def test_len_sizes(self) -> None:
        """Tests length counting on lists of different sizes."""
        linked_l: LinkedList = LinkedList()
        self.assertEqual(0, linked_l.len(),
            "Empty list length was determined incorrectly.")

        linked_l.clean()
        linked_l.add_in_tail(Node(6))
        self.assertEqual(1, linked_l.len(),
            "Single element list length was determined incorrectly.")

        linked_l.clean()
        for i in range(1000):
            linked_l.add_in_tail(Node(i + 1))
        self.assertEqual(1000, linked_l.len(),
            "Large list length was determined incorrectly.")

    # Tests for element insertion (ex 1.6)
    def test_insert_regression(self) -> None:
        """Tests correctness of insertion on a known and common case."""
        linked_l: LinkedList = LinkedList()
        for i in range(10):
            linked_l.add_in_tail(Node(i + 1))
        node: Node | None = linked_l.find(6)
        insertion: Node = Node(-1)
        linked_l.insert(node, insertion)

        expected_l: LinkedList = LinkedList()
        for i in range(10):
            if i + 1 == 7:
                expected_l.add_in_tail(Node(-1))
            expected_l.add_in_tail(Node(i + 1))

        self.assertTrue(lists_equal(expected_l, linked_l),
            "Insertion is incorrect.")

    def test_insert_null(self) -> None:
        """Tests insertion on an empty list."""
        linked_l: LinkedList = LinkedList()
        node: Node | None = None
        insertion: Node = Node(-1)
        linked_l.insert(node, insertion)

        expected_l: LinkedList = LinkedList()
        expected_l.add_in_tail(Node(-1))

        self.assertTrue(lists_equal(expected_l, linked_l),
            "Insertion in the empty list is incorrect.")
        self.assertEqual(-1, linked_l.head.value,
            "Insertion in the empty list left incorrect list head")
        self.assertIsNone(linked_l.tail.next,
            "Insertion in the empty list left incorrect list tail")

    def test_insert_single(self) -> None:
        """Tests insertion on a single element list."""
        linked_l: LinkedList = LinkedList()
        linked_l.add_in_tail(Node(1))
        node: Node | None = linked_l.head
        insertion: Node = Node(-1)
        linked_l.insert(node, insertion)

        expected_l: LinkedList = LinkedList()
        expected_l.add_in_tail(Node(1))
        expected_l.add_in_tail(Node(-1))

        self.assertTrue(lists_equal(expected_l, linked_l),
            "Insertion in the single element list is incorrect.")
        self.assertEqual(1, linked_l.head.value,
            "Insertion in the single element list left incorrect list head")
        self.assertIsNone(linked_l.tail.next,
            "Insertion in the single element list left incorrect list tail")

    def test_insert_many(self) -> None:
        """Tests insertion on a large list."""
        linked_l: LinkedList = LinkedList()
        node: Node | None = None
        for i in range(1000):
            linked_l.add_in_tail(Node(i + 1))
            if i + 1 == 600:
                node = linked_l.tail
        insertion: Node = Node(-1)
        linked_l.insert(node, insertion)

        expected_l: LinkedList = LinkedList()
        for i in range(1000):
            expected_l.add_in_tail(Node(i + 1))
            if i + 1 == 600:
                expected_l.add_in_tail(Node(-1))

        self.assertTrue(lists_equal(expected_l, linked_l),
            "Insertion in a large list is incorrect.")
        self.assertEqual(1, linked_l.head.value,
            "Insertion in a large list left incorrect list head")
        self.assertIsNone(linked_l.tail.next,
            "Insertion in a large list left incorrect list tail")


class Task1ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Tests for the extra task - sum of two lists (ex *1.8)
    def test_sum_regression(self) -> None:
        """Tests solution on a known and common case."""
        list1: LinkedList = LinkedList()
        list2: LinkedList = LinkedList()
        for i in range(10):
            list1.add_in_tail(Node(i + 1))
            list2.add_in_tail(Node(10 - i))
        result: LinkedList = sum_lists(list1, list2)

        expected: LinkedList = LinkedList()
        for i in range(10):
            expected.add_in_tail(Node(11))

        self.assertTrue(lists_equal(expected, result),
            "Sum of lists is incorrect.")

    def test_sum_multilength(self) -> None:
        """Tests summation on lists of different lengths."""
        list1: LinkedList = LinkedList()
        list2: LinkedList = LinkedList()
        for i in range(10):
            list1.add_in_tail(Node(i + 1))
            list2.add_in_tail(Node(10 - i))
        list2.add_in_tail(Node(11))
        result: LinkedList = sum_lists(list1, list2)
        expected: LinkedList = LinkedList()
        self.assertTrue(lists_equal(expected, result),
            "Sum of lists of different sizes isn't an empty list.")

    def test_sum_null(self) -> None:
        """Tests summation of empty lists."""
        list1: LinkedList = LinkedList()
        list2: LinkedList = LinkedList()
        result: LinkedList = sum_lists(list1, list2)
        expected: LinkedList = LinkedList()
        self.assertTrue(lists_equal(expected, result),
            "Sum of empty lists isn't an empty list.")

    def tests_sum_single(self) -> None:
        """Tests summation of single element lists."""
        list1: LinkedList = LinkedList()
        list2: LinkedList = LinkedList()
        list1.add_in_tail(Node(1))
        list2.add_in_tail(Node(10))
        result: LinkedList = sum_lists(list1, list2)
        expected: LinkedList = LinkedList()
        expected.add_in_tail(Node(11))
        self.assertTrue(lists_equal(expected, result),
            "Sum of single element lists is incorrect.")

    def tests_sum_many(self) -> None:
        """Tests summation of large lists."""
        list1: LinkedList = LinkedList()
        list2: LinkedList = LinkedList()
        for i in range(1000):
            list1.add_in_tail(Node(i + 1))
            list2.add_in_tail(Node(1000 - i))
        result: LinkedList = sum_lists(list1, list2)

        expected: LinkedList = LinkedList()
        for i in range(1000):
            expected.add_in_tail(Node(1001))

        self.assertTrue(lists_equal(expected, result),
            "Sum of large lists is incorrect.")


if __name__ == '__main__':
    unittest.main()



