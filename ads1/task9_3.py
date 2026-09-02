"""Tests for task 9."""

import unittest
import random
import string
from task9 import NativeDictionary
from task9_2 import OrderedDictionary, ByteDictionary


class Task9MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Test for the hash function
    def test_hash(self) -> None:
        """Tests validity of the hashes of random data."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            dct: NativeDictionary = NativeDictionary(size)

            for j in range(100):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                dict_hash: int = dct.hash_fun(key)

                self.assertGreaterEqual(dict_hash, 0,
                    "Hash must be a non-negative number.")
                self.assertLess(dict_hash, size,
                    "Hash must be less than a dictionary size.")

    # Tests for the key presence check
    def test_is_key(self) -> None:
        """Tests key presence check on dictionaries that have a target key."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: NativeDictionary = NativeDictionary(size)

            target_key: str = ""
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                if j == target_ind:
                    target_key = key
                dct.put(key, True)

            self.assertTrue(dct.is_key(target_key),
                "Target key wasn't found when it is present.")

    def test_is_key_none(self) -> None:
        """Tests key presence check when key is absent."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: NativeDictionary = NativeDictionary(size)

            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                dct.put(key, True)

            target_key: str = "!"  # Symbol not present in dict keys

            self.assertFalse(dct.is_key(target_key),
                "Target key was found when it is not present.")

    # Tests for the key insertion/writing
    def test_put(self) -> None:
        """Tests that new keys are being added correctly."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: NativeDictionary = NativeDictionary(size)

            expected: list[tuple[str, int]] = []

            key: str = random.choice(string.ascii_letters)
            for j in range(key_count):
                # Char-by-char addition for guaranteed unique keys
                key = key + random.choice(string.ascii_letters)
                dct.put(key, j)
                expected.append((key, j))

            for key, value in expected:
                self.assertIn(key, dct.slots,
                    "Key was not inserted.")
                index: int = dct.slots.index(key)
                self.assertEqual(value, dct.values[index],
                    "Wrong value was assigned to a key.")

    def test_put_overwrite(self) -> None:
        """Tests that a value of an existing key can be overwritten."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: NativeDictionary = NativeDictionary(size)

            expected: list[tuple[str, int]] = []

            key: str = random.choice(string.ascii_letters)
            for j in range(key_count):
                # Char-by-char addition for guaranteed unique keys
                key = key + random.choice(string.ascii_letters)
                dct.put(key, j)
                expected.append((key, j))

            # Overwrite values by their negative equivalent
            for ind, item in enumerate(dct.slots):
                if item is None:
                    continue
                value: int = dct.values[ind] * -1
                dct.put(item, value)

            for key, value in expected:
                self.assertIn(key, dct.slots,
                    "Overwriting a value removed a key.")
                index: int = dct.slots.index(key)
                self.assertEqual(value * -1, dct.values[index],
                    "Value was overwritten incorrectly.")

    # Tests for the value retrieval
    def test_get(self) -> None:
        """Tests a retrival of a value from an existing key."""
        # Run 10000 times
        for i in range(10000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: NativeDictionary = NativeDictionary(size)

            target_key: str = ""
            target_value: int = 0
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                # Set a target value and update it in case of a duplicate key
                if j == target_ind or key == target_key:
                    target_key = key
                    target_value = j
                dct.put(key, j)

            self.assertEqual(target_value, dct.get(target_key),
                "Wrong value got retrieved.")

    def test_get_none(self) -> None:
        """Tests a retrival of a value from an absent key."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(0, size)  # Might be 0 keys
            dct: NativeDictionary = NativeDictionary(size)

            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                dct.put(key, j)

            target_key: str = "!"  # Symbol not present in dict keys

            self.assertIsNone(dct.get(target_key),
                "A value was retrieved from an absent key.")


