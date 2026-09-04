from __future__ import annotations
from typing import Any


class PowerSet:

    def __init__(self) -> None:
        self.list: list[Any] = []

    def size(self) -> int:
        return len(self.list)

    def put(self, value: Any) -> None:
        if not self.get(value):
            self.list.append(value)

    def get(self, value: Any) -> bool:
        return value in self.list

    def remove(self, value: Any) -> bool:
        if not self.get(value):
            return False
        self.list.remove(value)
        return True

    def intersection(self, set2: PowerSet) -> PowerSet:
        result: PowerSet = PowerSet()
        for value in self.list:
            if set2.get(value):
                result.list.append(value)
        return result

    def union(self, set2: PowerSet) -> PowerSet:
        result: PowerSet = PowerSet()
        result.list = self.list.copy()
        for value in set2.list:
            result.put(value)
        return result

    def difference(self, set2: PowerSet) -> PowerSet:
        result: PowerSet = PowerSet()
        for value in self.list:
            if not set2.get(value):
                result.list.append(value)
        return result

    def issubset(self, set2: PowerSet) -> bool:
        for value in set2.list:
            if not self.get(value):
                return False
        return True

    def equals(self, set2: PowerSet) -> bool:
        if self.size() != set2.size():
            return False
        return self.issubset(set2)



