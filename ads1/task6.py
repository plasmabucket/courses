# Exercise 7.1:
# Time complexity for methods working with the beginning of the Python list
# will be O(n), while time complexity for methods working with its end will
# be only O(1).
# This difference exists because in order to insert (or delete) an element in
# the beginning of the list, all other elements in the list have to be moved.
# In contrast, insertion (or deletion) from the end of the Python list doesn't
# affect other elements at all -- work happens only on the inserted (deleted)
# element.

class Deque:
    def __init__(self) -> None:
        self.deque: list = []

    def addFront(self, item) -> None:
        self.deque.append(item)

    def addTail(self, item) -> None:
        self.deque.insert(0, item)

    def removeFront(self):
        if len(self.deque) == 0:
            return None
        return self.deque.pop()

    def removeTail(self):
        if len(self.deque) == 0:
            return None
        return self.deque.pop(0)

    def size(self) -> int:
        return len(self.deque)