class Task9ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Tests for the dictionary based on an ordered list (ex 5.*)
    def test_ord_closest_index_match(self) -> None:
        """Tests if closest_index() can find indexes of existing keys."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: OrderedDictionary = OrderedDictionary(size)

            target_key: str = ""
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                if j == target_ind:
                    target_key = key
                dct.put(key, j)

            index: int = dct.keys.index(target_key)

            self.assertEqual(index, dct._closest_index(target_key),
                "closest_index() didn't return an index of a match.")

    def test_ord_closest_index_none(self) -> None:
        """Tests if closest_index() returns correct indexes for insertion."""
        # Run 10000 times
        for i in range(10000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: OrderedDictionary = OrderedDictionary(size)

            target_key: str = ""
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                key += "11"  # Chars for consistent string order manipulation
                if j == target_ind:
                    target_key = key
                dct.put(key, j)

            index: int = dct.keys.index(target_key)

            self.assertEqual(index,
                             dct._closest_index(target_key[0:-2]),
                "Wrong closest lower index found.")
            self.assertEqual(index + 1,
                             dct._closest_index(target_key + "1"),
                "Wrong closest higher index found.")

    def test_ord_delete(self) -> None:
        """Tests deletion of existing keys."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: OrderedDictionary = OrderedDictionary(size)

            target_key: str = ""
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                if j == target_ind:
                    target_key = key
                dct.put(key, True)

            expected: list[str | None] = dct.keys.copy()
            expected.remove(target_key)
            expected.append(None)
            dct.delete(target_key)

            self.assertEqual(expected, dct.keys,
                "Target key wasn't deleted.")

    def test_ord_delete_none(self) -> None:
        """Tests deletion of keys not in dictionary."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: OrderedDictionary = OrderedDictionary(size)

            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                dct.put(key, True)

            expected: list[str | None] = dct.keys.copy()
            dct.delete("!")  # Symbol not present in dict keys

            self.assertEqual(expected, dct.keys,
                "An incorrect key was deleted.")

    def test_ord_is_key(self) -> None:
        """Tests key presence check on dictionaries that have a target key."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: OrderedDictionary = OrderedDictionary(size)

            target_key: str = ""
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                if j == target_ind:
                    target_key = key
                dct.put(key, True)

            self.assertTrue(dct.is_key(target_key),
                "Target key wasn't found when it is present.")

    def test_ord_is_key_none(self) -> None:
        """Tests key presence check when key is absent."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: OrderedDictionary = OrderedDictionary(size)

            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                dct.put(key, True)

            target_key: str = "!"  # Symbol not present in dict keys

            self.assertFalse(dct.is_key(target_key),
                "Target key was found when it is not present.")

    def test_ord_put(self) -> None:
        """Tests that new keys are being added correctly."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: OrderedDictionary = OrderedDictionary(size)

            expected: list[tuple[str, int]] = []

            key: str = random.choice(string.ascii_letters)
            for j in range(key_count):
                # Char-by-char addition for guaranteed unique keys
                key = key + random.choice(string.ascii_letters)
                dct.put(key, j)
                expected.append((key, j))

            for key, value in expected:
                self.assertIn(key, dct.keys,
                    "Key was not inserted.")
                index: int = dct.keys.index(key)
                self.assertEqual(value, dct.values[index],
                    "Wrong value was assigned to a key.")

    def test_ord_put_overwrite(self) -> None:
        """Tests that a value of an existing key can be overwritten."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: OrderedDictionary = OrderedDictionary(size)

            expected: list[tuple[str, int]] = []

            key: str = random.choice(string.ascii_letters)
            for j in range(key_count):
                # Char-by-char addition for guaranteed unique keys
                key = key + random.choice(string.ascii_letters)
                dct.put(key, j)
                expected.append((key, j))

            # Overwrite values by their negative equivalent
            for ind, item in enumerate(dct.keys):
                if item is None:
                    continue
                value: int = dct.values[ind] * -1
                dct.put(item, value)

            for key, value in expected:
                self.assertIn(key, dct.keys,
                    "Overwriting a value removed a key.")
                index: int = dct.keys.index(key)
                self.assertEqual(value * -1, dct.values[index],
                    "Value was overwritten incorrectly.")

    def test_ord_get(self) -> None:
        """Tests a retrival of a value from an existing key."""
        # Run 10000 times
        for i in range(10000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(1, size)
            dct: OrderedDictionary = OrderedDictionary(size)

            target_key: str = ""
            target_value: int = 0
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                # Set a target value and update it in case of a duplicate key
                if j == target_ind or key == target_key:
                    target_key = key
                    target_value = j
                dct.put(key, j)

            self.assertEqual(target_value, dct.get(target_key),
                "Wrong value got retrieved.")

    def test_ord_get_none(self) -> None:
        """Tests a retrival of a value from an absent key."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            key_count: int = random.randint(0, size)  # Might be 0 keys
            dct: OrderedDictionary = OrderedDictionary(size)

            for j in range(key_count):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                dct.put(key, j)

            target_key: str = "!"  # Symbol not present in dict keys

            self.assertIsNone(dct.get(target_key),
                "A value was retrieved from an absent key.")

    # Tests for the dictionary of fixed-size byte strings (ex 6.*)
    def test_byte_hash(self) -> None:
        """Tests validity of the hashes of random data."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 512)
            key_len: int = random.randint(1, 10)
            dct: ByteDictionary = ByteDictionary(size, key_len)

            for j in range(100):
                key: bytes = bytes(random.choices(range(255), k=key_len))
                dict_hash: int = dct.hash_fun(key)

                self.assertGreaterEqual(dict_hash, 0,
                    "Hash must be a non-negative number.")
                self.assertLess(dict_hash, size,
                    "Hash must be less than a dictionary size.")

    def test_byte_delete(self) -> None:
        """Tests deletion of existing keys."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 512)
            key_len: int = random.randint(1, 10)
            key_count: int = random.randint(1, size)
            dct: ByteDictionary = ByteDictionary(size, key_len)

            target_key: bytes = b""
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key: bytes = bytes(random.choices(range(255), k=key_len))
                if j == target_ind:
                    target_key = key
                dct.put(key, True)

            expected: list[bytes | None] = dct.keys.copy()
            expected[expected.index(target_key)] = None
            dct.delete(target_key)

            self.assertEqual(expected, dct.keys,
                "Target key wasn't deleted.")

    def test_byte_delete_none(self) -> None:
        """Tests deletion of keys not in dictionary."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 512)
            key_len: int = random.randint(1, 10)
            key_count: int = random.randint(1, size)
            dct: ByteDictionary = ByteDictionary(size, key_len)

            for j in range(key_count):
                key: bytes = bytes(random.choices(range(254), k=key_len))
                dct.put(key, True)

            expected: list[bytes | None] = dct.keys.copy()
            dct.delete(bytes(255))  # Value not present in dict keys

            self.assertEqual(expected, dct.keys,
                "An incorrect key was deleted.")

    def test_byte_is_key(self) -> None:
        """Tests key presence check on dictionaries that have a target key."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 512)
            key_len: int = random.randint(1, 10)
            key_count: int = random.randint(1, size)
            dct: ByteDictionary = ByteDictionary(size, key_len)

            target_key: bytes = b""
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key: bytes = bytes(random.choices(range(255), k=key_len))
                if j == target_ind:
                    target_key = key
                dct.put(key, True)

            self.assertTrue(dct.is_key(target_key),
                "Target key wasn't found when it is present.")

    def test_byte_is_key_none(self) -> None:
        """Tests key presence check when key is absent."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 512)
            key_len: int = random.randint(1, 10)
            key_count: int = random.randint(1, size)
            dct: ByteDictionary = ByteDictionary(size, key_len)

            for j in range(key_count):
                key: bytes = bytes(random.choices(range(254), k=key_len))
                dct.put(key, True)

            target_key: bytes = bytes(255)  # Value not present in dict keys

            self.assertFalse(dct.is_key(target_key),
                "Target key was found when it is not present.")

    def test_byte_put(self) -> None:
        """Tests that new keys are being added correctly."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 512)
            key_len: int = random.randint(1, 10)
            key_count: int = random.randint(1, min(255, size))
            dct: ByteDictionary = ByteDictionary(size, key_len)

            expected: list[tuple[bytes, int]] = []

            for j in range(key_count):
                key: bytes = bytes([j]) + bytes(
                    random.choices(range(255), k=key_len - 1))
                dct.put(key, j)
                expected.append((key, j))

            for key, value in expected:
                self.assertIn(key, dct.keys,
                    "Key was not inserted.")
                index: int = dct.keys.index(key)
                self.assertEqual(value, dct.values[index],
                    "Wrong value was assigned to a key.")

    def test_byte_put_overwrite(self) -> None:
        """Tests that a value of an existing key can be overwritten."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 512)
            key_len: int = random.randint(1, 10)
            key_count: int = random.randint(1, min(255, size))
            dct: ByteDictionary = ByteDictionary(size, key_len)

            expected: list[tuple[bytes, int]] = []

            for j in range(key_count):
                key: bytes = bytes([j]) + bytes(
                    random.choices(range(255), k=key_len - 1))
                dct.put(key, j)
                expected.append((key, j))

            # Overwrite values by their negative equivalent
            for ind, item in enumerate(dct.keys):
                if item is None:
                    continue
                value: int = dct.values[ind] * -1
                dct.put(item, value)

            for key, value in expected:
                self.assertIn(key, dct.keys,
                    "Overwriting a value removed a key.")
                index: int = dct.keys.index(key)
                self.assertEqual(value * -1, dct.values[index],
                    "Value was overwritten incorrectly.")

    def test_byte_get(self) -> None:
        """Tests a retrival of a value from an existing key."""
        # Run 10000 times
        for i in range(10000):
            size: int = random.randint(5, 512)
            key_len: int = random.randint(1, 10)
            key_count: int = random.randint(1, size)
            dct: ByteDictionary = ByteDictionary(size, key_len)

            target_key: bytes = b""
            target_value: int = 0
            target_ind: int = random.randint(0, key_count - 1)
            for j in range(key_count):
                key: bytes = bytes(random.choices(range(255), k=key_len))
                # Set a target value and update it in case of a duplicate key
                if j == target_ind or key == target_key:
                    target_key = key
                    target_value = j
                dct.put(key, j)

            self.assertEqual(target_value, dct.get(target_key),
                "Wrong value got retrieved.")

    def test_byte_get_none(self) -> None:
        """Tests a retrival of a value from an absent key."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 512)
            key_len: int = random.randint(1, 10)
            key_count: int = random.randint(1, size)
            dct: ByteDictionary = ByteDictionary(size, key_len)

            for j in range(key_count):
                key: bytes = bytes(random.choices(range(254), k=key_len))
                dct.put(key, j)

            target_key: bytes = bytes(255)  # Value not present in dict keys

            self.assertIsNone(dct.get(target_key),
                "A value was retrieved from an absent key.")


if __name__ == '__main__':
    unittest.main()



