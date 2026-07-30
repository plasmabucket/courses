class Node:

    def __init__(self, v) -> None:
        self.value = v
        self.next: Node | None = None


class LinkedList:

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def add_in_tail(self, item: Node) -> None:
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self) -> None:
        node: Node | None = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val) -> Node | None:
        node: Node | None = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # exercise 1.4
    def find_all(self, val) -> list[Node]:
        node: Node | None = self.head
        result: list[Node] = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    # exercise 1.1, 1.2
    def delete(self, val, all: bool = False) -> None:
        prev_node: Node | None = None
        node: Node | None = self.head
        while node is not None:
            if node.value != val:
                prev_node = node
                node = node.next
                continue
            if node is self.tail:
                self.tail = prev_node
            if node is self.head:
                self.head = node.next
            node = node.next
            if prev_node is not None:
                prev_node.next = node
            if not all:
                break

    # exercise 1.3
    def clean(self) -> None:
        self.head = None
        self.tail = None

    # exercise 1.5
    def len(self) -> int:
        length: int = 0
        node: Node | None = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    # exercise 1.6
    def insert(self, afterNode: Node | None, newNode: Node) -> None:
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
        if afterNode is self.tail:
            self.tail = newNode



