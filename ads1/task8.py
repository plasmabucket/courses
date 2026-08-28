class HashTable:

    def __init__(self, sz: int, stp: int) -> None:
        self.size: int = sz
        self.step: int = stp
        self.slots: list[str | None] = [None] * self.size

    def hash_fun(self, value: str) -> int:
        index: int = 0
        for char in value:
            index += ord(char)
        return index % self.size

    def seek_slot(self, value: str) -> int | None:
        index: int = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[index] is None:
                return index
            index = (index + self.step) % self.size
        return None

    def put(self, value: str) -> int | None:
        index: int | None = self.seek_slot(value)
        if index is None:
            return None
        self.slots[index] = value
        return index

    def find(self, value: str) -> int | None:
        index: int = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[index] == value:
                return index
            if self.slots[index] is None:
                return None
            index = (index + self.step) % self.size
        return None



