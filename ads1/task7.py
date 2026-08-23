class Node:

    def __init__(self, v) -> None:
        self.value = v
        self.prev: Node | None = None
        self.next: Node | None = None


class OrderedList:

    # Exercise 1 - Private flag for ascending/descending order
    def __init__(self, asc: bool) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.__ascending: bool = asc
        self.length: int = 0

    # Exercise 2 - Method for element comparison (numerical)
    def compare(self, v1: float | int, v2: float | int) -> int:
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        return 1

    # Exercise 3 - Addition of an element to the list
    def add(self, value) -> None:
        new_node: Node = Node(value)
        self.length += 1
        if self.length == 1:
            self.head = new_node
            self.tail = new_node
            return

        node: Node | None = self.head
        while node is not None:
            if (self.__ascending
                    and self.compare(new_node.value, node.value) <= 0
                    or not self.__ascending
                    and self.compare(new_node.value, node.value) >= 0):
                break
            node = node.next
        if node is None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return

        new_node.prev = node.prev
        new_node.next = node
        if node.prev is not None:
            node.prev.next = new_node
        node.prev = new_node
        if node is self.head:
            self.head = new_node

    # Exercise 6 - Method for finding elements
    # Space complexity: O(1)
    # Time complexity:  O(n)
    # This method is slightly faster than the find() method of an
    # unordered list, but its complexity didn't change.
    def find(self, val) -> Node | None:
        node: Node | None = self.head
        while node is not None and self.compare(node.value, val) != 0:
            if (self.__ascending
                    and self.compare(node.value, val) == 1
                    or not self.__ascending
                    and self.compare(node.value, val) == -1):
                return None
            node = node.next
        return node

    # Exercise 4 - Deletion of an element by value
    def delete(self, val) -> None:
        node: Node | None = self.find(val)
        if node is None:
            return
        self.length -= 1
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node is self.tail:
            self.tail = node.prev
        if node is self.head:
            self.head = node.next

    def clean(self, asc: bool) -> None:
        self.__ascending = asc
        self.length = 0
        self.head = None
        self.tail = None

    def len(self) -> int:
        return self.length

    def get_all(self) -> list[Node]:
        r: list[Node] = []
        node: Node | None = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):

    def __init__(self, asc: bool) -> None:
        super(OrderedStringList, self).__init__(asc)

    # Exercise 5 - Comparison method overload to handle strings
    def compare(self, v1: str, v2: str) -> int:
        str1: str = v1.strip()
        str2: str = v2.strip()
        if str1 < str2:
            return -1
        if str1 == str2:
            return 0
        return 1



