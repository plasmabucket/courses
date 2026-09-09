"""Tests for task 11."""

import unittest
import random
import string
from task11 import BloomFilter
from task11_2 import bf_merge, BloomDelete, val_extract, unhash


class Task11MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Test for the hash function
    def test_hash_fun(self) -> None:
        """Tests validity of values returned by the hash function."""
        # Run 1000 times
        for i in range(1000):
            size: int = random.randint(5, 100)
            bloom: BloomFilter = BloomFilter(size)
            bf_bit_array: int = bloom.bit_array
            # Integer that is used for customization of hash functions
            random_int: int = random.randint(2, 300)

            for j in range(100):
                value_len: int = random.randint(0, 100)
                value: str = "".join(
                    random.choices(string.ascii_letters, k=value_len))
                bloom_mask: int = bloom.hash_fun(value, random_int)
                bloom_hash: int = bloom_mask.bit_length() - 1

                self.assertEqual(1, bloom_mask.bit_count(),
                    "Mask doesn't contain exactly one '1' bit.")
                self.assertGreaterEqual(bloom_hash, 0,
                    "Hash must be a non-negative number.")
                self.assertLess(bloom_hash, size,
                    "Hash must be less than a bit array size.")
            self.assertEqual(size, bloom.filter_len,
                "Hash calculation affected filter length.")
            self.assertEqual(bf_bit_array, bloom.bit_array,
                "Hash calculation affected bit array contents.")

    # Tests for the insertion of values
    def test_add_regression(self) -> None:
        """Tests value insertion on a known case."""
        size: int = 32
        bloom: BloomFilter = BloomFilter(size)
        str1: str = "0123456789"

        for i in range(10):
            bloom.add(str1)
            str1 = str1[1:] + str1[0]  # Cycle characters in a string

        self.assertEqual(size, bloom.filter_len,
            "Element addition affected filter length.")
        for i in range(10):
            self.assertTrue(bloom.is_value(str1),
                f"Value '{str1}' could not be retrieved.")
            str1 = str1[1:] + str1[0]
        self.assertEqual(0b00101000000000000010000000100000,
                         bloom.bit_array,
            "Resulting bit array is incorrect.")

    def test_add(self) -> None:
        """Tests value insertion on random data."""
        # Run 1000 times
        for i in range(1000):
            size: int = 32
            bloom: BloomFilter = BloomFilter(size)

            inserted: list[str] = []
            for j in range(10):
                rand_str: str = "".join(
                    random.choices(string.ascii_letters, k=10))
                bloom.add(rand_str)
                inserted.append(rand_str)

            for val in inserted:
                self.assertTrue(bloom.is_value(val),
                    f"Value '{val}' could not be retrieved.")
            self.assertEqual(size, bloom.filter_len,
                "Element addition affected filter length.")

    # Test for the element presence check
    def test_is_value(self) -> None:
        """Tests value presence check on random data."""
        false_hits: int = 0
        # Run 1000 times
        run_count: int = 1000
        random_insert_count: int = 10
        for i in range(run_count):
            size: int = 32
            bloom: BloomFilter = BloomFilter(size)

            inserted: list[str] = []
            for j in range(10):
                rand_str: str = "".join(
                    random.choices(string.ascii_letters, k=10))
                bloom.add(rand_str)
                inserted.append(rand_str)
            bf_bit_array: int = bloom.bit_array

            # All inserted values should be reported as present
            for val in inserted:
                self.assertTrue(bloom.is_value(val),
                    f"Value '{val}' could not be retrieved.")

            # Not-inserted values shouldn't have a false positive rate
            # higher than ~31%
            for j in range(random_insert_count):
                rand_str = "".join(
                    random.choices(string.ascii_letters, k=10))
                if rand_str in inserted:
                    continue
                if bloom.is_value(rand_str):
                    false_hits += 1
            self.assertEqual(size, bloom.filter_len,
                "Element presence check affected filter length.")
            self.assertEqual(bf_bit_array, bloom.bit_array,
                "Presence check affected bit array contents.")
        self.assertLess(false_hits / (run_count * random_insert_count), 0.5,
            "False positive rate is too high. (>50%)")


