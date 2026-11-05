# Правильные комментарии

#### 12 правок комментариев


1. 28z - Задача №14 - п.1. информативный комментарий  
Старый комментарий пересказывал цикл. Сделал код более выразительным -- вынес формулу в функцию `waiting_time()` с переменными `cycle_position` и `is_red`. В самой функции уже указал комментарий, связанный с условием задачи -- что все светофоры начинают свою работу с красного света.

```python
# ====== Было ======
# Go through each coordinate and if a streetlight is encountered
# add required waiting time
time: int = 0
for coord in range(length):
    if coord in streetlights:
        red_time: int = streetlights[coord][0]
        green_time: int = streetlights[coord][1]
        time += max(0, red_time - time % (red_time + green_time))
    time += 1  # Time of traveling
```
```python
# ====== Стало ======
def waiting_time(arrival_time: int, red_time: int, green_time: int) -> int:
    # Every light starts red at time 0, then alternates red and green
    cycle_position: int = arrival_time % (red_time + green_time)
    is_red: bool = cycle_position < red_time
    time_to_wait: int = red_time - cycle_position if is_red else 0
    return time_to_wait


def Unmanned(track_len: int, num_streetlights: int, track: list[list[int]]) -> int:
    ...
    time: int = 0
    for coord in range(length):
        if coord in streetlights:
            red_time: int = streetlights[coord][0]
            green_time: int = streetlights[coord][1]
            time += waiting_time(time, red_time, green_time)
        time += 1
```

2. ads1 - Задача №11 - п.1. информативный комментарий  
Старый комментарий говорил только то, что целое число используется как битовый массив. Новый объясняет, почему был сделан такой выбор.

```python
# ====== Было ======
self.bit_array: int = 0  # A regular integer is used as a bit array
```
```python
# ====== Стало ======
# Regular integer is used as an array. Bit i is slot i of the filter.
# In Python, integers can be made of arbitrary size, and arbitrary
# bit length. So one integer can be a bit array of any length.
self.bit_array: int = 0
```

3. 28z - Задача №24 - п.6, TODO  
Старый комментарий пересказывал код. Заменил его на TODO-комментарий, указывающий на потенциальную оптимизацию алгоритма.

```python
# ====== Было ======
# Rotate rings
for i in range(T):
    for ring in rings:
        ring.insert(0, ring.pop())
```
```python
# ====== Стало ======
# TODO: optimize the solution by rotating for more than one step at a time
for i in range(T):
    for ring in rings:
        ring.insert(0, ring.pop())
```

4. 28z - Задача №23 - п.4, предупреждение о последствиях  
Старые комментарии говорили, что делает код, но не объясняли, почему уничтожение веток было сделано в два прохода. Добавил комментарий предупреждающий о том, что упрощать до уничтожение до одного прохода нельзя.

```python
# ====== Было ======
# Raise flags on the map of cells to be destroyed
for i in range(H * W):
    x_coord: int = i % W
    y_coord: int = i // W
    ...
...
# Destroy all cells on which the flag was raised
for i in range(H * W):
    x_coord = i % W
    y_coord = i // W
    ...
```
```python
# ====== Стало ======
# Branch destruction runs in two passes: flag, then clear.
# Clearing right away would make the result depend on iteration order:
# an old branch already zeroed by its neighbour would no longer
# destroy its own neighbours. This way, all old branches break at once
for i in range(H * W):
    x_coord: int = i % W
    y_coord: int = i // W
    ...
```

5. 28z - Задача №8 - п.3, прояснение  
Старый комментарий по большей части пересказывал цикл. Упростил код -- заменил цикл на `sum()`, а в комментарии оставил только обоснование такой формулы.

```python
# ====== Было ======
def SumOfThe(n: int, data: list[int]) -> int:
    # Since it is known, that one element is equal to the sum of all others
    # all we have to do is to sum all elements and divide the sum by 2
    total_sum: int = 0
    for num in data:
        total_sum += num
    return total_sum // 2
```
```python
# ====== Стало ======
def SumOfThe(n: int, data: list[int]) -> int:
    # Since it is known that one element is equal to the sum of all others,
    # the total sum of the list is equal to double of that element
    return sum(data) // 2
```

6. 28z - Задача №3 - п.3, прояснение  
Упростил код -- убрал индексацию с шагом 2 через использование `batched()` из `itertools`. Три комментария, пересказывавшие цикл, стали не нужны. Комментарии заменил единственным, проясняющим что координаты считаются с единицы.

