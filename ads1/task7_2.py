from typing import Any
from task7 import OrderedList, Node


# Task 7 - exercise 9.* - Merge of two ordered lists
# Space complexity: O(n + m)
# Time complexity:  O(n + m)
# Takes two lists, both of which must have the same ascension/decension order.
def list_merge(list1: OrderedList,
               list2: OrderedList, asc: bool) -> OrderedList:
    result: OrderedList = OrderedList(asc)
    # Set the comparison value which corresponds to the ascension order
    cmp_val: int = 1 if asc else -1
    # Cycle over the lists backwards in order to accommodate
    # the add() method. This way it will always add elements to the beginning
    # of the new list, which will take only O(1) time. In comparison, adding
    # elements to the tail of the new list through add() will take O(n) time.
    node1: Node | None = list1.tail
    node2: Node | None = list2.tail
    while node1 is not None:
        while (node2 is not None
                and list1.compare(node1.value, node2.value) != cmp_val):
            result.add(node2.value)
            node2 = node2.prev
        result.add(node1.value)
        node1 = node1.prev
    while node2 is not None:
        result.add(node2.value)
        node2 = node2.prev
    return result


class OrderedListExtra(OrderedList):

    def __init__(self, asc: bool) -> None:
        super(OrderedListExtra, self).__init__(asc)
        self.__ascending: bool = asc

    # Task 7 - exercise 8.* - Removal of all duplicates in an ordered list
    # Space complexity: O(1)
    # Time complexity:  O(n)
    def rm_duplicates(self) -> None:
        node: Node | None = self.head
        current_val: Any = None
        while node is not None:
            if node is self.head or node.value != current_val:
                current_val = node.value
                node = node.next
                continue
            node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
            if node is self.tail:
                self.tail = node.prev
            self.length -= 1
            node = node.next

    # Task 7 - exercise 10.* - Searching a sub-list in a list
    # Space complexity: O(1)
    # Time complexity:  O(n * m)
    def find_sublist(self, sublist: OrderedList) -> bool:
        # Empty list is treated as a sublist of all lists
        if sublist.len() == 0:
            return True
        # Start list comparison at the first viable point. Move to the next
        # viable start point if the current one failed. Repeat until either a
        # match is found or no viable starting points left.
        first_value: Any = sublist.head.value
        entry_point: Node | None = self.find(first_value)
        while (entry_point is not None
               and self.compare(entry_point.value, first_value) == 0):
            main_point: Node | None = entry_point
            sub_point: Node | None = sublist.head
            match: bool = True
            while sub_point is not None:
                if (main_point is None
                        or self.compare(main_point.value, sub_point.value) != 0):
                    match = False
                    break
                main_point = main_point.next
                sub_point = sub_point.next
            if match:
                return True
            entry_point = entry_point.next
        return False

    # Task 7 - exercise 11.* - Find the most common value
    # Space complexity: O(1)
    # Time complexity:  O(n)
    # If there is a tie, method returns a value which is closer to the head
    def most_common(self) -> Any:
        most_common_val: Any = None
        highest_count: int = 0
        current_val: Any = None
        current_count: int = 0
        node: Node | None = self.head
        while node is not None:
            if (node is self.head
                    or self.compare(node.value, current_val) != 0):
                current_count = 0
                current_val = node.value
            current_count += 1
            if current_count > highest_count:
                highest_count = current_count
                most_common_val = node.value
            node = node.next
        return most_common_val

    # Task 7 - exercise 12.* - Find an index of an element in O(log n) time
    # Space complexity: O(n)
    # Time complexity:  O(n)
    # I couldn't figure out how to implement indexing for the linked list in
    # O(log n) time. The search itself is O(log n), but the creation of the
    # required array takes O(n) which is larger than O(log n)
    def find_index(self, value: Any) -> int:
        if self.len() == 0:
            return -1
        elements: list[Node] = self.get_all()  # Takes O(n) time
        if not self.__ascending:
            elements.reverse()
        if (self.compare(elements[0].value, value) == 1
                or self.compare(elements[-1].value, value) == -1):
            return -1
        # Binary search in an array -- takes O(log n)
        min_index: int = 0
        max_index: int = self.len() - 1
        while min_index <= max_index:
            index: int = (min_index + max_index) // 2
            cmp: int = self.compare(elements[index].value, value)
            if cmp == 0 and not self.__ascending:
                return self.len() - 1 - index
            if cmp == 0:
                return index
            if cmp == -1:
                min_index = index + 1
                continue
            max_index = index - 1
        return -1


"""
Рефлексия


Задание 5 - задача 3.* - Вращение очереди на N шагов.

Сделал так, как и указано в рекомендации -- цикл до n, выталкиваю элемент и
его же заталкиваю обратно.

Решение верное.


Задание 5 - задача 4.* - Очередь с помощью двух стеков.

Идею понял, но реализовал неоптимально. Не додумался, что добавлять элементы
в "исходящий" стек достаточно только тогда, когда он пуст. Вместо этого, мой
алгоритм старается запихнуть *все* элементы очереди в исходящий стек, к тому
моменту, когда нужно из него что-то взять. И для этого производится перегон
элементов из исходящего стека во входящий -- перегон, который, как я вижу
сейчас, абсолютно не нужен.
Спасает меня только то, что в условии задачи строгого требования к
производительности не было, а сам мой алгоритм не превышает O(n) по времени.

Считаю решение допустимым, но не оптимальным.
 

Задание 5 - задача 5.* - Обращение очереди.

Правильно реализовал алгоритм -- использовал стек, как буфер для хранения
элементов.

Решение верное.


Задание 5 - задача 6.* - Циклическая очередь на основе статического массива.

Вместо переменных head и tail использовал связку head и count -- количество
элементов в очереди. Адрес конца, откуда нужно доставать элементы, находил
через арифметику. Это позволило использовать весь массив целиком -- не 
приходится оставлять одну пустую ячейку, чтобы различать ситуации, когда
адреса head и tail совпадают. Вдобавок можно знать количество элементов в
очереди, что проблематично, если использовать только head и tail.
Весь остальной алгоритм совпадает с описанным в рекомендации.

Решение верное.
"""



