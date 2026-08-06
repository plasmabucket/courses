import ctypes


class DynArray:

    def __init__(self) -> None:
        self.count: int = 0
        self.capacity: int = 16
        self.array = self.make_array(self.capacity)

    def __len__(self) -> int:
        return self.count

    def make_array(self, new_capacity: int):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, ind: int):
        if ind < 0 or ind >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[ind]

    def resize(self, new_capacity: int) -> None:
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm) -> None:
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1


    # Exercise 1
    # Space complexity: O(n) - worst case, o(1) - average case
    # Time complexity:  O(n)
    def insert(self, ind: int, itm) -> None:
        if ind < 0 or ind > self.count:  # ind == self.count is valid
            raise IndexError("Index for insertion is out of bounds")
        if self.count < self.capacity:
            for i in range(self.count, ind, -1):
                self.array[i] = self.array[i - 1]
            self.array[ind] = itm
            self.count += 1
            return
        # In order not to copy the elements twice (once to resize,
        # once to insert), insert() has its own resize implementation.
        self.capacity = 2 * self.capacity
        new_array = self.make_array(self.capacity)
        for i in range(0, ind):
            new_array[i] = self.array[i]
        for i in range(self.count, ind, -1):
            new_array[i] = self.array[i - 1]
        new_array[ind] = itm
        self.array = new_array
        self.count += 1

    # Exercise 2
    # Space complexity: O(n) - worst case, o(1) - average case
    # Time complexity;  O(n)
    def delete(self, ind: int) -> None:
        if ind < 0 or ind >= self.count:
            raise IndexError("Index for deletion is out of bounds")
        if max(16, (self.count - 1) * 2) >= self.capacity:
            for i in range(ind, self.count - 1):
                self.array[i] = self.array[i + 1]
            self.count -= 1
            return
        # In order not to copy array elements twice (once to resize,
        # once to delete), delete() has its own resize implementation.
        self.capacity = max(16, self.capacity * 2 // 3)
        new_array = self.make_array(self.capacity)
        for i in range(0, ind):
            new_array[i] = self.array[i]
        for i in range(ind, self.count - 1):
            new_array[i] = self.array[i + 1]
        self.array = new_array
        self.count -= 1



