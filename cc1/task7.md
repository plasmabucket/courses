# ООП и интерфейсы

#### 3.1) Три примера методов-фабрик

В своём коде никогда перегрузкой конструкторов не пользовался, поэтому примеры взяты из чужого кода.  
Источник: https://github.com/kovidgoyal/calibre

В выбранном источнике нигде не нашёл методов, использующих перегрузку через декоратор `@singledispatch`. Поэтому искал конструкторы, использующие `if isinstance()` для обработки разных типов аргументов. Думаю, что такие конструкторы можно приравнять к перегруженным.


1) Класс Image  
Было:  
Конструктор, принимающий либо путь до файла, либо байтовую строку.
```
class Image:
    def __init__(self, path_or_bytes):
        if not isinstance(path_or_bytes):
            ... # Здесь файл, на который указывает путь, открывается как байтовая строка.
        ...  # Обработка байтовой строки
```
Стало:  
Два метода с наглядными именами, принимающие только один тип.
```
class Image:
    def __init__(self, data: bytes) -> None:
        ... # Обработка байтовой строки
    
    @classmethod
    def from_path(cls, path: str) -> Image:
        ... # Файл открывается в виде байтовой строки
        return Image(data)
    
    @classmethod
    def from_bytes(cls, data: bytes) -> Image:
        return Image(data)
```

2) Класс Sfnt  
Было:  
Конструктор, принимающий либо байтовую строку, либо функцию.
```
class Sfnt:
    def __init__(self, raw_or_get_bytes):
        if isinstance(raw_or_get_bytes, bytes):
            ... # Работа с байтовой строкой
        else:
            ... # Получение байтовой строки от функции
```
Стало:  
Два метода-фабрики с наглядными именами.
```
class Sfnt:
    def __init__(self, tables, version) -> Sfnt:
        ... # Установка переданных значений
    
    @classmethod
    def from_bytes(data: bytes) -> Sfnt:
        ... # Работа с байтовой строкой
        return Sfnt(tables, version)
    
    @classmethod
    def from_func(getter: function) -> Sfnt:
        ... # Получение байтов от функции
        return Sfnt(tables, version)
```

3) Класс MessageWriter  
Было:  
Конструктор с двойным разделением по типу аргумента. Данные обрабатываются по-разному, в зависимости от того, текст ли это, байтовая строка или открытый файл.
```
class MessageWriter:
    def __init__(self, buf, ...):
        if isinstance(buf, str):
            ...
        elif isinstance(buf, bytes):
            ...
        ...
```
Стало:  
Три метода-фабрики с понятными именами.
```
class MessageWriter:
    def __init__(self, ...):
        ...

    @classmethod
    def from_text(cls, string, ...):
        ...
        return cls(...)

    @classmethod
    def from_byte(cls, data, ):
        ...
        return cls(...)

    @classmethod
    def from_stream(cls, stream, ...):
        ...
        return cls(...)
```

#### 3.2) Именование интерфейсов/абстрактных классов

В задании требуется привести примеры только в случае, если был опыт использования интерфейсов или абстрактных классов. У меня такого опыта ещё нет.
