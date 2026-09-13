"""Tests for task 12."""

import unittest
import random
import string
from typing import Any
from task12 import NativeCache


class Task12MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Test for the hash function
    def test_hash(self) -> None:
        """Tests validity of hashes on random data."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            cache: NativeCache = NativeCache(size)

            # Save the state of the cache
            orig_slots: list[str | None] = cache.slots.copy()
            orig_values: list[Any] = cache.values.copy()
            orig_hits: list[int] = cache.hits.copy()

            for j in range(100):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                cache_hash: int = cache._hash_fun(key)

                self.assertGreaterEqual(cache_hash, 0,
                    "Hash must be a non-negative number.")
                self.assertLess(cache_hash, size,
                    "Hash must be less than a table size.")

            # Make sure hashing didn't affect the state of the cache
            self.assertEqual(size, cache.size,
                "Hash calculations affected table size.")
            self.assertEqual(orig_slots, cache.slots,
                "Hash calculations affected list of keys.")
            self.assertEqual(orig_values, cache.values,
                "Hash calculations affected list of values.")
            self.assertEqual(orig_hits, cache.hits,
                "Hash calculations affected lisf of hits.")

    # Tests for the slot search
    def test_seek_key(self) -> None:
        """Tests slot search when an existing key is requested."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            cache: NativeCache = NativeCache(size)

            # Put some values in a table
            keys: list[str] = []
            for j in range(random.randint(1, size)):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                cache.put(key, j)
                keys.append(key)

            # Save the state of the cache
            orig_slots: list[str | None] = cache.slots.copy()
            orig_values: list[Any] = cache.values.copy()
            orig_hits: list[int] = cache.hits.copy()

            # Test that the found index is a correct one
            # Perform a query for each key in a table
            for k in keys:
                index: int = cache._seek_slot(k)
                self.assertEqual(k, cache.slots[index],
                    "Wrong slot index was found for an existing key.")

            # Make sure the slot search didn't affect the state of the cache
            self.assertEqual(size, cache.size,
                "Key search affected table size.")
            self.assertEqual(orig_slots, cache.slots,
                "Key search affected list of keys.")
            self.assertEqual(orig_values, cache.values,
                "Key search affected list of values.")
            self.assertEqual(orig_hits, cache.hits,
                "Key search affected lisf of hits.")

    def test_seek_empty(self) -> None:
        """Tests slot search for a new key."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            cache: NativeCache = NativeCache(size)

            # Put some values in a table
            # -1 for size because table should not be full
            for j in range(random.randint(0, size - 1)):
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                cache.put(key, j)

            # Save the state of the cache
            orig_slots: list[str | None] = cache.slots.copy()
            orig_values: list[Any] = cache.values.copy()
            orig_hits: list[int] = cache.hits.copy()

            # Test that the found index is a correct one
            for j in range(100):
                key_len = random.randint(0, 100)
                key = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                if key in cache.slots:  # Only query new keys
                    continue
                index: int = cache._seek_slot(key)
                self.assertIsNone(cache.slots[index],
                    "Wrong slot index was found for a new key.")

            # Make sure the slot search didn't affect the state of the cache
            self.assertEqual(size, cache.size,
                "Empty slot search affected table size.")
            self.assertEqual(orig_slots, cache.slots,
                "Empty slot search affected list of keys.")
            self.assertEqual(orig_values, cache.values,
                "Empty slot search affected list of values.")
            self.assertEqual(orig_hits, cache.hits,
                "Empty slot search affected lisf of hits.")

    def test_seek_none(self) -> None:
        """Tests slot search for a new key in a full table."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            cache: NativeCache = NativeCache(size)

            # Fill the table with values
            key_set: set[str] = set()
            while len(key_set) < size:
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                key_set.add(key)
            for k in key_set:
                cache.put(k, random.randint(0, size))

            # Save the state of the cache
            orig_slots: list[str | None] = cache.slots.copy()
            orig_values: list[Any] = cache.values.copy()
            orig_hits: list[int] = cache.hits.copy()

            # Test that the found index is a correct one
            for j in range(100):
                key_len = random.randint(0, 100)
                key = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                if key in key_set:
                    continue
                self.assertEqual(-1, cache._seek_slot(key),
                    "Index for a new key in a full table isn't '-1'.")

            # Make sure the slot search didn't affect the state of the cache
            self.assertEqual(size, cache.size,
                "Unsuccessful slot search affected table size.")
            self.assertEqual(orig_slots, cache.slots,
                "Unsuccessful slot search affected list of keys.")
            self.assertEqual(orig_values, cache.values,
                "Unsuccessful slot search affected list of values.")
            self.assertEqual(orig_hits, cache.hits,
                "Unsuccessful slot search affected lisf of hits.")

    # Test for the key dropping
    def test_drop(self) -> None:
        """Tests key dropping on random data."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            cache: NativeCache = NativeCache(size)

            # Fill the table with values
            key_set: set[str] = set()
            while len(key_set) < size:
                key_len: int = random.randint(0, 100)
                key: str = "".join(
                    random.choices(string.ascii_letters, k=key_len))
                key_set.add(key)
            for k in key_set:
                cache.put(k, random.randint(0, 1000))
            cache.hits = random.choices(range(0, 1000), k=size)

            # Save the state of the cache
            orig_slots: list[str | None] = cache.slots.copy()
            orig_values: list[Any] = cache.values.copy()
            orig_hits: list[int] = cache.hits.copy()

            # Test that the correct key was dropped
            expected: int = cache.hits.index(min(cache.hits))
            index: int = cache._drop_least_used()
            self.assertEqual(expected, index,
                "Wrong key was dropped.")
            self.assertIsNone(cache.slots[index],
                "Key was not dropped from the list.")
            self.assertIsNone(cache.slots[index],
                "Value of a dropped key was not dropped from the list.")
            self.assertEqual(0, cache.hits[index],
                "Number of hits of a dropped key was not reset to zero.")

            # Make sure the key drop affected only one element
            orig_slots[expected] = None
            orig_values[expected] = None
            orig_hits[expected] = 0
            self.assertEqual(size, cache.size,
                "Key drop affected table size.")
            self.assertEqual(orig_slots, cache.slots,
                "Key drop affected list of keys.")
            self.assertEqual(orig_values, cache.values,
                "Key drop affected list of values.")
            self.assertEqual(orig_hits, cache.hits,
                "Key drop affected lisf of hits.")

    # Tests for key insertion
    def test_put(self) -> None:
        """Tests key insertion without key drops."""
        size: int = 10
        cache: NativeCache = NativeCache(size)

        # Get a list of keys.
        # Key hashes form an ordered sequence which starts at zero
        key_list: list[str] = []
        init_ind: int = ord("a") + size - ord("a") % size
        for i in range(size):
            key_list.append(chr(init_ind + i))

        expected_slots: list[str] = key_list
        expected_values: list[int] = list(range(0, size))
        expected_hits: list[int] = [1] * size

        # Fill the table with keys
        for i in range(size):
            cache.put(key_list[i], i)

        self.assertEqual(expected_slots, cache.slots,
            "Key insertion is incorrect.")
        self.assertEqual(expected_values, cache.values,
            "Values are incorrectly inserted during key insertion.")
        self.assertEqual(expected_hits, cache.hits,
            "Key insertion is not counted as a hit.")

        # Make sure the insertion didn't affect the size of the cache
        self.assertEqual(size, cache.size,
            "Key insertion affected table size.")

    def test_put_overwrite(self) -> None:
        """Tests key insertion of an already present key."""
        size: int = 10
        cache: NativeCache = NativeCache(size)

        cache.put("key", 10)
        expected_index: int = cache.slots.index("key")

        # Save the state of the cache
        orig_slots: list[str | None] = cache.slots.copy()
        orig_values: list[Any] = cache.values.copy()
        orig_hits: list[int] = cache.hits.copy()

        # Insert the key again, now with a different value
        cache.put("key", 20)

        # Make sure key overwrite affected only one element
        orig_values[expected_index] = 20
        orig_hits[expected_index] = 2
        self.assertEqual(size, cache.size,
        "Key overwrite affected table size.")
        self.assertEqual(orig_slots, cache.slots,
        "Key overwrite affected list of keys.")
        self.assertEqual(orig_values, cache.values,
        "Value overwrite is incorrect.")
        self.assertEqual(orig_hits, cache.hits,
        "Overwriting doesn't count as a hit.")

    def test_put_drop(self) -> None:
        """Tests key insertion with a key drop."""
        size: int = 10
        cache: NativeCache = NativeCache(size)

        # Fill the table with values
        key_set: set[str] = set()
        while len(key_set) < size:
            key_len: int = random.randint(0, 100)
            key: str = "".join(
                random.choices(string.ascii_letters, k=key_len))
            key_set.add(key)
        for k in key_set:
            cache.put(k, random.randint(0, size))
        # Adjust hit count of keys
        cache.hits = random.choices(range(1, 100), k=size)
        expected_index: int = cache.hits.index(min(cache.hits))

        # Save the state of the cache
        orig_slots: list[str | None] = cache.slots.copy()
        orig_values: list[Any] = cache.values.copy()
        orig_hits: list[int] = cache.hits.copy()

        # Insert a new key and drop an old one
        cache.put("new key", size + 1)

        # Make sure key replacement affected only one element
        orig_slots[expected_index] = "new key"
        orig_values[expected_index] = size + 1
        orig_hits[expected_index] = 1
        self.assertEqual(size, cache.size,
            "Insertion with a key drop affected table size.")
        self.assertEqual(orig_slots, cache.slots,
            "Insertion with a key drop affected list of keys.")
        self.assertEqual(orig_values, cache.values,
            "Insertion with a key drop affected list of values.")
        self.assertEqual(orig_hits, cache.hits,
            "Insertion with a key drop affected lisf of hits.")

    # Tests for value retrieval
    def test_get(self) -> None:
        """Tests value retrieval of an existing key."""
        size: int = 10
        cache: NativeCache = NativeCache(size)

        cache.put("key", 10)
        expected_index: int = cache.slots.index("key")

        # Save the state of the cache
        orig_slots: list[str | None] = cache.slots.copy()
        orig_values: list[Any] = cache.values.copy()
        orig_hits: list[int] = cache.hits.copy()

        # Retrieve a value of a key 10 times
        hit_count: int = 10
        for i in range(hit_count):
            self.assertEqual(10, cache.get("key"),
                "Retrieved value is incorrect.")

        # Make sure key retrieval affected only the hit count of one element
        orig_hits[expected_index] += hit_count
        self.assertEqual(size, cache.size,
            "Value retrieval affected table size.")
        self.assertEqual(orig_slots, cache.slots,
            "Value retrieval affected list of keys.")
        self.assertEqual(orig_values, cache.values,
            "Value retrieval affected list of values.")
        self.assertEqual(orig_hits, cache.hits,
            "Value retrieval affected lisf of hits.")

    def test_get_none(self) -> None:
        """Tests value retrieval of a nonexistent key."""
        size: int = 10
        cache: NativeCache = NativeCache(size)

        cache.put("key", 10)

        # Save the state of the cache
        orig_slots: list[str | None] = cache.slots.copy()
        orig_values: list[Any] = cache.values.copy()
        orig_hits: list[int] = cache.hits.copy()

        # Retrieve a value of a key 10 times
        hit_count: int = 10
        for i in range(hit_count):
            self.assertIsNone(cache.get("wrong key"),
                "Retrieved value is incorrect.")

        # Make sure key retrieval didn't affect the cache state
        self.assertEqual(size, cache.size,
            "Value retrieval of a non-present key affected table size.")
        self.assertEqual(orig_slots, cache.slots,
            "Value retrieval of a non-present key affected list of keys.")
        self.assertEqual(orig_values, cache.values,
            "Value retrieval of a non-present key affected list of values.")
        self.assertEqual(orig_hits, cache.hits,
            "Value retrieval of a non-present key affected lisf of hits.")


if __name__ == '__main__':
    unittest.main()



