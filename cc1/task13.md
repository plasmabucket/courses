# Массивы

#### 5 улучшений работы с массивами

Работал с решениями из курса 28z

1) Задача №6 - убрал прямую индексацию списка.

Использовал функцию `pairwise()` из стандартной библиотеки `itertools` для разбития списка точек на пары. Использовал её вместе с циклом `for` для итерации по полученным парам точек. В итоге, получилось полностью избавиться от прямой индексации списка.

```python
# == Было ==
for i in range(n - 1):
    x_coord_changed: bool = grid_hits[i][0] != grid_hits[i + 1][0]
    y_coord_changed: bool = grid_hits[i][1] != grid_hits[i + 1][1]
    ...
    
    
# == Стало ==
for (start_x, start_y), (end_x, end_y) in pairwise(grid_hits):
    x_coord_changed: bool = start_x != end_x
    y_coord_changed: bool = start_y != end_y
    ...
```

2) Задача №2 -  убрал прямую индексация списка.

Использовал функцию `batched()` из `itertools` для разбития списка на непересекающиеся пары. По условию задачи, на вход решения поступает список, где чередуются показания скорости и времени. С помощью `batched()` получилось выделить показания без использования индексации.

```python
# == Было ==
traveled_km: int = 0  # Distance im kilometers
time_h_old: int = 0  # Time in hours
# Walking through array with step width of 2
for i in range(0, len(speed_time_readings), 2):
    speed_kmph: int = speed_time_readings[i]
    time_h_new: int = speed_time_readings[i + 1]
    time_h_delta: int = time_h_new - time_h_old
    traveled_km += speed_kmph * time_h_delta
    time_h_old = time_h_new


# == Стало ==
traveled_km: int = 0  # Distance im kilometers
time_h_old: int = 0  # Time in hours
for speed_kmph, time_h_new in batched(speed_time_readings, 2, strict=True):
    time_h_delta: int = time_h_new - time_h_old
    traveled_km += speed_kmph * time_h_delta
    time_h_old = time_h_new
```

3) Задача №7 - убрал прямую индексацию списка.

Простое исправление -- заменил итерацию по индексам на итерацию по символам. Подправил логику в цикле, чтобы обращение к списку `wrapped_chars` шло только через метод `.append()`.

```python
# == Было ==
wrapped_chars: list[str] = list(input_data)
char_count: int = 0
for i in range(len(wrapped_chars)):
    char_count += 1
    if wrapped_chars[i] == WORD_SEPARATOR:
        char_count = 0
    # Long words are split into parts
    if char_count > line_len:
        wrapped_chars[i] = "".join([WORD_SEPARATOR, wrapped_chars[i]])
        char_count = 1


# == Стало ==
wrapped_chars: list[str] = []
char_count: int = 0
for char in input_data:
    char_count += 1
    if char == WORD_SEPARATOR:
        char_count = 0
    # Long words are split into parts
    if char_count > line_len:
        wrapped_chars.append(WORD_SEPARATOR)
        char_count = 1
    wrapped_chars.append(char)
```

4) Задача №12 - убрал прямую индексацию.

Использовал встроенную функцию `enumerate()`, чтобы проводить итерацию по элементам и также иметь доступ к их индексам.

```python
# == Было ==
winner_id: int = 0
for i in range(n):
    if vote_results[i] == max_votes:
        winner_id = i + 1
        break

# == Стало ==
winner_id: int = 0
for i, candidate_votes in enumerate(vote_results):
    if candidate_votes == max_votes:
        winner_id = i + 1
        break
```

5) Задача №19 - заменил список на итератор.

Использовал `iter()` для получения объекта, допускающего только последовательный доступ. Создал отдельные переменные и использовал их вместо списка с индексами.

```python
# == Было ==
catalog: dict[str, int] = {}
for line in lines:
    fields: list[str] = line.split(WORD_SEPARATOR)
    catalog.setdefault(fields[0], 0)
    catalog[fields[0]] += int(fields[1])


# == Стало ==
catalog: dict[str, int] = {}
for line in lines:
    fields: Iterator[str] = iter(line.split(WORD_SEPARATOR))
    product_name: str = next(fields)  # First field
    product_quantity: str = next(fields)  # Second field
    
    catalog.setdefault(product_name, 0)
    catalog[product_name] += int(product_quantity)
```
