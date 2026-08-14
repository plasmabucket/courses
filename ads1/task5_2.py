from typing import Any
import ctypes
from task5 import Queue


# Task 5 - exercise 3.* - Rotation of a queue for N steps
# Space complexity: O(1)
# Time complexity:  O(n)
def queue_rotate(queue: Queue, steps: int) -> None:
    if queue.size() == 0:
        return
    for i in range(steps):
        queue.enqueue(queue.dequeue())


# Task 5 - exercise 5.* - Reversal of a queue
# Space complexity: O(n)
# Time complexity:  O(n)
def queue_reverse(queue: Queue) -> None:
    stack: list[Any] = []
    while queue.size() > 0:
        stack.append(queue.dequeue())
    while len(stack) > 0:
        queue.enqueue(stack.pop())


# Task 5 - exercise 4.* - Queue, implemented with two stacks
class StackQueue:

    def __init__(self) -> None:
        self._count: int = 0
        self._stack_a: list[Any] = []
        self._stack_b: list[Any] = []

    # Space complexity: O(n)
    # Time complexity:  O(n)
    def enqueue(self, item: Any) -> None:
        while len(self._stack_b) > 0:
            self._stack_a.append(self._stack_b.pop())
        self._stack_a.append(item)
        self._count += 1

    # Space complexity: O(n)
    # Time complexity:  O(n)
    def dequeue(self) -> Any:
        if self.size() == 0:
            return None
        while len(self._stack_a) > 0:
            self._stack_b.append(self._stack_a.pop())
        self._count -= 1
        return self._stack_b.pop()

    def size(self) -> int:
        return self._count


# Task 5 - exercise 6.* - Cyclic queue based on a static array
class CycleQueue:

    def __init__(self, capacity: int) -> None:
        self._count: int = 0
        self._head: int = 0
        self._max_capacity: int = capacity
        self._buffer: ctypes.Array[Any] = (capacity * ctypes.py_object)()

    def full(self) -> bool:
        return self._max_capacity == self._count

    # Space complexity: O(1)
    # Time complexity:  O(1)
    def enqueue(self, item: Any) -> None:
        if self.full():
            return
        self._buffer[self._head] = item
        self._head = (self._head + 1) % self._max_capacity
        self._count += 1

    # Space complexity: O(1)
    # Time complexity:  O(1)
    def dequeue(self) -> Any:
        if self._count == 0:
            return None
        tail: int = (self._head - self._count) % self._max_capacity
        self._count -= 1
        return self._buffer[tail]

    def size(self) -> int:
        return self._count


"""
Рефлексия


Задание 3 - задача 5.* - Динамический массив на основе банковского метода.

Реализовал метод добавления элемента, но не реализовал метод удаления элемента,
т.к. не понял как к нему применить банковский метод.

Я понимаю суть банковского метода для анализа средней сложности по времени --
вместо результата: "O(1), но иногда O(n)", получаем результат: "в среднем O(3),
который равен O(1)".
Я понимаю почему стоимость добавления элемента является тройкой -- это
наименьшая цена, которую нужно платить, чтобы всегда оставаться в плюсе, когда
реаллокация работает по схеме: "при заполнении, умножай размер массива на 2".
Но я не понимаю, как этот метод применим к управлению массивом. Не к анализу
поведения, а именно к управлению.

В рекомендации говорится: "когда надо выполнять реаллокацию, вопрос
неоднозначный, можно по некоторому порогу в банке, но лучше когда внутренний
массив весь заполнен". Но если реаллокацию делать без опоры на банковский
баланс -- просто опираясь на заполненность массива, тогда зачем этот баланс нужен?

В материале задания №3, в описании банковского метода, говорится: "как только
накапливается достаточная сумма, чтобы оплатить очередную реаллокацию, она
выполняется. Причём цена её зависит от количества элементов в массиве и
выбирается например, как степень двойки, не превышающая новый размер буфера".
По этой схеме я реализовал метод append() для массива, но вот как реализовать
метод delete() не понял. Я не мог опираться на какой-то порог баланса при
уменьшении размера массива -- всегда можно было бы многократно повторить
"append-delete", чтобы набрать нужную сумму, вне зависимости от текущего
размера массива. Для предотвращения такого "заработка" стоимость удаления нужно
было бы сделать отрицательной, что противоречит смыслу метода. Опираться просто
на количество элементов не стал, так как опять возникал вопрос "зачем вообще
нужен баланс?".

В итоге, разрешить эти противоречия у меня не получилось. Поэтому в решении
метод удаления элемента не реализовал.

Насколько понял из рекомендации, реаллокацию лучше проводить, опираясь на
заполненность массива. И, насколько понимаю, банковский баланс здесь вообще
роли не играет -- просто ведётся учёт, не играющий роли в управлении.
Не понимаю тогда, зачем этот баланс нужен.

Не могу определить, насколько верным или допустимым является моё решение.


Задание 3 - задача 6.* - Многомерный динамический массив

Не додумался до того, что многомерный массив будет удобнее представлять
одномерным. О такой возможности знал, но в голове была идея, что задачу
нужно решать через рекурсию.

Соответственно, реализовал рекурсивные методы -- создание динамического массива
динамических массивов, обращение к элементам, и изменение размера по каждому
из измерений.

Не могу сказать, что рекурсивный подход в чём-то лучше одномерного массива.
Считаю, что с одномерным массивом сложность программы была бы меньше. 

Считаю решение верным, но не оптимальным.
"""



