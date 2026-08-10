from task4 import Stack


# Task 4 - exercise 5.* - Determining parenthesis balance
#          exercise 6.* - Three types of brackets
# Spase complexity: O(n)
# Time complexity:  O(n)
# Time complexity measure assumes correct stack implementation -- operations
# are done on the tail of the list and take O(1) time.
# If pop() and push() take O(n) time, then function's time measure is O(n^2).
def bracket_balance(string: str) -> bool:
    normal: Stack = Stack()  # For "()" brackets
    square: Stack = Stack()  # For "[]" brackets
    curly: Stack = Stack()   # For "{}" brackets
    pop: bool | None = True
    for char in string:
        if char == "(":
            normal.push(True)
        if char == ")":
            pop = normal.pop()

        if char == "[":
            square.push(True)
        if char == "]":
            pop = square.pop()

        if char == "{":
            curly.push(True)
        if char == "}":
            pop = curly.pop()

        if pop is None:
            return False
    if (normal.size() != 0
            or square.size() != 0
            or curly.size() != 0):
        return False
    return True


# Task 4 - exercise 9.* - Postfix notation calculator
# Space complexity: O(n)
# Time complexity:  O(n)
def calculator(sequence: Stack) -> int:
    stack: Stack = Stack()
    result: int = 0
    while sequence.size() > 0:
        element: int | str = sequence.pop()
        if isinstance(element, int):
            stack.push(element)
            continue
        if element == "*":
            result = stack.pop() * stack.pop()
        if element == "+":
            result = stack.pop() + stack.pop()
        if element == "=":
            result = stack.pop()
            break
        stack.push(result)
    return result


class StackExtra:

    def __init__(self) -> None:
        self.stack: list[int] = []
        self.min_elements: list[int] = []
        self.sum: int = 0

    def size(self) -> int:
        return len(self.stack)

    def peek(self) -> int | None:
        if self.size() == 0:
            return None
        return self.stack[-1]

    # Task 4 - exercise 7.* - Minimal element in a stack in O(1) time
    # Space complexity: O(1)
    # Time complexity:  O(1)
    # Time O(1) is achieved by having an additional stack and modifying
    # pop() and push() methods.
    def min(self) -> int | None:
        if self.size() == 0:
            return None
        return self.min_elements[-1]

    # Task 4 - exercise 8.* - Average value of all elements in O(1) time
    # Space complexity: O(1)
    # Time complexity:  O(1)
    # Achieved by modifying pop() and push() methods.
    def average(self) -> float | int | None:
        if self.size() == 0:
            return None
        return self.sum / self.size()

    def pop(self) -> int | None:
        if self.size() == 0:
            return None
        if self.peek() == self.min_elements[-1]:
            self.min_elements.pop()
        self.sum -= self.peek()
        return self.stack.pop()

    def push(self, value: int) -> None:
        if (len(self.min_elements) == 0
                or value <= self.min_elements[-1]):
            self.min_elements.append(value)
        self.sum += value
        self.stack.append(value)


"""
Рефлексия


Задание 2 - задача 2.10.* - Переворачивание списка

Верно реализовал алгоритм -- прохожу по каждому узлу и меняю местами
поля 'next' и 'prev'. Про head и tail не забыл -- тоже их поменял.

Решение верное.


Задание 2 - задача 2.11.* - Проверка на циклы в списке

Логика определения циклов отличается от рекомендованной.
Не использовал в методе определения циклов метод определения длины.

В моей реализации метод определения длины проходит по списку, пока не дойдёт
до конца. В случае наличия циклов в списке, метод уйдёт в бесконечный цикл,
поэтому, применять схему "сделай len() шагов и проверь в конце ли ты" я не мог.

Чтобы организовать рекомендуемую логику мне необходимо было бы по-другому
определять длину: добавить новое поле -- длину списка, и вести учёт длины в
методах insert, add_in_* и delete. Я рассматривал такой вариант, но я подумал,
что он ненадёжный т.к. у пользователя есть доступ к узлам списка, и
пользователь может "вручную" проводить манипуляции -- удалять узлы, добавлять
узлы, может даже вставить целую цепочку узлов в середину списка, и ни одно из
этих действий не будет учтено. Поэтому я решил длину списка определять не
учётом, а проходом.

Соответственно, метод определения циклов у меня реализован без использования
длины списка -- проход по списку и проверка, что нет узлов, у которых бы
нарушался линейный порядок.

В любом случае, мой метод определения циклов имеет ту же сложность, что и
метод рекомендуемый: O(1) по пространству и O(n) по времени.

Считаю решение верным.


Задание 2 - задача 2.12.* - Сортировка списка

Свёл задачу к уже известной -- перевёл список в массив, и отсортировал массив
встроенным методом. Затем восстановил список по массиву.

Рекомендуемая сортировка пузырьком имеет временную сложность O(n^2), моя
реализация имеет сложность O(n log n) (Насколько мне известно, т.к. сложность
определяется встроенным методом). По пространственной сложности мой метод
проигрывает -- O(1) против O(n). Мне приходится создавать дополнительный массив
из всех элементов, а сортировка пузырьком может проводиться на самом списке.
Считаю это единственным минусом моей реализации.

Считаю решение верным.


Задание 2 - задача 2.13.* - Слияние списков

Мой алгоритм соответствует рекомендованному, но только без
обобщения на множество списков.

Происходит сравнение двух текущих элементов в списках, и в результат включается
подходящий. И так пока элементы не закончатся.

Считаю решение верным.


Задание 2 - задача 2.14.* - Dummy

Здесь немного затупил. Реализовал список с dummy узлами без создания
класса-наследника от Node. Отслеживал dummy-узлы через дополнительные поля
_start и _end у списка.

В самом условии задачи (2.14.*) было указано, что "лучше всего это делать через
наследование и перегрузку", но я тогда не понял что должно было наследоваться и
где должна была быть перегрузка. Только после прочтения рекомендации уже узнал
что к чему.

Я понимал, что создание дополнительного поля в классе Node нежелательно. Я это
обосновывал тем, что при создании, например, миллиона узлов с дополнительным
полем типа bool, в памяти будет сидеть минимум мегабайт полностью отведённый
под значения, которые всегда гарантированно будут иметь значение False. Было
очевидно, что "специальным значением" должны обладать только dummy-узлы, но вот
что этим значением мог выступать сам тип, я не догадался.

В своём решении старался сделать так, чтобы пользователю фиктивные узлы не
были видны. Поэтому сделал поля _start и _end скрытыми, а head и tail
переопределил -- сделал их property-методами. Так, сохраняется возможность
обращаться к head и tail, но при этом достигается упрощение методов вставки
и удаления -- как раз то, чего мы и добивались в задаче. Плюс, property-методы
дополнительно ограничивают пользователя класса -- теперь ему нельзя вручную
перезаписать значения полей head и tail.

Считаю своё решение приемлемым.
"""



