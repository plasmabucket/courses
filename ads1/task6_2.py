from typing import Any
import ctypes
from task6 import Deque
from task4 import Stack


# Task 6 - exercise 7.3.* - Determination of palindromes using deque
# Space complexity: O(n)
# Time complexity:  O(n)
def is_palindrome(string: str) -> bool:
    deque: Deque = Deque()
    for char in string:
        deque.addFront(char)
    while deque.size() > 1:
        if deque.removeTail() != deque.removeFront():
            return False
    return True


# Task 6 - exercise 7.6.* - Determination of bracket balance using a stack
# Space complexity: O(n)
# Time complexity:  O(n)
def bracket_balance(string: str) -> bool:
    stack: Stack = Stack()
    brackets: dict[str, str] = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    for char in string:
        if char in brackets:
            stack.push(char)
            continue
        prev_bracket: str = stack.pop()
        if brackets.get(prev_bracket) != char:
            return False
    return stack.size() == 0


# Task 6 - exercise 7.4.* - Minimal deque element in O(1) time
class DequeExtra:

    def __init__(self) -> None:
        self._deque: list[int] = []
        self._min_stack: Stack = Stack()  # Field for storing minimal values

    def add_front(self, item: int) -> None:
        self._deque.append(item)
        if (self._min_stack.size() == 0
                or item <= self._min_stack.peek()):
            self._min_stack.push(item)

    def add_tail(self, item: int) -> None:
        self._deque.insert(0, item)
        if (self._min_stack.size() == 0
                or item <= self._min_stack.peek()):
            self._min_stack.push(item)

    def remove_front(self) -> int | None:
        if self.size() == 0:
            return None
        item: int = self._deque.pop()
        if item == self._min_stack.peek():
            self._min_stack.pop()
        return item

    def remove_tail(self) -> int | None:
        if self.size() == 0:
            return None
        item: int = self._deque.pop(0)
        if item == self._min_stack.peek():
            self._min_stack.pop()
        return item

    def size(self) -> int:
        return len(self._deque)

    # Method that returns minimal value in the deque
    # Space complexity: O(1)
    # Time complexity:  O(1)
    def min_value(self) -> int | None:
        return self._min_stack.pop()


# Task 6 - exercise 7.5.* - Deque based on a dynamic array
# Based on a cyclic deque with a static buffer. In this case static buffer was
# replaced by a dynamic array.
# For addition/removal methods:
# Space complexity: o(1) - amortized cost
# Time complexity:  o(1) - amortized cost
class DequeDynamic:

    def __init__(self) -> None:
        self._count: int = 0
        self._capacity: int = 16
        self._array: ctypes.Array[Any] = self._make_array(self._capacity)
        self._front: int = 0
        self._tail: int = 0

    def add_front(self, item: Any) -> None:
        if self._count == self._capacity:
            self._resize(self._capacity * 2)
        if self._count != 0:
            self._front = (self._front + 1) % self._capacity
        self._array[self._front] = item
        self._count += 1

    def add_tail(self, item: Any) -> None:
        if self._count == self._capacity:
            self._resize(self._capacity * 2)
        if self._count != 0:
            self._tail = (self._tail - 1) % self._capacity
        self._array[self._tail] = item
        self._count += 1

    def remove_front(self) -> Any | None:
        if self._count == 0:
            return None
        if max(16, (self._count - 1) * 2) < self._capacity:
            self._resize(max(16, self._capacity * 2 // 3))
        item: Any = self._array[self._front]
        if self._count != 1:
            self._front = (self._front - 1) % self._capacity
        self._count -= 1
        return item

    def remove_tail(self) -> Any | None:
        if self._count == 0:
            return None
        if max(16, (self._count - 1) * 2) < self._capacity:
            self._resize(max(16, self._capacity * 2 // 3))
        item: Any = self._array[self._tail]
        if self._count != 1:
            self._tail = (self._tail + 1) % self._capacity
        self._count -= 1
        return item

    @staticmethod
    def _make_array(new_capacity: int) -> ctypes.Array[Any]:
        return (new_capacity * ctypes.py_object)()

    def _resize(self, new_capacity: int) -> None:
        new_array: ctypes.Array[Any] = self._make_array(new_capacity)
        index: int = self._tail
        for i in range(self._count):
            new_array[i] = self._array[index]
            index = (index + 1) % self._capacity
        self._tail = 0
        self._front = self._count - 1
        self._capacity = new_capacity
        self._array = new_array

    @property
    def size(self) -> int:
        return self._count

    @property
    def capacity(self) -> int:
        return self._capacity


"""
Рефлексия

Задание 4 - задача 5.*, 6.* - Определение баланса скобок.

Допустил ошибку при расширении функции от одного вида скобок к трём.

Первая часть задания выполнена верно -- сбалансированность скобок одного вида
определяется корректно. Когда расширял функцию от одного вида скобок к трём, 
подумал что сбалансированность у одного типа скобок определяется вне зависимости
от скобок других типов. Поэтому просто сделал три стека-счётчика для каждого
типа. И так как ошибка здесь была в интерпретации условия задачи, то тесты
здесь не помогли -- у меня сделан тест, в котором несбалансированные скобки
считаются, как сбалансированные.
  
Когда прочитал рекомендацию по решению, понял, почему надо было использовать
именно стек, а не простую переменную-счётчик. Когда решал задачу возник этот
вопрос, но теперь очевидно -- переменная не может содержать в себе тип предыдущей
скобки, а стек может.

Ошибка в понимании условия.


Задание 4 - задача 7.* - Минимальный элемент в стеке за O(1).

Верно использовал вспомогательный стек для хранения минимумов.
Логика добавления и удаления элементов из вспомогательного стека тоже верная.

Решение верное


Задание 4 - задача 8.* - Среднее значение всех элементов в списке за O(1)

Верно использовал дополнительную переменную, хранящую сумму элементов стека.
Как и в рекомендации, среднее значение получаю, разделяя сумму на количество
элементов.

Решение верное.


Задание 4 - задача 9.* - Постфиксная запись выражений. Калькулятор.

Допустил указанную в рекомендации ошибку -- оба аргумента выражения достаю из
стека в одной строке.

Пришлось немного посидеть и подумать о чём идёт речь в
рекомендации, но потом вспомнил, что и в C++ подобная неопределённость в 
порядке исполнения операций тоже была. Совсем забыл про это, т.к. думал, что
раз Python не компилируется, то и подвохов с неопределённым поведением не будет.
Ошибся. Не знал что такие эффекты и здесь есть.

Сам алгоритм к этим эффектам не восприимчив, т.к. я реализовал только необходимый
минимум для вычисления выражения в задаче: сложение, умножение и равенство.
Сложение и умножение коммутативные, и от порядка элементов не зависят, но сам
факт того, что для некоммутативных операций здесь может быть неопределённость, я не
осознавал, поэтому всё-равно считаю это ошибкой.

Указание на создание словаря с лямбда-функциями запомню. В будущем попытаюсь 
делать меньше "hardcoded" вещей -- буду стараться искать общее решение, вместо
множества частных.

Считаю решение допустимым. Ошибку запомнил на будущее.
"""



