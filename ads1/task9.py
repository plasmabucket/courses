class NativeDictionary:

    def __init__(self, sz: int) -> None:
        self.size: int = sz
        self.slots: list[str | None] = [None] * self.size
        self.values: list = [None] * self.size

    def hash_fun(self, key: str) -> int:
        index: int = 0
        for char in key:
            index += ord(char)
        return index % self.size

    def is_key(self, key: str) -> bool:
        index: int = self.hash_fun(key)
        for i in range(self.size):
            if self.slots[index] == key:
                return True
            if self.slots[index] is None:
                return False
            index = (index + 1) % self.size
        return False

    def put(self, key: str, value) -> None:
        index: int = self.hash_fun(key)
        for i in range(self.size):
            if self.slots[index] == key:
                self.values[index] = value
                return
            if self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                return
            index = (index + 1) % self.size

    def get(self, key: str):
        index: int = self.hash_fun(key)
        for i in range(self.size):
            if self.slots[index] == key:
                return self.values[index]
            if self.slots[index] is None:
                return None
            index = (index + 1) % self.size
        return None



