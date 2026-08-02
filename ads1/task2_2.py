from task2 import Node, LinkedList2


class LinkedList2Ext(LinkedList2):

    # Task 2 - exercise 2.10.* - Reverse doubly linked list
    # Space complexity: O(1)
    # Time complexity: O(n)
    def list_reverse(self) -> None:
        node: Node | None = self.head
        while node is not None:
            node.next, node.prev = node.prev, node.next
            node = node.prev
        self.head, self.tail = self.tail, self.head

    # Task 2 - exercise 2.11.* - Determine cycles in a list
    # Space complexity: O(1)
    # Time complexity: O(n)
    def has_cycles(self) -> bool:
        # There are no cycles in an empty list
        if self.head is None:
            return False
        # If head has preceding nodes -- there is a cycle
        if self.head.prev is not None:
            return True
        # Check that every node progresses linearly
        # Next node's previous node should be the current one
        node: Node = self.head
        while node.next is not None:
            if node.next.prev is not node:
                return True
            node = node.next
        # If every node progresses linearly -- there are no cycles
        return False

    # Task 2 - exercise 2.12.* - Sort the list
    # Space complexity: O(n)
    # Time complexity: O(n log n)
    def list_sort(self) -> None:
        # Empty list is already sorted
        if self.head is None:
            return
        array: list[Node] = []
        node: Node | None = self.head
        while node is not None:
            array.append(node)
            node = node.next
        # Use standard sort() method for sorting.
        # It's complexity should be: Space - O(1), Time - O(n log n)
        array.sort(key=lambda x: x.value)
        # Recreate our list from the sorted array
        self.head = array[0]
        self.tail = array[-1]
        self.head.prev = None
        self.tail.next = None
        if len(array) > 1:
            self.head.next = array[1]
            self.tail.prev = array[-2]
        for i in range(1, len(array) - 1):
            array[i].prev = array[i - 1]
            array[i].next = array[i + 1]

    # Task 2 - exercise 2.13.* - Merge two sorted lists
    # Space complexity: O(n1 + n2)
    # Time complexity: O(n1 + n2)
    @staticmethod
    def list_merge(list1: LinkedList2, list2: LinkedList2) -> LinkedList2:
        # Takes two sorted lists and returns a third sorted list.
        result: LinkedList2 = LinkedList2()
        node1: Node | None = list1.head
        node2: Node | None = list2.head
        while node1 is not None:
            while node2 is not None:
                if node1.value < node2.value:
                    break
                result.add_in_tail(Node(node2.value))
                node2 = node2.next
            result.add_in_tail(Node(node1.value))
            node1 = node1.next
        while node2 is not None:
            result.add_in_tail(Node(node2.value))
            node2 = node2.next
        return result


# Task 2 - exercise 2.14.* - Linked list with dummy nodes
class LinkedListDummy:

    # Creates two dummy nodes at the beginning and the end of the list
    def __init__(self) -> None:
        # Fields are private since user shouldn't have access to dummy nodes
        self._start: Node = Node(None)
        self._end: Node = Node(None)
        self._start.prev = None
        self._start.next = self._end
        self._end.next = None
        self._end.prev = self._start

    # Examples of simplified methods

    def insert(self, after_node: Node, new_node: Node) -> None:
        new_node.next = after_node.next
        new_node.prev = after_node
        after_node.next.prev = new_node
        after_node.next = new_node

    def add_in_tail(self, new_node: Node) -> None:
        self.insert(self._end.prev, new_node)

    def add_in_head(self, new_node: Node) -> None:
        self.insert(self._start, new_node)

    def delete(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    # Special methods for getting the head and the tail of the list
    @property
    def head(self) -> Node | None:
        if self._start.next is not self._end:
            return self._start.next
        return None

    @property
    def tail(self) -> Node | None:
        if self._end.prev is not self._start:
            return self._end.prev
        return None



