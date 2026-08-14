# Exercise 1 - size(), enqueue(), dequeue()
# Exercise 2 - complexity of enqueue() and dequeue()
class Queue:

    def __init__(self) -> None:
        self.count: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    # Space complexity: O(1)
    # Time complexity:  O(1)
    def enqueue(self, item) -> None:
        node: Node = Node(item)
        if self.size() == 0:
            self.head = node
        if self.size() != 0:
            self.tail.next = node
        self.tail = node
        self.count += 1

    # Space complexity: O(1)
    # Time complexity:  O(1)
    def dequeue(self):
        if self.size() == 0:
            return None
        item = self.head.value
        self.head = self.head.next
        self.count -= 1
        return item

    def size(self) -> int:
        return self.count


class Node:

    def __init__(self, v) -> None:
        self.value = v
        self.next: Node | None = None



