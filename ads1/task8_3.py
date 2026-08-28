"""Tests for task 8."""

import unittest
import random
import string
from task8 import HashTable
from task8_2 import (DynamicHashTable, MultiHashTable, ResistantHashTable,
                     hash_table_dos)


class Task8MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Test for the hash function
    def test_hash(self) -> None:
        """Tests validity of the hashes of random data."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            for j in range(100):
                length: int = random.randint(0, 100)
                value: str = "".join(
                    random.choices(string.ascii_letters, k=length))
                table_hash: int = table.hash_fun(value)

                self.assertGreaterEqual(table_hash, 0,
                    "Hash must be a non-negative number.")
                self.assertLess(table_hash, size,
                    "Hash must be less than a table size.")

    # Tests for the slot seeking method
    def test_slot_seek_empty(self) -> None:
        """Tests slot seeking method on an empty table."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            for j in range(100):
                length: int = random.randint(0, 100)
                value: str = "".join(
                    random.choices(string.ascii_letters, k=length))
                table_hash: int = table.hash_fun(value)
                table_slot: int | None = table.seek_slot(value)

                self.assertIsNotNone(table_slot,
                    "Suitable slot wasn't found in an empty table.")
                self.assertEqual(table_hash, table_slot,
                    "Slot index doesn't equal to hash despite no collisions.")

    def test_slot_seek_collision(self) -> None:
        """Tests slot seeking method on a case with collisions."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            index: int = random.randint(0, size - 1)
            table.slots = ["dummy"] * size
            table.slots[index] = None

            length: int = random.randint(0, 100)
            value: str = "".join(
                random.choices(string.ascii_letters, k=length))
            table_slot: int | None = table.seek_slot(value)

            self.assertIsNotNone(table_slot,
                "Suitable slot wasn't found despite there being one.")
            self.assertEqual(index, table_slot,
                "Wrong slot got found.")

    def test_slot_seek_full(self) -> None:
        """Tests slot seeking method on a full table."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            table.slots = ["dummy"] * size

            length: int = random.randint(0, 100)
            value: str = "".join(
                random.choices(string.ascii_letters, k=length))
            table_slot: int | None = table.seek_slot(value)

            self.assertIsNone(table_slot,
                "Suitable slot got found despite there being none.")

    # Tests for the value insertion method
    def test_put(self) -> None:
        """Tests how put() method fills a table."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            # Table will be filled with "a"s ond one "b".
            # A "b" will be inserted last.
            expected: list[str] = ["a"] * size
            expected[(ord("a") - step) % size] = "b"

            for j in range(size):
                value: str = "a"
                if j == size - 1:
                    value = "b"
                self.assertIsNotNone(table.put(value),
                    "Value could not be inserted.")

            self.assertEqual(expected, table.slots,
                "Values were inserted in the wrong slots.")

    def test_put_full(self) -> None:
        """Tests how put() method behaves with a full table."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            # Table will be filled with "a"s
            expected: list[str] = ["a"] * size

            for j in range(size):
                value: str = "a"
                self.assertIsNotNone(table.put(value),
                    "Value could not be inserted.")

            self.assertIsNone(table.put("b"),
                "Value was inserted despite table being full.")
            self.assertEqual(expected, table.slots,
                "Insertion in a full table overrode existing values.")

    # Tests for the value finding method
    def test_find(self) -> None:
        """Tests find() method on a case with no collisions."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            for j in range(size):
                value: str = chr(ord("0") + i)
                table.put(value)

            for j in range(size):
                value = chr(ord("0") + i)
                index: int | None = table.find(value)
                self.assertIsNotNone(index,
                    "Value wasn't found when it's present.")
                self.assertEqual(table.hash_fun(value), index,
                    "Wrong index was found.")

    def test_find_collision(self) -> None:
        """Tests find() method on a case with collisions."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            expected: int = (ord("a") - step) % size

            for j in range(size):
                value: str = "a"
                if j == size - 1:
                    value = "b"
                table.put(value)

            index: int | None = table.find("b")

            self.assertIsNotNone(index,
                "Value wasn't found when it's present.")
            self.assertEqual(expected, index,
                "Wrong index was found.")

    def test_find_none(self) -> None:
        """Tests find() method on a case with no collisions with no match."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            for j in range(size):
                value: str = chr(ord("0") + i)
                table.put(value)

            value = chr(ord("0") - 1)
            index: int | None = table.find(value)
            self.assertIsNone(index,
                "Value got found when it's not present.")

    def test_find_collision_none(self) -> None:
        """Tests find() method on a case with collisions with no match."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            for j in range(size):
                value: str = "a"
                table.put(value)

            index: int | None = table.find("b")

            self.assertIsNone(index,
                "Value got found when it's not present.")


