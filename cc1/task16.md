# Плохие комментарии

#### 15 правок плохих комментариев

1) ads1 - Задача №1_2 - п.4. Шум  
Комментарий говорил то, что можно было понять из кода. Избавился от него и переписал строку, чтобы она была более выразительной.

```python
# ====== Было ======
...
if length != list2.len():  # Sum lists only if lengths match
    return combined_list
...
```
```python
# ====== Стало ======
...
if not is_len_equal:
    return combined_list
...
```

2) ads1 - Все тесты ко всем задачам - п.10. Обязательные комментарии  
При написании тестов я старался строго придерживаться PEP 8. PEP 8 рекомендует чтобы у всех классов, функций и методов были док-строки в заголовке. Сейчас я прошёлся по всем тестам к задачам в ads1 и удалил из классов док-строки, которые не дают ничего, кроме очевидной информации.  
Пример правки:

```python
# ====== Было ======
class Task1Tests(unittest.TestCase):
    """Class for unit tests for the main task."""
    ...
```
```python
# ====== Стало ======
class Task1Tests(unittest.TestCase):
    ...
```

3) ads1 - Задача №2_2 - п.4. Шум  
Убрал бессмысленный комментарий. Он говорил то, что можно мгновенно увидеть из кода.

```python
# ====== Было ======
# Special methods for getting the head and the tail of the list
@property
def head(self) -> Node | None:
    ...
```
```python
# ====== Стало ======
@property
def head(self) -> Node | None:
    ...
```

4) ads1 - Задача №6_2 - п.4. Шум  
Убрал комментарий, описывающий смысл поля. Вместо этого сделал имя поля более выразительным.

```python
# ====== Было ======
self._min_stack: Stack = Stack()  # Field for storing minimal values
```
```python
# ====== Стало ======
self._minimal_values: Stack = Stack()
```

5) ads1 - Задача №8_2 - п.4 Шум  
Убрал очевидный комментарий. Добавил выразительности у имени поля.

```python
# ====== Было ======
self.count: int = 0  # Number of values stored in the table
```
```python
# ====== Стало ======
self.value_count: int = 0
```

6) ads1 - Задача №8_2 - п.4 Шум  
Убрал бессмысленный комментарий. Не стал ничего изменять в коде, т.к. всё и так очевидно.

```python
# ====== Было ======
# Increase the counter on successful insertion
if result is not None:
    self.value_count += 1
```
```python
# ====== Стало ======
if result is not None:
    self.value_count += 1
```

7) ads1 - Задача №8_2 - п.12. Использование функции/переменной  
Убрал бессмысленный комментарий. Добавил булеву переменную для выразительности.

```python
# ====== Было ======
# Resize the table if necessary
if self.value_count > self.size * RESIZE_THRESHOLD:
   self.resize(self.size * 2)
```
```python
# ====== Стало ======
is_resize_needed: bool = self.value_count > self.size * RESIZE_THRESHOLD
if is_resize_needed:
    self.resize(self.size * 2)
```

8) ads1 - Задача 8_2 - п.3. Недостоверный комментарий  
Комментарий говорит, что все значения из старой таблицы добавляются в новую. Код говорит, что значения `None` должны пропускаться. Убрал комментарий полностью т.к. комментарий здесь вообще не уместен.

```python
# ====== Было ======
# Go through all values of the old table and add them to the new one
for value in old_slots:
    if value is None:
        continue
    super().put(value)
```
```python
# ====== Стало ======
for value in old_slots:
    if value is None:
        continue
    super().put(value)
```

9) ads1 - Задача №9_2 - п.12. Использование функции/переменной  
Убрал комментарий, пересказывающий код. Из  кода очевидно, что после проверок идёт бинарный поиск, поэтому дополнительно утверждать это в комментарии не надо. Добавил именованных булевых переменных для выразительности.

