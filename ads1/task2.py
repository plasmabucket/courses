class Node:
    def __init__(self, v) -> None:
        self.value = v
        self.prev: Node | None = None
        self.next: Node | None = None


class LinkedList2:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def add_in_tail(self, item: Node) -> None:
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    # exercise 2.1
    def find(self, val) -> Node | None:
        node: Node | None = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # exercise 2.2
    def find_all(self, val) -> list[Node]:
        node: Node | None = self.head
        result: list[Node] = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    # exercise 2.3, 2.4
    def delete(self, val, all: bool = False) -> None:
        node: Node | None = self.head
        while node is not None:
            if node.value != val:
                node = node.next
                continue
            if node is self.tail:
                self.tail = node.prev
            if node is self.head:
                self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev
            if node.prev is not None:
                node.prev.next = node.next
            if not all:
                break
            node = node.next

    # exercise 2.5
    def insert(self, after_node: Node | None, new_node: Node) -> None:
        if after_node is None:
            self.add_in_tail(new_node)
            return
        new_node.prev = after_node
        new_node.next = after_node.next
        after_node.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        if new_node.next is None:
            self.tail = new_node

    # exercise 2.6
    def add_in_head(self, new_node: Node) -> None:
        new_node.prev = None
        if self.tail is not None:
            self.head.prev = new_node
            new_node.next = self.head
        if self.tail is None:
            self.tail = new_node
            new_node.next = None
        self.head = new_node

    # exercise 2.7
    def clean(self) -> None:
        self.head = None
        self.tail = None

    # exercise 2.8
    def len(self) -> int:
        length: int = 0
        node: Node | None = self.head
        while node is not None:
            length += 1
            node = node.next
        return length



