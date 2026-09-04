"""Tests for task 10."""

import unittest
import random
import time
from typing import Any
from task10 import PowerSet
from task10_2 import PowerSetExtra, multi_intersect, Bag


class Task10MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Tests for element insertion
    def test_put(self) -> None:
        """Tests insertion of a new element."""
        my_set: PowerSet = PowerSet()
        elements: list[Any] = [123, "123", [1, 2, 3], 1.23]
        for value in elements:
            my_set.put(value)

        for value in elements:
            self.assertTrue(my_set.get(value),
                f"Element of {str(type(value))[8:-2]} type was not inserted.")

    def test_put_duplicate(self) -> None:
        """Tests insertion of an already present element."""
        my_set: PowerSet = PowerSet()
        elements: list[Any] = [123, "123", [1, 2, 3], 1.23]
        for value in elements:
            my_set.put(value)
        for value in elements:
            my_set.put(value)

        for value in elements:
            self.assertEqual(1, my_set.list.count(value),
            f"Element of {str(type(value))[8:-2]} type was inserted twice.")

    # Tests for element deletion
    def test_remove(self) -> None:
        """Tests removal of elements present in the set."""
        my_set: PowerSet = PowerSet()
        elements: list[Any] = [123, "123", [1, 2, 3], 1.23]
        for value in elements:
            my_set.put(value)

        for value in elements:
            self.assertTrue(my_set.remove(value),
                "Error during removal of an existing element.")
        for value in elements:
            self.assertFalse(my_set.get(value),
                "Element didn't get removed.")

    def test_remove_none(self) -> None:
        """Tests removal of elements not present in the set."""
        my_set: PowerSet = PowerSet()
        elements: list[Any] = [123, "123", [1, 2, 3], 1.23]

        for value in elements:
            self.assertFalse(my_set.remove(value),
                "Element not present in the set got removed.")

    # Tests for set intersection
    def test_intersect(self) -> None:
        """Tests set intersection on random data."""
        # Run 10000 times
        for i in range(10000):
            my_set: PowerSet = PowerSet()
            my_set2: PowerSet = PowerSet()

            elements: list[int] = random.choices(range(100), k=40)
            elements2: list[int] = random.choices(range(50, 150), k=40)
            for value in elements:
                my_set.put(value)
            for value in elements2:
                my_set2.put(value)
            result: PowerSet = my_set.intersection(my_set2)

            expected: set[int] = set(elements) & set(elements2)

            self.assertEqual(expected, set(result.list),
                "Set intersection is incorrect.")

    def test_intersect_empty(self) -> None:
        """Tests set intersection on non-intersecting sets."""
        my_set: PowerSet = PowerSet()
        my_set2: PowerSet = PowerSet()

        # Two empty sets
        result: PowerSet = my_set.intersection(my_set2)
        self.assertEqual([], result.list,
            "Intersection of two empty sets is not empty.")

        # Empty and non-empty set
        my_set.put(1)
        result = my_set.intersection(my_set2)
        self.assertEqual([], result.list,
            "Intersection with an empty set is not empty.")

        # Empty and non-empty set -- reversed
        result = my_set2.intersection(my_set)
        self.assertEqual([], result.list,
            "Intersection of an empty set is not empty.")

        # Non-intersecting sets
        my_set2.put(2)
        result = my_set.intersection(my_set2)
        self.assertEqual([], result.list,
            "Intersection of non-intersecting sets is not empty.")

    # Tests for set unification
    def test_union(self) -> None:
        """Tests set unification on random data."""
        # Run 10000 times
        for i in range(10000):
            my_set: PowerSet = PowerSet()
            my_set2: PowerSet = PowerSet()

            elements: list[int] = random.choices(range(100), k=40)
            elements2: list[int] = random.choices(range(50, 150), k=40)
            for value in elements:
                my_set.put(value)
            for value in elements2:
                my_set2.put(value)
            result: PowerSet = my_set.union(my_set2)

            expected: set[int] = set(elements) | set(elements2)

            self.assertEqual(expected, set(result.list),
                "Set unification is incorrect.")

    def test_union_empty(self) -> None:
        """Tests set unification on emtpy sets."""
        my_set: PowerSet = PowerSet()
        my_set2: PowerSet = PowerSet()

        # Two empty sets
        result: PowerSet = my_set.union(my_set2)
        self.assertEqual([], result.list,
            "Union of two empty sets is not empty.")

        # Empty and non-empty set
        my_set.put(1)
        result = my_set.union(my_set2)
        self.assertEqual(my_set.list, result.list,
            "Union of a set with an empty set is not the same set.")

        # Empty and non-empty set -- reversed
        result = my_set2.union(my_set)
        self.assertEqual(my_set.list, result.list,
            "Union of an empty set with a set is not a copy of a set.")

    # Tests for set difference
    def test_difference(self) -> None:
        """Tests set difference on random data."""
        # Run 10000 times
        for i in range(10000):
            my_set: PowerSet = PowerSet()
            my_set2: PowerSet = PowerSet()

            elements: list[int] = random.choices(range(100), k=40)
            elements2: list[int] = random.choices(range(50, 150), k=40)
            for value in elements:
                my_set.put(value)
            for value in elements2:
                my_set2.put(value)
            result: PowerSet = my_set.difference(my_set2)

            expected: set[int] = set(elements) - set(elements2)

            self.assertEqual(expected, set(result.list),
                "Set difference is incorrect.")

    def test_difference_empty(self) -> None:
        """Tests set difference on empty sets."""
        my_set: PowerSet = PowerSet()
        my_set2: PowerSet = PowerSet()

        # Two empty sets
        result: PowerSet = my_set.difference(my_set2)
        self.assertEqual([], result.list,
            "Difference of two empty sets is not empty.")

        # Empty and non-empty set
        my_set.put(1)
        result = my_set.difference(my_set2)
        self.assertEqual(my_set.list, result.list,
            "Difference of a set with an empty set is not the same set.")

        # Empty and non-empty set -- reversed
        result = my_set2.difference(my_set)
        self.assertEqual([], result.list,
            "Difference of an empty set with a set is not empty.")

        # Set and its superset
        my_set2.put(1)
        result = my_set.difference(my_set2)
        self.assertEqual([], result.list,
            "Difference of a set with a superset is not empty.")

    # Tests for subset check
    def test_subset(self) -> None:
        """Tests subset check on random data."""
        # Run 10000 times
        for i in range(10000):
            my_set: PowerSet = PowerSet()
            my_set2: PowerSet = PowerSet()

            elements: list[int] = random.choices(range(100), k=80)
            elements2: list[int] = random.choices(range(100), k=5)
            for value in elements:
                my_set.put(value)
            for value in elements2:
                my_set2.put(value)
            result: bool = my_set.issubset(my_set2)

            expected: bool = set(elements2).issubset(set(elements))

            self.assertEqual(expected, result,
                "Subset check is incorrect.")

    def test_subset_true(self) -> None:
        """Tests subset check on valid subsets."""
        my_set: PowerSet = PowerSet()
        my_set2: PowerSet = PowerSet()

        # Two empty sets
        self.assertTrue(my_set.issubset(my_set2),
            "Empty set is flagged as not a subset of an empty set.")

        # A non-empty and an empty sets
        my_set.put(1)
        self.assertTrue(my_set.issubset(my_set2),
            "Empty set is flagged as not a subset of a set.")

        # A set and an equal set
        my_set2.put(1)
        self.assertTrue(my_set.issubset(my_set2),
            "An equal set is flagged as not a subset.")

        # A set and its proper subset
        my_set.put(2)
        self.assertTrue(my_set.issubset(my_set2),
            "A proper subset is flagged as not a subset.")

    def test_subset_false(self) -> None:
        """Tests subset check on non-subsets."""
        my_set: PowerSet = PowerSet()
        my_set2: PowerSet = PowerSet()

        # An empty set and a non-empty set
        my_set2.put(2)
        self.assertFalse(my_set.issubset(my_set2),
            "A set is flagged as a subset of an empty set.")

        # A set and a non-intersecting set
        my_set.put(1)
        self.assertFalse(my_set.issubset(my_set2),
            "A non-intersecting set is flagged as a subset.")

        # A set and an intersecting non-subset
        my_set.put(2)
        my_set2.put(3)
        self.assertFalse(my_set.issubset(my_set2),
            "A non-subset is flagged as a subset.")

        # A set and its superset
        my_set2.put(1)
        self.assertFalse(my_set.issubset(my_set2),
            "A proper superset is flagged as a subset.")

    # Test for equality check
    def test_equals(self) -> None:
        """Tests equality check on random data."""
        # Run 10000 times
        for i in range(10000):
            my_set: PowerSet = PowerSet()
            my_set2: PowerSet = PowerSet()

            elements: list[int] = random.choices(range(10),
                                                 k=random.randint(0, 5))
            elements2: list[int] = random.choices(range(10),
                                                  k=random.randint(0, 5))
            for value in elements:
                my_set.put(value)
            for value in elements2:
                my_set2.put(value)
            result: bool = my_set.equals(my_set2)

            expected: bool = set(elements) == set(elements2)

            self.assertEqual(expected, result,
                "Equality check is incorrect.")

    # Test for performance of the class methods
    def test_performance(self) -> None:
        """Tests time to perform operations on large sets."""
        # Two sets with 20k elements
        my_set: PowerSet = PowerSet()
        my_set2: PowerSet = PowerSet()
        for i in range(20000):
            my_set.put(i)
            my_set2.put(i)

        start_time: float = time.time()

        my_set.put(-1)
        my_set.remove(-1)
        my_set.intersection(my_set2)
        my_set.union(my_set2)
        my_set.difference(my_set2)
        my_set.issubset(my_set2)
        my_set.equals(my_set2)

        elapsed_time: float = time.time() - start_time

        # Execution time should be less than 10 seconds.
        self.assertLess(elapsed_time, 10,
            "Operations on large sets take too long.")