```python
# ====== Было ======
# Check extremes before binary search
if self.count == 0 or self.keys[0] > key:
    return 0
if self.keys[self.count - 1] < key:
    return self.count
...
```
```python
# ====== Стало ======
is_array_empty: bool = self.count == 0
if is_array_empty:
    return 0
is_less_than_min: bool = self.keys[0] > key
if is_less_than_min:
    return 0
is_greater_than_max: bool = self.keys[self.count - 1] < key
if is_greater_than_max :
    return self.count
...
```

10) ads1 - Задача №9_2 - п.12. Использование функции/переменной  
Убрал комментарий. Добавил булеву переменную для выразительности.

```python
# ====== Было ======
# Overwrite a value if key already exists
if index < self.count and self.keys[index] == key:
    self.values[index] = value
    return
```
```python
# ====== Стало ======
is_key_present: bool = index < self.count and self.keys[index] == key
if is_key_present:
    self.values[index] = value
    return
```

11) ads1 - Задача №9_2 - п.12. Использование функции/переменной  
Убрал комментарий. Добавил булеву переменную для выразительности.

```python
# ====== Было ======
# Don't add a key if the dictionary is full
if self.size == self.count:
    return
```
```python
# ====== Стало ======
is_dict_full: bool = self.size == self.count
if is_dict_full:
    return
```

12) ads1 - Задача №9_2 - п.12. Использование функции/переменной  
Заменил комментарий и блок кода на один вызов метода. В методе добавил выразительности для границ цикла.

```python
# ====== Было ======
    ...
    # Make space for a new key and value and insert them
    for i in range(self.count, index, -1):
        self.keys[i] = self.keys[i - 1]
        self.values[i] = self.values[i - 1]
    self.keys[index] = key
    self.values[index] = value
    self.count += 1
```
```python
# ====== Стало ======
    ...
    self._insert_pair(index, key, value)

...
def _insert_pair(self, index: int, key: str, value: Any) -> None:
    elements_to_move: range = range(index, self.count)
    for i in reversed(elements_to_move):
        self.keys[i + 1] = self.keys[i]
        self.values[i + 1] = self.values[i]
    self.keys[index] = key
    self.values[index] = value
    self.count += 1
```

13) ads1 - Задача №9_2 - п.12. Использование функции/переменной  
Заменил комментарий на булеву переменную.

```python
# ====== Было ======
# Don't delete anything if the key wasn't found
if index >= self.count or self.keys[index] != key:
    return None
```
```python
# ====== Стало ======
key_found: bool = index < self.count and self.keys[index] == key
if not key_found:
    return None
```

14) ads1 - Задача №9_2 - п.12. Использование функции/переменной  
Заменил комментарий и блок кода на один вызов метода. В методе добавил выразительности для границ цикла.

```python
# ====== Было ======
    ...
    # Adjust positions of keys and values
    for i in range(index, self.count - 1):
        self.keys[i] = self.keys[i + 1]
        self.values[i] = self.values[i + 1]
    self.keys[self.count - 1] = None
    self.values[self.count - 1] = None
    self.count -= 1
```
```python
# ====== Стало ======
    ...
    self._remove_pair(index)

...
def _remove_pair(self, index: int) -> None:
    elements_to_move: range = range(index + 1, self.count)
    for i in elements_to_move:
        self.keys[i - 1] = self.keys[i]
        self.values[i - 1] = self.values[i]
    del elements_to_move
    self.keys[self.count - 1] = None
    self.values[self.count - 1] = None
    self.count -= 1
```

15) ads1 - Задача №9_2 - п.12. Использование функции/переменной  
Заменил очевидный комментарий на именованную булеву переменную.

```python
# ====== Было ======
# If the key wasn't found -- return None
if index >= self.count or self.keys[index] != key:
    return None
```
```python
# ====== Стало ======
key_found: bool = index < self.count and self.keys[index] == key
if not key_found:
    return None
```
