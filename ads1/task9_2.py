from typing import Any


# Task 9 - exercise 5.* - Dictionary based on an ordered list of fixed size.
class OrderedDictionary:

    def __init__(self, sz: int):
        self.size: int = sz  # Maximum size of the dictionary
        self.count: int = 0  # How many keys are in the dictionary
        self.keys: list[str | None] = [None] * self.size
        self.values: list[Any] = [None] * self.size

    # Return an index of the matching key if one exists. Otherwise,
    # return an index which the key should occupy if inserted.
    # Space complexity: O(1)
    # Time complexity:  O(log n)
    def _closest_index(self, key: str) -> int:
        # Check extremes before binary search
        if self.count == 0 or self.keys[0] > key:
            return 0
        if self.keys[self.count - 1] < key:
            return self.count
        # Binary search in an array -- takes O(log n)
        index: int = 0
        min_index: int = 0
        max_index: int = self.count - 1
        while min_index <= max_index:
            index = (min_index + max_index) // 2
            if self.keys[index] == key:
                return index
            if self.keys[index] < key:
                min_index = index + 1
                continue
            max_index = index - 1
        # In case of no matches, return the index of the appropriate slot
        # for insertion
        if self.keys[index] < key:
            index += 1
        return index

    # Insertion of a key-value pair into dictionary.
    # Space complexity: O(1)
    # Time complexity:  O(n)
    def put(self, key: str, value: Any) -> None:
        index: int = self._closest_index(key)
        # Overwrite a value if key already exists
        if index < self.count and self.keys[index] == key:
            self.values[index] = value
            return
        # Don't add a key if the list is full
        if self.size == self.count:
            return
        # Make space for a new key and value and insert them
        for i in range(self.count, index, -1):
            self.keys[i] = self.keys[i - 1]
            self.values[i] = self.values[i - 1]
        self.keys[index] = key
        self.values[index] = value
        self.count += 1

    # Removal of a key-value pair from a dictionary.
    # Returns a deleted value if the key existed and None otherwise.
    # Space complexity: O(1)
    # Time complexity:  O(n)
    def delete(self, key: str) -> Any:
        index: int = self._closest_index(key)
        # Don't delete anything if the key wasn't found
        if index >= self.count or self.keys[index] != key:
            return None
        value: Any = self.values[index]
        # Adjust positions of keys and values
        for i in range(index, self.count - 1):
            self.keys[i] = self.keys[i + 1]
            self.values[i] = self.values[i + 1]
        self.keys[self.count - 1] = None
        self.values[self.count - 1] = None
        self.count -= 1
        return value

    # Returns a value, corresponding to a key or None if key is not present.
    # Space complexity: O(1)
    # Time complexity:  O(log n)
    def get(self, key: str) -> Any:
        index: int = self._closest_index(key)
        # If the key wasn't found -- return None
        if index >= self.count or self.keys[index] != key:
            return None
        return self.values[index]

    # Checks if a key is present in a dictionary.
    # Space complexity: O(1)
    # Time complexity:  O(log n)
    def is_key(self, key: str) -> bool:
        index: int = self._closest_index(key)
        return index < self.count and self.keys[index] == key