```python
# ====== Было ======
min_distance: int = -1  # Minimum distance to a dispatch cell
# Calculating distances to dispatch cells
j: int
for j in range(0, L * 2, 2):
    distance: int = (abs(n_coord - battalion[j])
                     + abs(m_coord - battalion[j + 1]))
    # Finding distance to a closest dispatch cell
    if j == 0 or distance < min_distance:
        min_distance = distance
```
```python
# ====== Стало ======
# Coordinates in "battalion" start with index 1
min_distance: int = min(
    abs(n_coord - dispatch_n) + abs(m_coord - dispatch_m)
    for dispatch_n, dispatch_m in batched(battalion, 2)
)
```

7. 28z - Задача №20 - п.4, предупреждение о последствиях  
По условию задачи состояние редактора хранится в глобальных переменных. Добавил предупреждение об этом.

```python
# ====== Было ======
history: list[str] = [""]
current_position: int = 0
...
```
```python
# ====== Стало ======
# ! BastShoe() keeps editor state in these global variables !
history: list[str] = [""]
current_position: int = 0
...
```

8. 28z - Задача №25 - п.4, предупреждение о последствиях  
Добавил предупреждение о том, что решение имеет большую сложность по времени. Ограничений по условию никаких нет, но такой комментарий мне кажется полезным.

```python
# ====== Было ======
def transform(data: list[int]) -> list[int]:
    data_len: int = len(data)
    ...
```
```python
# ====== Стало ======
def transform(data: list[int]) -> list[int]:
    # This solution has a high time complexity.
    # Beware running it on long sequences
    data_len: int = len(data)
    ...
```

9. 28z - Задача №11 - п.5, усиление  
Комментарий пересказывал код. Заменил его на комментарий, объясняющий важность условия в цикле.

```python
# ====== Было ======
    # Remove leading zeroes
    while len(result) > 1 and result[0] == "0":
        result.pop(0)
```
```python
# ====== Стало ======
    # The check len(result) > 1 is important.
    # When s1 == s2 every digit is zero. The last digit must stay, so the answer is not an empty string
    while len(result) > 1 and result[0] == "0":
        result.pop(0)
        ...
```

10. 28z - Задача №7 - п.5, усиление  
Старый комментарий пересказывал код. Заменил его комментарием, указывающим, почему используется поиск слов через `in` вместо поиска через подстроки.
```python
# ====== Было ======
# Determine which lines contain the word we are looking for
result: list[int] = []
for line in lines:
    if search in line:
```

```python
# ====== Стало ======
result: list[int] = []
for line_words in lines:
    # 'line_words' is a list, so 'in' checks for an exact word.
    # Simple substring check would also find the word inside longer words
    if search in line_words:
    ...
```

11. 28z - Задача №20 - п.5, усиление  
Во время просмотра решения немного подправил граничный случай. Команда удаления символов в редакторе `2 0` стирала всю строку вместо того, чтобы удалить ноль символов и оставить строку без изменения. Условия задачи ничего не говорят про этот случай, и все тесты проходят без ошибок, но по-моему прежнее поведение было менее адекватным. В связи с этим заменил неинформативный комментарий на комментарий, описывающий причины текущего изменения.

```python
# ====== Было ======
if operation == "2":
    # Remove characters
    count: int = min(int(arguments[1]), len(history[current_position]))
    new_line: str = history[current_position][0:-count]
    history.append(new_line)
```

```python
# ====== Стало ======
if operation == "2":
    current_line: str = history[current_position]
    count: int = min(int(arguments[1]), len(current_line))
    # Using [:len()-count] instead of [:count]  is intentional
    # With count == 0 the negative index [:-0] equals [:0] and erases the whole line
    new_line: str = current_line[:len(current_line) - count]
    history.append(new_line)
```

12. ads1 - Задача №12 - п.6, TODO  
В классе был длинный комментарий о проблеме найденного решения, заканчивающийся фразой о том, что более хорошего решения я не нашёл.  Подправил его и сделал его TODO-комментарием.

```python
# ====== Было ======
    # 1) Collisions will be resolved by looking for the closest free slot.
    # 2) When we need to drop a key, we choose the one with the least amount
    # of hits.
    #
    # Given these rules, if we allow the table to be completely filled,
    # then the new key will always be inserted in the slot of the least
    # used key. Hashes of these keys are (in principle) uncorrelated,...
    # ...
    # ...
    # I couldn't come up with a simple and elegant solution for this problem,
    # so I left it as is.
```
```python
# ====== Стало ======
    # 1) Collisions will be resolved by looking for the closest free slot.
    # 2) When we need to drop a key, we choose the one with the least amount
    # of hits.
    # ...
    # ...
    # TODO: Find a solution to abscence of correlation between a hash and an index
    # in a table after many assignments
```