class Task8ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Test for the dynamic-size hash table (ex 3.*)
    def test_dynamic_resize(self) -> None:
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: DynamicHashTable = DynamicHashTable(size, step)

            for j in range(size):
                value: str = chr(ord("0") + i)
                table.put(value)

            self.assertEqual(size, table.count,
                "Number of values in the table is wrong.")
            self.assertEqual(size * 2, table.size,
                "Table wasn't resized when more than 75% full.")

            for j in range(size):
                value = chr(ord("0") + i)
                index: int | None = table.find(value)
                self.assertIsNotNone(index,
                    "Value wasn't found when it should be present.")
                self.assertEqual(table.hash_fun(value), index,
                    "Wrong index was found.")

    # Tests for multi-hash table (ex 4.*)
    def test_hash2(self) -> None:
        """Tests validity of the hashes of random data."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: MultiHashTable = MultiHashTable(size, step)

            for j in range(100):
                length: int = random.randint(0, 100)
                value: str = "".join(
                    random.choices(string.ascii_letters, k=length))
                table_hash2: int = table.hash_fun2(value)

                self.assertGreaterEqual(table_hash2, 1,
                    "Hash 2 must be a positive number.")
                self.assertLess(table_hash2, size,
                    "Hash 2 must be less than a table size.")

    def test_multi_slot_seek_empty(self) -> None:
        """Tests slot seeking method on an empty table."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: MultiHashTable = MultiHashTable(size, step)

            for j in range(100):
                length: int = random.randint(0, 100)
                value: str = "".join(
                    random.choices(string.ascii_letters, k=length))
                table_hash: int = table.hash_fun(value)
                table_slot: int | None = table.seek_slot(value)

                self.assertIsNotNone(table_slot,
                    "Suitable slot wasn't found in an empty table.")
                self.assertEqual(table_hash, table_slot,
                    "Slot index doesn't equal to hash despite no collisions.")

    def test_multi_slot_seek_collision(self) -> None:
        """Tests slot seeking method on a case with collisions."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: MultiHashTable = MultiHashTable(size, step)

            index: int = random.randint(0, size - 1)
            table.slots = ["dummy"] * size
            table.slots[index] = None

            length: int = random.randint(0, 100)
            value: str = "".join(
                random.choices(string.ascii_letters, k=length))
            table_slot: int | None = table.seek_slot(value)

            self.assertIsNotNone(table_slot,
                "Suitable slot wasn't found despite there being one.")
            self.assertEqual(index, table_slot,
                "Wrong slot got found.")

    def test_multi_slot_seek_full(self) -> None:
        """Tests slot seeking method on a full table."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: MultiHashTable = MultiHashTable(size, step)

            table.slots = ["dummy"] * size

            length: int = random.randint(0, 100)
            value: str = "".join(
                random.choices(string.ascii_letters, k=length))
            table_slot: int | None = table.seek_slot(value)

            self.assertIsNone(table_slot,
                "Suitable slot got found despite there being none.")

    def test_multi_find(self) -> None:
        """Tests find() method on a case with no collisions."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: MultiHashTable = MultiHashTable(size, step)

            for j in range(size):
                value: str = chr(ord("0") + i)
                table.put(value)

            for j in range(size):
                value = chr(ord("0") + i)
                index: int | None = table.find(value)
                self.assertIsNotNone(index,
                    "Value wasn't found when it's present.")
                self.assertEqual(table.hash_fun(value), index,
                    "Wrong index was found.")

    def test_multi_find_collision(self) -> None:
        """Tests find() method on a case with collisions."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: MultiHashTable = MultiHashTable(size, step)

            expected: int = (ord("a") - table.hash_fun2("a")) % size

            for j in range(size):
                value: str = "a"
                if j == size - 1:
                    value = "b"
                table.put(value)

            index: int | None = table.find("b")

            self.assertIsNotNone(index,
                "Value wasn't found when it's present.")
            self.assertEqual(expected, index,
                "Wrong index was found.")

    def test_multi_find_none(self) -> None:
        """Tests find() method on a case with no collisions with no match."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: MultiHashTable = MultiHashTable(size, step)

            for j in range(size):
                value: str = chr(ord("0") + i)
                table.put(value)

            value = chr(ord("0") - 1)
            index: int | None = table.find(value)
            self.assertIsNone(index,
                "Value got found when it's not present.")

    def test_multi_find_collision_none(self) -> None:
        """Tests find() method on a case with collisions with no match."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: MultiHashTable = MultiHashTable(size, step)

            for j in range(size):
                value: str = "a"
                table.put(value)

            index: int | None = table.find("b")

            self.assertIsNone(index,
                "Value got found when it's not present.")

    # Test for the DOS tool (ex 5.*)
    def test_dos(self) -> None:
        """Tests that DOS tool generates collisions."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            table: HashTable = HashTable(size, step)

            seed: str = random.choice(string.ascii_letters)
            collisions: int = hash_table_dos(table, seed)

            self.assertEqual(table.size, collisions,
                "Table should be full.")

            collide_hash: int = table.hash_fun(seed)
            for j in range(size):
                table_val: str | None = table.slots[j]
                # Assert purely to stop mypy from issuing a warning
                assert table_val is not None
                self.assertEqual(collide_hash, table.hash_fun(table_val),
                    "Value doesn't have a colliding hash.")

    # Test for the resistant table (ex 5.*)
    def test_resistant(self) -> None:
        """Test to make sure the resistant table is functional."""
        sizes: list[int] = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # Run 1000 times
        for i in range(1000):
            size: int = random.choice(sizes)
            step: int = random.randint(1, size - 1)
            salt: int = random.randint(0, 10)
            table: ResistantHashTable = ResistantHashTable(size, step, salt)

            for j in range(size):
                value: str = chr(ord("0") + i)
                table.put(value)

            for j in range(size):
                value = chr(ord("0") + i)
                index: int | None = table.find(value)
                self.assertIsNotNone(index,
                    "Value wasn't found when it's present.")
                self.assertEqual(table.hash_fun(value), index,
                    "Wrong index was found.")


if __name__ == '__main__':
    unittest.main()



