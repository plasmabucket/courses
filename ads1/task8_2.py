from task8 import HashTable


# Task 8 - exercise 3.* - Dynamic-size hash table
# Cost of table resize:
# Space complexity: O(n)
# Time complexity;  O(n)
class DynamicHashTable(HashTable):

    def __init__(self, sz: int, stp: int) -> None:
        super().__init__(sz, stp)
        self.count: int = 0  # Number of values stored in the table

    def put(self, value: str) -> int | None:
        result = super().put(value)
        # Increase the counter on successful insertion
        if result is not None:
            self.count += 1
        # Resize the table if necessary
        if self.count > self.size // 4 * 3:
            self.resize(self.size * 2)
        return result

    def resize(self, new_size: int) -> None:
        old_slots: list[str | None] = self.slots
        self.size = new_size
        self.slots = [None] * new_size
        # Go through all values of the old table and add them to the new one
        for value in old_slots:
            if value is None:
                continue
            super().put(value)


# Task 8 - exercise 4.* - Multi-hash table.
# Complexity of value lookup is the same as for the regular hash table:
# Space complexity: O(n)
# Time complexity:  O(1)
# From my rough and imprecise tests, multi-hash table fills up from 0% to 50%
# capacity 40% faster than regular hash table. This increase in speed probably
# tells more about the original hash function -- it tends to cluster values
# together, but still, this result is significant enough to indicate that
# multi-hash table really has an advantage at decreasing the number of collisions.
class MultiHashTable(HashTable):

    def hash_fun2(self, value: str) -> int:
        # To avoid infinite loops, returned value must not be 0
        index: int = 1
        if len(value) > 0:
            index += ord(value[0])
        return index % (self.size - 1) + 1

    def seek_slot(self, value: str) -> int | None:
        index: int = self.hash_fun(value)
        step: int = self.hash_fun2(value)  # step is now a hash-2
        for i in range(self.size):
            if self.slots[index] is None:
                return index
            index = (index + step) % self.size  # changed 'self.step' -> step
        return None

    def find(self, value: str) -> int | None:
        index: int = self.hash_fun(value)
        step: int = self.hash_fun2(value)  # Step is now a hash-2
        for i in range(self.size):
            if self.slots[index] == value:
                return index
            if self.slots[index] is None:
                return None
            index = (index + step) % self.size  # changed 'self.step' -> step
        return None


# Task 8 - exercise 5.* - DOS-attack and countermeasures.

# Attack on the hash table.
# This function takes a hash table and a starting value and fills the table
# with colliding values. An empty table filled in this way would have an
# O(n) lookup time.
def hash_table_dos(table: HashTable, seed: str) -> int:
    collisions: int = 0
    malicious_value: str = seed
    while table.put(malicious_value) is not None:
        collisions += 1
        malicious_value += chr(table.size)
    return collisions


# An example of a hash table which is resistant to the attack.
# Multiple tables can be initialized with different salts -- their hash
# functions will all be slightly different, and the attacker would need to
# modify their solution for each one. The default hash table is achieved by
# initialization with salt equal to zero.
class ResistantHashTable(HashTable):

    def __init__(self, sz: int, stp: int, salt: int) -> None:
        super().__init__(sz, stp)
        self.__salt: int = salt

    def hash_fun(self, value: str) -> int:
        raw_hash: int = super().hash_fun(value)
        return (raw_hash + len(value) * self.__salt) % self.size


"""
Рефлексия


Задание 6 - задача 7.3.* - Проверка строки на палиндром.

Реализованный алгоритм в точности соответствует алгоритму из рекомендации.
Сначала посимвольно загоняю строку в деку, а затем проверяю равенство символов,
взятых с двух концов деки.

Решение верное.


Задание 6 - задача 7.4.* - Минимальный элемент деки за O(1).

Допустил серьёзную ошибку, связанную с корректностью алгоритма. При заполнении
деки, а затем при чередующемся извлечении элементов с хвоста и головы, метод
min_value() вернёт некорректный результат.

Не поймал эту ошибку, т.к. тесты проводились без чередующегося извлечения --
был тест на извлечение элементов с хвоста, был тест на извлечение элементов
с головы, но теста с извлечением с двух концов не было.
И именно при чередовании возникает ошибка -- при работе только с одним концом
деки, результат всегда возвращается корректным.

Ошибку понял только после прочтения рекомендации -- в своей реализации
использую стек для хранения минимумов, что в рекомендации напрямую
указывается как ошибка. Использовать надо было не стек, а вспомогательную
деку, и алгоритм тоже должен был быть соответствующий.

Виню в этом недостаточное тестирование. Стоило написать тест с рандомным
изъятием элементов из деки -- случайным образом брать из головы или
хвоста. Такой тест бы выявил ошибку, и было бы невозможно его пройти без
полного переделывания метода.

Решение некорректное. Ошибка в алгоритме.


Задание 6 - задача 7.5.* - Двусторонняя очередь на базе динамического массива.

Свою реализацию деки, основанной на динамическом массиве, я строил, опираясь на
круговую очередь -- заменил в круговой очереди фиксированный буфер на
динамический и добавил недостающие методы для добавления в хвост/взятия с
головы, чтобы из односторонней очереди сделать двустороннюю.

Допустил указанную в рекомендации ошибку по смешиванию логики двух структур
данных: деки и динамического буфера. Всю логику поместил в один класс
DequeDynamic.

Класс DynArray из занятия 3 я не мог использовать для композиции,
т.к. в нём нельзя реализовать круговую очередь с временной эффективностью o(1)
для головы и хвоста одновременно.

Судя по рекомендации, мне необходимо было создать отдельный специальный класс
динамического буфера, позволяющий мне работать с его элементами без
ограничения по расположению элементов, как у массива. В этом классе буфера
была бы вся логика по увеличению/уменьшению его размера, и тогда можно
было бы использовать композицию, чтобы в классе DequeDynamic никакой логики,
связанной с размером буфера не было.

Решение рабочее, но с ошибкой.
"""



