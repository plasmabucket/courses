# Комментарии

#### Добавить 7 уместных комментариев

1) ads1 - Задача №9  
Добавил TODO-комментарий про хэш-функцию. Текущая хэш-функция рабочая, но слишком примитивная.
```python
def hash_fun(self, key: str) -> int:
    computed_hash: int = 0
    # TODO: replace hash function with a more robust one
    for char in key:
        computed_hash += ord(char)
    return computed_hash % self.size
```

2) ads1 - Задача №9_2  
Тоже TODO-комментарий про хэш-функцию. Указал, что по условию задачи в функции должны присутствовать битовые операции.
```python
def hash_fun(self, key: bytes) -> int:
    # TODO: replace hash function with a more robust one
    # A new hash function MUST use bit operations in its calculations
    index: int = 0
    mask: int = self.hash_bits
    byte_count: int = 0
    while mask >= 8:
    ...
```

3) ads1 - Задача №8  
Тоже указание на плохую хэш-функцию.
```python
def hash_fun(self, value: str) -> int:
    index: int = 0
    # TODO: replace hash function with a more robust one
    for char in value:
        index += ord(char)
    return index % self.size
```

4) ads1 - Задача №7_2  
Добавил комментарий, объясняющий наличие приватного поля в классе-наследнике.
```python
class OrderedListExtra(OrderedList):

    def __init__(self, asc: bool) -> None:
        super(OrderedListExtra, self).__init__(asc)
        # This field has to be here, because the 'ascending' flag from the base
        # class is not inherited. The base class has 'ascending' as private by
        # the conditions of the task
        self.__ascending: bool = asc
```

5) ads1 - Задача №8_2  
Добавил предостережение и объяснение, почему было использован метод `super().put()` вместо `self.put()`.
```python
class DynamicHashTable(HashTable):
    ...
    def resize(self, new_size: int) -> None:
        old_slots: list[str | None] = self.slots
        self.size = new_size
        self.slots = [None] * new_size
        for value in old_slots:
            if value is None:
                continue
            # Usage of "super()" is deliberate
            # Using "self" method will cause the elements to be double-counted
            # and might trigger another resize
            super().put(value)
```

6) ads1 - Задача №4_2  
В реализации стека, хранящего свои минимальные значения, добавил указание, что в стеке минимумов повторяющиеся минимумы обязательно должны быть включены.
```python
class StackExtra:
    ...
    def push(self, value: int) -> None:
        # Usage of "<=" in 'is_new_min' is deliberate
        # Stack of minimums MUST include duplicates
        is_new_min: bool = value <= self.min_elements[-1]
        is_stack_empty: bool = len(self.min_elements) == 0
        if is_stack_empty or is_new_min:
            self.min_elements.append(value)
        self.sum += value
        self.stack.append(value)
```

7) ads1 - Задача №5_2  
Указал, что отбрасывание нового элемента при заполненной очереди -- намеренное поведение.
```python
class CycleQueue:
    ...
    def enqueue(self, item: Any) -> None:
        # "return" here is deliberate
        # If the queue is full, the element MUST be dropped
        if self.full():
            return
        self._buffer[self._head] = item
        self._head = (self._head + 1) % self._max_capacity
        self._count += 1
```


#### Убрать 5 излишних комментариев

1) 28z - Задача №6.  
Переименовал `grid_hits` в `point_sequence`. Вынес выражение `pow(10, CALC_PRECISION)` в отдельную константу `ORTHOGONAL_LENGTH`. Свернул две булевы переменные в одну. Заменил условный переход на тернарный оператор. Убрал две лишних переменных. После этих изменений, код стал достаточно выразителен, чтобы убрать три комментария.
```python
# ====== Было ======
def PatternUnlock(hit_count: int, hits: list[int]) -> str:
    """Generates a password based on a list of number hits."""
    # Translation of hits to a sequence of coordinates
    grid_hits: list[tuple[int, int]] = [GRID_MAP[hit] for hit in hits]

    # Go through each pair of coordinates and
    # add length of all line segments
    length_segments: list[int] = []
    for (start_x, start_y), (end_x, end_y) in pairwise(grid_hits):
        # Segment is diagonal when both coordinates change
        x_coord_changed: bool = start_x != end_x
        y_coord_changed: bool = start_y != end_y
        segment_len: int = pow(10, CALC_PRECISION)
        if x_coord_changed and y_coord_changed:
            segment_len = DIAGONAL_LENGTH
        length_segments.append(segment_len)
    line_length: int = sum(length_segments)
    del length_segments
    del grid_hits

    # Generate a password from line length
    password: str = str(round(line_length, ANSWER_PRECISION - CALC_PRECISION))
    password = password.replace("0", "")
    del line_length
    return password

```
```python
# ====== Стало ======
def PatternUnlock(hit_count: int, hits: list[int]) -> str:
    """Generates a password based on a list of number hits."""
    point_sequence: list[tuple[int, int]] = [GRID_MAP[hit] for hit in hits]

    line_length: int = 0
    for (start_x, start_y), (end_x, end_y) in pairwise(point_sequence):
        is_diagonal: bool = (start_x != end_x) and (start_y != end_y)
        segment_len: int = DIAGONAL_LENGTH if is_diagonal else ORTHOGONAL_LENGTH
        line_length += segment_len
    del point_sequence

    password: str = str(round(line_length, ANSWER_PRECISION - CALC_PRECISION))
    password = password.replace("0", "")
    del line_length
    return password
```

