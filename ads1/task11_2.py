from task11 import BloomFilter


# Task 11 - exercise 2.* - Merge of bloom filters.
# Space complexity: O(n)
# Time complexity:  O(1)
# Time is O(1) only when a filter size is small and the bitwise OR can be
# done in a single operation. For sizes larger than 64 bits time should be O(n)
#
# Using the formula for the probability of a false positive, the probability of
# the false positive for the combined filter should be:
# P = 0.6931 ^ (m / (n1 + n2))
# where m is the size of the filter, and n1, n2 - number of elements in the
# original filters.
def bf_merge(bf1: BloomFilter, bf2: BloomFilter) -> BloomFilter:
    result: BloomFilter = BloomFilter(bf1.filter_len)
    result.bit_array = bf1.bit_array | bf2.bit_array
    return result


# Task 11 - exercise 3.* - Bloom filter with element deletion.
class BloomDelete(BloomFilter):

    # Returns "True" if deletion was successful and "False" otherwise.
    # May delete values other than the target one.
    # Space complexity: O(1)
    # Time complexity:  O(1)
    def delete(self, str1: str) -> bool:
        if not self.is_value(str1):
            return False
        # Remove only one hash bit to reduce collateral damage.
        # This is enough to render the value as "not present" while minimizing
        # probability of deleting other values in the filter
        mask: int = self.hash1(str1)
        self.bit_array = self.bit_array & ~mask
        return True


# Task 11 - exercise 4.* - Restoration of values from the filter.

# Returns a list of strings. Inserting those strings in an empty filter
# should result in a copy of the original filter. This, however, does not
# guarantee that the returned set of strings is the original set.
# Space complexity: O(n^2)
# Time complexity:  O(n^3), where n is the size of the filter.
def val_extract(bfilter: BloomFilter) -> list[str]:
    filter_size: int = bfilter.filter_len
    result: list[str] = []
    for i in range(filter_size):
        if (bfilter.bit_array & (1 << i)) == 0:
            continue
        for j in range(i, filter_size):
            if (bfilter.bit_array & (1 << j)) == 0:
                continue
            unhashed_str: str | None = unhash(filter_size, i, j)
            if unhashed_str is None:
                continue
            result.append(unhashed_str)
    return result

# Function that attempts to restore a value from its hashes.
# Not guaranteed to return a string for every pair of hashes.
# Returned string isn't guaranteed to be the original string.
# Space complexity: O(1)
# Time complexity:  O(n), where n is the size of the filter.
def unhash(bf_size: int, hash1: int, hash2: int) -> str | None:
    # Random integers used in hash functions
    rand_int1: int = 17
    rand_int2: int = 223
    result: str = ""
    # Return a single character if possible
    if hash1 == hash2:
        result = chr(hash1)
        return result
    # Attempt to construct two-character long string that has the same hash
    # pair as provided
    ord1: int = 0
    hash_delta: int = (hash1 - hash2) % bf_size
    rand_int_delta: int = (rand_int1 - rand_int2) % bf_size
    cycle_broken: bool = False
    for i in range(bf_size):
        if hash_delta == (rand_int_delta * i) % bf_size:
            ord1 = i
            cycle_broken = True
            break
    if not cycle_broken:  # No two-character long solutions found
        # This search stops at string length 2.
        # Non-trivial solutions of greater lengths are harder to find.
        # Trivial solutions of greater lengths could be found by prepending any
        # amount of "ord(bf_size)" chars to a valid solution.
        # Adding "bf_size * k" to the ord() of any char of a solution also
        # returns a valid solution.
        return None
    ord2: int = (hash1 - ord1 * rand_int1) % bf_size
    result = chr(ord1) + chr(ord2)
    return result


"""
Рефлексия


Задание 9 - задача 5.* - Словарь на основе упорядоченного списка.

В своей реализации сделал методы, работающие со стандартным питоновским списком.
Т.к. список упорядоченный, то применил бинарный поиск для поиска по ключу.
На временную сложность добавления и удаления элемента это не повлияло, но 
методы поиска ключа и получения значения ускорились с O(n) до O(log n).

В данном доп. задании не отходил от схемы, реализованной в задании основном:
значение записывается в вспомогательный список под тем же индексом, что и
индекс его ключа. В рекомендации указана схема другая: в упорядоченном списке
хранить кортеж с ключом и индексом значения, а значение располагать в
вспомогательном списке так, как нам удобно.

Моя реализация оказывается медленнее рекомендованной, т.к. при вставке или
удалении ключа, передвигать элементы приходится и в массиве ключей, и в массиве
значений. В рекомендованной схеме необходимо передвигать значения только в
массиве ключей. Хоть сложность остаётся одной и той же -- O(n), из-за меньшего
количества перестановок производительность может отличаться в два раза.

В остальном, моё решение корректное. Ошибок не допустил.

Считаю решение допустимым, но не оптимальным.

! Однако, в тестах к этой задаче (и к 6.*) обнаружил ошибку. Метод delete()
работает с двумя массивами, но тестируется на корректность работы только с
массивом ключей. Корректность работы с массивом значений не проверяется.
Подобное недостаточное тестирование ранее уже приводило меня к отправке
некорректного решения (задание 6 - задача 7.4.*). На этот раз тупо повезло --
ошибки в алгоритме не было.
Над чем мне стоит поработать: при тестировании проверять корректность состояний
всех полей и всех их свойств в совокупности, а не ограничиваться проверкой
отдельных полей или каких-то их отдельных свойств.
"""