# Task 9 - exercise 6.* - Dictionary of fixed-size byte strings.
# This exercise requires using bit operations in order to increase the speed of
# class methods. I can't think of ways how bit operations can be applied to
# any method other than a hash function. It doesn't seem like I can make put(),
# get(), is_key() and delete() any faster by using bit operations.
class ByteDictionary:

    def __init__(self, sz: int, key_sz: int) -> None:
        self.size: int = sz  # Maximum size of the dictionary
        self.count: int = 0  # How many keys are in the dictionary
        self.keys: list[bytes | None] = [None] * self.size
        self.values: list[Any] = [None] * self.size

        self.key_size: int = key_sz  # Length of the key in bytes
        # How many bits should be taken as a hash.
        # Can't take more bits than key bit size
        self.hash_bits: int = min((self.size - 1).bit_length(),
                                  self.key_size * 8)

    # Hash function takes first N bits of a key as its hash.
    # N is such that: 2**N >= (self.size - 1)
    # Space complexity: O(1)
    # Time complexity:  O(1)
    def hash_fun(self, key: bytes) -> int:
        index: int = 0
        mask: int = self.hash_bits

        byte_count: int = 0
        while mask >= 8:
            index += key[byte_count] * pow(256, byte_count)
            mask -= 8
            byte_count += 1
        if mask > 0:
            index += (key[byte_count] >> (8 - mask)) * pow(256, byte_count)

        return index % self.size

    # Space complexity: O(1)
    # Time complexity:  o(1)
    def is_key(self, key: bytes) -> bool:
        index: int = self.hash_fun(key)
        for i in range(self.size):
            if self.keys[index] == key:
                return True
            if self.keys[index] is None:
                return False
            index = (index + 1) % self.size
        return False

    # Space complexity: O(1)
    # Time complexity:  o(1)
    def put(self, key: bytes, value: Any) -> None:
        index: int = self.hash_fun(key)
        for i in range(self.size):
            if self.keys[index] == key:
                self.values[index] = value
                return
            if self.keys[index] is None:
                self.keys[index] = key
                self.values[index] = value
                return
            index = (index + 1) % self.size

    # Space complexity: O(1)
    # Time complexity:  o(1)
    def get(self, key: bytes) -> Any:
        index: int = self.hash_fun(key)
        for i in range(self.size):
            if self.keys[index] == key:
                return self.values[index]
            if self.keys[index] is None:
                return None
            index = (index + 1) % self.size
        return None

    # Removal of a key-value pair from a dictionary.
    # Returns a deleted value if the key existed and None otherwise.
    # Space complexity: O(1)
    # Time complexity:  o(1)
    def delete(self, key: bytes) -> Any:
        index: int = self.hash_fun(key)
        for i in range(self.size):
            if self.keys[index] == key:
                value: Any = self.values[index]
                self.keys[index] = None
                self.values[index] = None
                return value
            if self.keys[index] is None:
                return None
            index = (index + 1) % self.size
        return None


"""
Рефлексия


Задание 7 - задача 9.* - Слияние двух упорядоченных списков.

Алгоритм слияния сделал таким же, как и при слиянии списков в задании 2.
В рекомендации указано, что такое решение -- правильное.

Решение верное.


Задание 7 - задача 10.* - Проверка наличия под-списка в списке.

Основа алгоритма такая же, как и в рекомендации -- найти первую точку
вхождения и затем поэлементно сравнивать списки, переходя на следующую точку
вхождения при неудаче. Но в своей реализации я упустил несколько условий, при
которых поиск можно сразу останавливать.

В моём алгоритме нет остановки, когда оставшаяся часть основного списка меньше,
чем подсписок. И также нет остановки, когда во время сравнения элементов в
основном списке находится элемент больше, чем элемент подсписка.
Эти условия не влияют на корректность алгоритма, а только на его
производительность, поэтому тесты такую ошибку поймать не могли.
Остаётся только запомнить на будущее, что нужно уделять больше внимания
реализации алгоритмов.

Считаю решение допустимым, но не оптимальным.


Задание 7 - задача 11.* - Наиболее часто встречающееся значение.

Алгоритм совпадает с алгоритмом из рекомендации -- значение ищется за один
проход по списку. Сложность по времени получается O(n).

Решение верное.


Задание 7 - задача 12.* - Индекс заданного элемента в списке за O(log n).

Во время решения этой задачи я долго не мог понять, как можно реализовать
индексацию для связанного списка, ведь без индексации я точно не мог бы достичь
времени O(log n). Я предполагал, что придётся создавать упомянутый в занятии
"skip list", ведь в нём, насколько я понимаю, индексация возможна и достаточно
быстра. Но без поиска решений в интернете, самостоятельно додуматься до того
как сделать skip list у меня не получилось.

В итоге я создал метод, который выгружает связный список в стандартный
питоновский и затем работает уже с ним. В комментарии к решению указал, что
хоть поиск и работает за O(log n), создание доп. списка требует O(n) времени,
что в O(log n) не укладывается. Я думал, что с этим заданием я не справился.

Но в рекомендации указано, что так и нужно было -- для O(log n) необходима
индексация, а для индексации можно использовать массив. Всё ещё непонятно, как
так может быть, ведь создание массива всё-равно требует O(n) времени, но в
итоге получается, что моё решение совпадает с рекомендованным.

Сам алгоритм бинарного поиска сделал верно -- ошибок в перестановках границ
поиска нет.

Считаю решение верным.
"""