class Task11ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Test for the bloom filter merging (ex 2.*)
    def test_merge(self) -> None:
        """Tests filter merging on random data."""
        false_hits: int = 0
        # Run 1000 times
        run_count: int = 1000
        random_insert_count: int = 10
        for i in range(run_count):
            size: int = 32
            bloom1: BloomFilter = BloomFilter(size)
            bloom2: BloomFilter = BloomFilter(size)

            inserted: list[str] = []
            for j in range(10):
                rand_str: str = "".join(
                    random.choices(string.ascii_letters, k=10))
                bloom1.add(rand_str)
                inserted.append(rand_str)
            for j in range(10):
                rand_str = "".join(
                    random.choices(string.ascii_letters, k=10))
                bloom2.add(rand_str)
                inserted.append(rand_str)
            bf1_bit_array: int = bloom1.bit_array
            bf2_bit_array: int = bloom2.bit_array

            bloom3: BloomFilter = bf_merge(bloom1, bloom2)

            self.assertEqual(size, bloom3.filter_len,
                "Filter merging resulted in a filter of incorrect length.")
            self.assertEqual(size, bloom1.filter_len,
                "Filter merging affected filter length (1).")
            self.assertEqual(size, bloom2.filter_len,
                "Filter merging affected filter length (2).")
            self.assertEqual(bf1_bit_array, bloom1.bit_array,
                "Filter merging affected bit array contents (1).")
            self.assertEqual(bf2_bit_array, bloom2.bit_array,
                "Filter merging affected bit array contents (2).")

            # All inserted values should be reported as present
            for val in inserted:
                self.assertTrue(bloom3.is_value(val),
                    f"Value '{val}' could not be retrieved.")

            # Not-inserted values shouldn't have a false positive rate
            # higher than ~56%
            for j in range(random_insert_count):
                rand_str = "".join(
                    random.choices(string.ascii_letters, k=10))
                if rand_str in inserted:
                    continue
                if bloom3.is_value(rand_str):
                    false_hits += 1

        self.assertLess(false_hits / (run_count * random_insert_count), 0.7,
            "False positive rate is too high. (>70%)")

    # Tests for value removal (ex 3.*)
    def test_delete(self) -> None:
        """Tests value removal on random data."""
        # Run 1000 times
        for i in range(1000):
            size: int = 32
            bloom: BloomDelete = BloomDelete(size)

            inserted: list[str] = []
            for j in range(10):
                rand_str: str = "".join(
                    random.choices(string.ascii_letters, k=10))
                bloom.add(rand_str)
                inserted.append(rand_str)
            bf_bit_count: int = bloom.bit_array.bit_count()

            rm_target: str = random.choice(inserted)

            self.assertTrue(bloom.delete(rm_target),
                "Inserted value couldn't be removed.")
            self.assertFalse(bloom.is_value(rm_target),
                "Value was not removed.")
            self.assertEqual(size, bloom.filter_len,
                "Deletion affected filter length.")
            self.assertEqual(bf_bit_count - 1, bloom.bit_array.bit_count(),
                "Deletion changed more than 1 bit.")

    def test_delete_false(self) -> None:
        """Tests removal of non-present value."""
        size: int = 32
        bloom: BloomDelete = BloomDelete(size)
        str1: str = "0123456789"

        for i in range(10):
            bloom.add(str1)
            str1 = str1[1:] + str1[0]  # Cycle characters in a string
        bf_bit_array: int = bloom.bit_array

        self.assertFalse(bloom.delete("Not present"),
            "Value that was not present got deleted.")

        self.assertEqual(size, bloom.filter_len,
            "No-op deletion affected filter length.")
        self.assertEqual(bf_bit_array, bloom.bit_array,
            "No-op deletion affected bit array contents.")

        for i in range(10):
            self.assertTrue(bloom.is_value(str1),
                f"Value '{str1}' could not be retrieved after no-op removal.")
            str1 = str1[1:] + str1[0]

    # Tests for value extraction (ex 4.*)
    def test_extract(self) -> None:
        """Tests value extraction on random data."""
        # Run 1000 times
        for i in range(1000):
            size: int = 32
            bloom: BloomFilter = BloomFilter(size)
            for j in range(10):
                rand_str: str = "".join(
                    random.choices(string.ascii_letters, k=10))
                bloom.add(rand_str)
            bf_bit_array: int = bloom.bit_array

            extracted: list[str] = val_extract(bloom)
            bloom_ex: BloomFilter = BloomFilter(size)
            for val in extracted:
                bloom_ex.add(val)

            self.assertEqual(size, bloom.filter_len,
                "Value extraction affected filter length.")
            self.assertEqual(bf_bit_array, bloom.bit_array,
                "Value extraction affected bit array contents.")

            for val in extracted:
                self.assertTrue(bloom.is_value(val),
                    "Extracted value is not in the set.")
            self.assertEqual(bloom.bit_array, bloom_ex.bit_array,
                "Only a subset of values got extracted.")

    def test_unhash(self) -> None:
        """Tests hash-reversal function on random data."""
        size: int = 32
        bloom: BloomFilter = BloomFilter(size)
        bf_bit_array: int = bloom.bit_array
        # Run 10000 times
        for i in range(10000):
            rand_str: str = "".join(
                random.choices(string.ascii_letters, k=10))
            h1: int = bloom.hash1(rand_str).bit_length() - 1
            h2: int = bloom.hash2(rand_str).bit_length() - 1

            unhashed_str: str | None = unhash(size, h1, h2)
            self.assertIsNotNone(unhashed_str,
                "Valid hash pair couldn't be reversed.")

            # Hashing resulting string should return original hashes
            uh1: int = bloom.hash1(unhashed_str).bit_length() - 1
            uh2: int = bloom.hash2(unhashed_str).bit_length() - 1
            self.assertEqual([h1, h2], [uh1, uh2],
                "Hash reversal is incorrect.")

            self.assertEqual(size, bloom.filter_len,
                "Hash reversal affected filter length.")
            self.assertEqual(bf_bit_array, bloom.bit_array,
                "Hash reversal affected bit array contents.")


if __name__ == '__main__':
    unittest.main()