class Task10ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Tests for the cartesian product of sets (ex 4.*)
    def test_product(self) -> None:
        """Tests cartesian product method on random data."""
        # Run 10000 times
        for i in range(10000):
            my_set: PowerSetExtra = PowerSetExtra()
            my_set2: PowerSet = PowerSet()

            elements: list[int] = random.choices(range(100), k=40)
            elements2: list[int] = random.choices(range(50, 150), k=40)
            for value in elements:
                my_set.put(value)
            for value in elements2:
                my_set2.put(value)
            result: PowerSetExtra = my_set.product(my_set2)

            expected: set[tuple[int, int]] = set()
            for value in set(elements):
                for value2 in set(elements2):
                    expected.add((value, value2))

            self.assertEqual(expected, set(result.list),
                "Cartesian product of sets is incorrect.")

    def test_product_empty(self) -> None:
        """Tests cartesian product on empty sets."""
        my_set: PowerSetExtra = PowerSetExtra()
        my_set2: PowerSetExtra = PowerSetExtra()

        # Two empty sets
        result: PowerSetExtra = my_set.product(my_set2)
        self.assertEqual([], result.list,
            "Product of two empty sets is not empty.")

        # Empty and non-empty set
        my_set.put(1)
        result = my_set.product(my_set2)
        self.assertEqual([], result.list,
            "Product of a set with an empty set is not empty.")

        # Empty and non-empty set -- reversed
        result = my_set2.product(my_set)
        self.assertEqual([], result.list,
            "Product of an empty set with a set is not empty.")

    # Test for the intersection of multiple sets (ex 5.*)
    def test_multi_intersect(self) -> None:
        """Tests multi-intersection of sets on random data."""
        # Run 10000 times
        for i in range(10000):
            sets: list[PowerSet] = []
            set_count: int = random.randint(0, 50)
            for j in range(set_count):
                my_set: PowerSet = PowerSet()
                for value in random.choices(range(100), k=90):
                    my_set.put(value)
                sets.append(my_set)

            result: PowerSet = multi_intersect(sets)

            expected: set[int] = set()
            if set_count > 0:
                expected = set(sets[0].list)
            for pow_set in sets:
                expected = expected & set(pow_set.list)

            self.assertEqual(expected, set(result.list),
                "Multi-intersect of sets is incorrect.")

    # Tests for the multi-set (bag) (ex 6.*)
    def test_bag_put(self) -> None:
        """Tests insertion of a new element into multi-set on random data."""
        # Run 10000 times
        for i in range(10000):
            bag: Bag = Bag()

            elements: list[int] = random.choices(range(100), k=80)
            for value in elements:
                bag.put(value)

            for value in set(elements):
                self.assertIn(value, bag.dict,
                    "Value was not inserted.")
                self.assertEqual(elements.count(value), bag.dict.get(value),
                    "Number of inserted duplicates is incorrect.")

    def test_bag_remove(self) -> None:
        """Tests removal of elements from the multi-set on random data."""
        # Run 10000 times
        for i in range(10000):
            bag: Bag = Bag()
            elements: list[int] = random.choices(range(100), k=40)
            for value in elements:
                bag.put(value)

            elements2: list[int] = random.choices(range(100), k=80)
            for value in elements2:
                self.assertEqual(value in bag.dict, bag.remove(value),
                    "Error during removal of a value.")

            for value in set(elements):
                leftover: int = (
                    max(0, elements.count(value) - elements2.count(value)))
                if leftover == 0:
                    self.assertNotIn(value, bag.dict,
                        "Value was not removed.")
                    continue
                self.assertEqual(leftover, bag.dict.get(value),
                    "Number of leftover duplicates is incorrect.")

    def test_bag_get_all(self) -> None:
        """Tests retrieval of a list of elements from a multi-set."""
        # Run 10000 times
        for i in range(10000):
            bag: Bag = Bag()

            elements: list[int] = random.choices(range(100), k=80)
            for value in elements:
                bag.put(value)

            result: list[tuple[int, int]] = bag.get_all()

            self.assertEqual(len(set(elements)), len(result),
                "Incorrect number of values retrieved.")
            for value in set(elements):
                self.assertIn((value, elements.count(value)), result,
                    "A value-count pair was retrieved incorrectly.")

    def test_bag_get_all_empty(self) -> None:
        """Tests retrieval of a list of elements from an empty multi-set."""
        bag: Bag = Bag()

        result: list[tuple[Any, int]] = bag.get_all()

        self.assertEqual([], result,
            "A list of all elements from an empty multi-set is not empty.")


if __name__ == '__main__':
    unittest.main()