2) 28z - Задача №12  
Провёл рефакторинг решения. Количество строк получилось сократить вдвое. Комментарии стали не нужны.
```python
# ====== Было ======
def MassVote(n: int, vote_results: list[int]) -> str:
    # Determine total votes, greatest element and number of greatest elements
    total_votes: int = 0
    max_votes: int = vote_results[0]
    leaders: int = 0
    for num in vote_results:
        if num == max_votes:
            leaders += 1
        if num > max_votes:
            max_votes = num
            leaders = 1
        total_votes += num
    # Determine the index of the first greatest element
    winner_id: int = 0
    for i, candidate_votes in enumerate(vote_results):
        if candidate_votes == max_votes:
            winner_id = i + 1
            break
    # Generate a result string based on the data
    if leaders > 1:
        result: str = "no winner"
    elif max_votes * 2 > total_votes:
        result = "majority winner " + str(winner_id)
    else:
        result = "minority winner " + str(winner_id)
    return result
```
```python
# ====== Стало ======
def MassVote(num_candidates: int, vote_results: list[int]) -> str:
    winning_vote_count: int = max(vote_results)
    num_winners: int = vote_results.count(winning_vote_count)
    is_single_winner: bool = num_winners == 1
    total_votes: int = sum(vote_results)
    has_majority: bool = winning_vote_count * 2 > total_votes
    winner_id: int = 1 + vote_results.index(winning_vote_count)
    del winning_vote_count, num_winners, total_votes

    if is_single_winner and has_majority:
        return f"majority winner {winner_id}"
    if is_single_winner and not has_majority:
        return f"minority winner {winner_id}"
    return "no winner"
```
3) 28z - Задача №16  
Убрал комментарий из строки с условием. Вместо этого добавил константу и заменил цикл `for` на генератор списков. Комментарий, объясняющий почему используется данный алгоритм, оставил.

```python
# ====== Было ======
def MaximumDiscount(num_items: int, item_prices: list[int]) -> int:
    # Max discount is achieved by grouping expensive items together
    prices_sorted: list[int] = sorted(price, reverse=True)
    discount_total: int = 0
    for i in range(length):
        if i % 3 == 2:  # Every third item is free
            discount_total += price_sorted[i]
    return discount_total
```
```python
# ====== Стало ======
GROUP_SIZE: Final[int] = 3

def MaximumDiscount(num_items: int, item_prices: list[int]) -> int:
    # Max discount is achieved by grouping expensive items together
    prices_sorted: list[int] = sorted(item_prices, reverse=True)
    discounted_items: list[int] = [
        price
        for i, price in enumerate(prices_sorted)
        if (i + 1) % GROUP_SIZE == 0
    ]
    discount_total: int = sum(discounted_items)
    return discount_total
```

4) 28z - Задача №5  
Убрал комментарии без изменения кода. Код уже был достаточно выразителен, комментарии только дублировали информацию.
```python
# ====== Было ======
def SynchronizingTables(n: int, ids: list[int], salaries: list[int]) -> list[int]:
    """Returns a list of salaries ordered by corresponding id."""
    # Sort salary and id lists
    ids_sorted: list[int] = sorted(ids)
    salaries_sorted: list[int] = sorted(salaries)
    # Create a dictionary of correct id-salary pairs
    combined_table: dict[int, int] = dict(zip(ids_sorted, salaries_sorted))
    # Populate a new salary list using a dictionary of correct pairs
    salaries_ordered_by_ids: list[int] = [combined_table[key] for key in ids]
    return salaries_ordered_by_ids
```
```python
# ====== Стало ======
def SynchronizingTables(n: int, ids: list[int], salaries: list[int]) -> list[int]:
    """Returns a list of salaries ordered by corresponding id."""
    ids_sorted: list[int] = sorted(ids)
    salaries_sorted: list[int] = sorted(salaries)
    combined_table: dict[int, int] = dict(zip(ids_sorted, salaries_sorted))
    salaries_ordered_by_ids: list[int] = [combined_table[key] for key in ids]
    return salaries_ordered_by_ids
```

5) 28z - Задача №17  
Тоже убрал комментарии без изменения кода. Комментарии дублировали названия переменных. Необходимости в них не было.
```python
def LineAnalysis(line: str) -> bool:
    current_dot_count: int = 0  # How many dots we counted in the current segment
    previous_dot_count: int = 0  # Number of dots in the previous segment
    is_first_star: bool = True  # Flag to skip the first star
    is_first_segment: bool = True  # Flag to treat first segment as a reference
    ...
```
```python
def LineAnalysis(line: str) -> bool:
    current_dot_count: int = 0  
    previous_dot_count: int = 0
    is_first_star: bool = True
    is_first_segment: bool = True
    ...
```
