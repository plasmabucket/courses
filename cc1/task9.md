# Типы данных

### 12 улучшений кода по рекомендациям

Работал с решениями задач к курсу "28 задач".

1) Задача №6 - В вычислениях длины заменил число с плавающей запятой на целочисленное. Добавил константы для параметризации точности вычислений. Изменил формулы расчёта для поддержки констант точности.

Прежний заголовок программы:
```
ROOT_2: float = 1.4142135623730951  # Length of a diagonal
```
Новый заголовок:
```
CALC_PRECISION: Final[int] = 10  # Number of decimal digits in use for calculation
ANSWER_PRECISION: Final[int] = 5  # Precision with which the answer is generated
# Length of a diagonal line segment
DIAGONAL_LENGTH: Final[int] = round(math.sqrt(2) * pow(10, CALC_PRECISION))
```

2) Задача №6 - Добавил булевых переменных для повышения читаемости сложного условия.

Было:
```
if (grid[i][0] != grid[i + 1][0] and
        grid[i][1] != grid[i + 1][1]):
    line_len += DIAGONAL_LENGTH
```
Стало:
```
x_coord_changed: bool = grid_hits[i][0] != grid_hits[i + 1][0]
y_coord_changed: bool = grid_hits[i][1] != grid_hits[i + 1][1]
if x_coord_changed and y_coord_changed:
    line_len += DIAGONAL_LENGTH
```

3) Задача №7 - Заменил магический символ -- сепаратор слов -- на константу.

```
WORD_SEPARATOR: Final[str] = " "
```

4) Задача №9 - Заменил магический символ -- сепаратор слов -- на константу.

```
WORD_SEPARATOR: Final[str] = " "
```

5) Задача №9 - Добавил булевые переменные для повышения читаемости сложного условия.

Было:
```
if i % matrix_rows == matrix_rows - 1 and i // matrix_rows != matrix_columns - 1:
    ...
```
Стало:
```
is_column_traversed: bool = i % matrix_rows == matrix_rows - 1
is_last_column: bool = i // matrix_rows == matrix_columns - i
if is_column_traversed and not is_last_column:
    ...
```

6)  Задача №12 - Строки сообщений заменил на константы

Новые константы:
```
NO_WINNER_MSG: Final[str] = "no winner"
MAJORITY_WINNER_MSG: Final[str] = "majority winner "
MINORITY_WINNER_MSG: Final[str] = "minority winner "
```

7) Задача №19 - Заменил магический символ -- сепаратор слов -- на константу.

```
WORD_SEPARATOR: Final[str] = " "
```

8) Задача №20 - Заменил магические символы на константы.

Новые константы:
```
ADD_OPERATION: Final[str] = "1"
REMOVE_OPERATION: Final[str] = "2"
RETURN_OPERATION: Final[str] = "3"
UNDO_OPERATION: Final[str] = "4"
REDO_OPERATION: Final[str] = "5"
```

9) Задача №22 - Добавил булевые переменные для повышения читаемости сложного условия.

Было:
```
validity: bool = (num_of_rare_freqs == 0 or  # If all segments are the same or
    num_of_rare_freqs == 1 and  # If only one segment is different and
    (distribution_sorted[1][1] == 1 or  # its length is one, or
    # its length is one more than the most frequent
    distribution_sorted[1][1] - 1 == distribution_sorted[0][1] or
    # If there are two segments with frequency of one
    (distribution_sorted[0][0] == 1 and
    # And the first is one character longer than the second
    distribution_sorted_descending[0][1] - 1 == distribution_sorted_descending[1][1])))
```
Стало:
```
all_freqs_are_same: bool = num_of_rare_freqs == 0

is_single_correctable_freq: bool = (num_of_rare_freqs == 1 and
    # If only one segment is different and
    # its length is one, or
    (distribution_sorted[1][1] == 1 or
     # its length is one more than the most frequent
    distribution_sorted[1][1] - 1 == distribution_sorted[0][1]))

most_common_freq_is_correctable: bool = (num_of_rare_freqs == 1 and
    # If only one segment is different and
    # there are two segments with frequency of one
    (distribution_sorted[0][0] == 1 and
    # And the first is one character longer than the second
    distribution_sorted[0][1] - 1 == distribution_sorted[1][1]))

# The string is valid if...
validity: bool = (all_freqs_are_same or
    is_single_correctable_freq or
    most_common_freq_is_correctable)
```

10) Задача №23 - Заменил магические символы на константы.

Новые константы:
```
EMPTY_CELL: Final[str] = "."
BRANCH_CELL: Final[str] = "+"
```

11) Задача №23 - Заменил магический символ -- сепаратор чисел в строке -- на константу.
```
SEPARATOR: Final[str] = "="
```

12) Задача №28 - Заменил магические символы на константы.

Новые константы:
```
DOOR_OPEN: Final[str] = "1"
DOOR_CLOSED: Final[str] = "2"
```
