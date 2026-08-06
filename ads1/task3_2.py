import ctypes
import math


# Task 3 = exercise 5.* - Dynamic array using banking method
class DynBanking:

    # Added two new fields - current balance and its limit
    def __init__(self) -> None:
        self.count: int = 0
        self.capacity: int = 16
        self.array = self._make_array(self.capacity)
        self._balance: int = 0  # Current "bank" balance
        self._limit: int = 32  # Current "cost" of reallocation

    def __len__(self) -> int:
        return self.count

    @staticmethod
    def _make_array(new_capacity: int):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, ind: int):
        if ind < 0 or ind >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[ind]

    def _resize(self, new_capacity: int) -> None:
        new_array = self._make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    # Append method, modified to use the banking method for reallocation
    # Space complexity: O(n) - worst case, o(1) - average case
    # Time complexity:  O(n) - worst case, o(1) - average case
    # Average time cost of a single append operation = 3 writing operations
    def append(self, itm) -> None:
        # Total cost - 3: cost of appending - 1, to the bank balance - 2
        self._balance += 2
        # Perform reallocation when we have enough balance in the bank
        if self._balance >= self._limit:
            self._balance -= self._limit
            new_capacity = 2 * self.capacity
            # Cost of reallocation: max power of 2 less than the capacity
            self._limit = 2 ** int(math.log2(new_capacity))
            self._resize(new_capacity)
        self.array[self.count] = itm
        self.count += 1


# Task 3 - exercise 6.* - Multidimensional dynamic array
# Supports any number of dimensions.
# Each dimension can be resized using dimension_size() method.
# All arrays corresponding to the same dimension are resized
# simultaneously.
class MultiDimArray:

    # Array is created by specifying a number of dimensions and a tuple
    # containing sizes of dimensions.
    # Array values are initialized by None.
    # dim_count can't be 0, dim_size can't be 0
    def __init__(self, dim_count: int, dim_sizes: tuple[int, ...]) -> None:
        self.count: int = dim_sizes[-dim_count]
        self.capacity: int = 4  # Minimum buffer size is 4
        while self.capacity < self.count:
            self.capacity *= 2
        self.array = self._make_array(self.capacity)
        if dim_count == 1:
            for i in range(self.count):
                self.array[i] = None
            return
        for i in range(dim_sizes[-dim_count]):
            self.array[i] = MultiDimArray(dim_count - 1, dim_sizes)

    def __len__(self) -> int:
        return self.count

    @staticmethod
    def _make_array(new_capacity: int):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, ind: int):
        if ind < 0 or ind >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[ind]

    # Added this method to be able to change values inside arrays
    def __setitem__(self, ind: int, val) -> None:
        if ind < 0 or ind >= self.count:
            raise IndexError("Index is out of bounds")
        self.array[ind] = val

    def _get_dim_sizes(self) -> tuple[int, ...]:
        if not isinstance(self.array[0], MultiDimArray):
            return (self.count, )
        return (self.count, ) + self.array[0]._get_dim_sizes()

    def _generate_element(self) -> MultiDimArray | None:
        dim_sizes: tuple[int, ...] = self._get_dim_sizes()
        if len(dim_sizes) == 1:
            return None
        dim_sizes = dim_sizes[1:]
        return MultiDimArray(len(dim_sizes), dim_sizes)

    def _resize(self, new_size: int) -> None:
        if (new_size > self.capacity
                or max(4, new_size * 2) < self.capacity):
            while max(4, new_size * 2) < self.capacity:
                self.capacity = max(4, self.capacity * 2 // 3)
            while new_size > self.capacity:
                self.capacity *= 2
            new_array = self._make_array(self.capacity)
            for i in range(min(self.count, new_size)):
                new_array[i] = self.array[i]
            for i in range(self.count, new_size):
                new_array[i] = self._generate_element()
            self.array = new_array
            self.count = new_size
            return
        for i in range(self.count, new_size):
            self.array[i] = self._generate_element()
        self.count = new_size

    # Takes a dimension index (starting from 1) and a new dimension size
    # Must be used only on the root array.
    def dimension_size(self, dim: int, new_size: int) -> None:
        if dim == 1:
            self._resize(new_size)
            return
        for i in range(self.count):
            self.array[i].dimension_size(dim - 1, new_size)


"""
Рефлексия

Задание 1 - задача 1.8.* - Суммирование двух связанных списков:

Проверяю равенство длин двух списков, но при несоответствии не выбрасываю
исключение, а возвращаю пустой список. Мне кажется, что так чуть лучше чем
исключение, но не совсем в этом уверен.

В заголовке цикла, как и рекомендовано, использую проверку только по одному
из списков (через for по длине).

Решение верное.
"""



