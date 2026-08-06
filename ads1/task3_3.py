"""Tests for task 3."""

import unittest
from task3 import DynArray
from task3_2 import DynBanking, MultiDimArray


def equal(array1: DynArray | DynBanking,
          array2: DynArray | DynBanking) -> bool:
    """Helper function for comparing arrays."""
    length: int = len(array1)
    if length != len(array2):
        return False
    for i in range(length):
        if array1[i] != array2[i]:
            return False
    return True


class Task3MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    # Tests for insertion (ex 1) from exercise 4
    def test_insert_no_resize(self) -> None:
        """Tests insertion without array reallocation."""
        array: DynArray = DynArray()
        for i in range(8):
            array.append(i)
        array.insert(6, -1)

        expected: DynArray = DynArray()
        for i in range(8):
            expected.append(i)
            if i == 5:
                expected.append(-1)

        self.assertEqual(16, array.capacity,
            "Insertion resized an array when it's not needed.")
        self.assertTrue(equal(expected, array),
            "Insertion without resize is incorrect.")

    def test_insert_resize(self) -> None:
        """Tests insertion with reallocation."""
        array: DynArray = DynArray()
        for i in range(16):
            array.append(i)
        array.insert(6, -1)

        expected: DynArray = DynArray()
        for i in range(16):
            expected.append(i)
            if i == 5:
                expected.append(-1)

        self.assertEqual(32, array.capacity,
            "Insertion didn't resize an array correctly.")
        self.assertTrue(equal(expected, array),
            "Insertion with resize is incorrect.")

    def test_insert_invalid_index(self) -> None:
        """Tests insertion with an invalid index."""
        array: DynArray = DynArray()
        for i in range(8):
            array.append(i)

        # Check for exceptions on invalid indexes
        self.assertRaises(IndexError, array.insert, 9, -1)
        self.assertRaises(IndexError, array.insert, -1, -1)

    # Additional tests for insertion
    def test_insert_null(self) -> None:
        """Tests insertion on an empty array."""
        array: DynArray = DynArray()

        # Check for exception on an invalid index
        self.assertRaises(IndexError, array.insert, 1, -1)

        array.insert(0, -1)
        expected: DynArray = DynArray()
        expected.append(-1)

        self.assertEqual(16, array.capacity,
            "Insertion resized an empty array when it's not needed.")
        self.assertTrue(equal(expected, array),
            "Insertion in an empty array is incorrect.")

    def test_insert_large(self) -> None:
        """Tests insertion on a large array."""
        array: DynArray = DynArray()
        for i in range(1000):
            array.append(i)
        array.insert(600, -1)

        expected: DynArray = DynArray()
        for i in range(1000):
            expected.append(i)
            if i == 599:
                expected.append(-1)

        self.assertEqual(1024, array.capacity,
            "Insertion resized a large array when it's not needed.")
        self.assertTrue(equal(expected, array),
            "Insertion in a large array is incorrect.")

    def test_insert_large_resize(self) -> None:
        """Tests insertion with reallocation on a large array."""
        array: DynArray = DynArray()
        for i in range(1024):
            array.append(i)
        array.insert(600, -1)

        expected: DynArray = DynArray()
        for i in range(1024):
            expected.append(i)
            if i == 599:
                expected.append(-1)

        self.assertEqual(2048, array.capacity,
            "Insertion didn't resize a large array.")
        self.assertTrue(equal(expected, array),
            "Insertion in a large array with resize is incorrect.")

    # Tests for deletion (ex 2) from exercise 4
    def test_delete_no_resize(self) -> None:
        """Tests deletion without reallocation."""
        array: DynArray = DynArray()
        for i in range(8):
            array.append(i)
        array.delete(6)

        expected: DynArray = DynArray()
        for i in range(8):
            if i == 6:
                continue
            expected.append(i)

        self.assertEqual(16, array.capacity,
            "Deletion resized an array when it's not needed.")
        self.assertTrue(equal(expected, array),
            "Deletion without resize is incorrect.")

    def test_delete_resize(self) -> None:
        """Tests deletion with reallocation."""
        array: DynArray = DynArray()
        for i in range(17):
            array.append(i)
        array.delete(6)
        array.delete(6)

        expected: DynArray = DynArray()
        for i in range(17):
            if i == 6 or i == 7:
                continue
            expected.append(i)

        self.assertEqual(21, array.capacity,
            "Deletion didn't resize an array correctly.")
        self.assertTrue(equal(expected, array),
            "Deletion with resize is incorrect.")

    def test_delete_invalid_index(self) -> None:
        """Tests deletion with an invalid index."""
        array: DynArray = DynArray()
        for i in range(8):
            array.append(i)

        # Check for exceptions on invalid indexes
        self.assertRaises(IndexError, array.delete, 9)
        self.assertRaises(IndexError, array.delete, -1)

    # Additional tests for deletion
    def test_delete_null(self) -> None:
        """Tests deletion on an empty array."""
        array: DynArray = DynArray()

        # Check for exception on an invalid index
        self.assertRaises(IndexError, array.delete, 0)

    def test_delete_large(self) -> None:
        """Tests deletion on a large array."""
        array: DynArray = DynArray()
        for i in range(1000):
            array.append(i)
        array.delete(600)

        expected: DynArray = DynArray()
        for i in range(1000):
            if i == 600:
                continue
            expected.append(i)

        self.assertEqual(1024, array.capacity,
            "Deletion resized a large array when it's not needed.")
        self.assertTrue(equal(expected, array),
            "Deletion in a large array is incorrect.")

    def test_delete_large_resize(self) -> None:
        """Tests deletion with reallocation on a large array."""
        array: DynArray = DynArray()
        for i in range(1025):
            array.append(i)
        array.delete(600)
        array.delete(600)

        expected: DynArray = DynArray()
        for i in range(1025):
            if i == 600 or i == 601:
                continue
            expected.append(i)

        self.assertEqual(1365, array.capacity,
            "Deletion didn't resize a large array.")
        self.assertTrue(equal(expected, array),
            "Deletion in a large array with resize is incorrect.")


class Task3ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Tests for the dynamic array based on banking method (ex 5.*)
    def test_banking_append_no_resize(self) -> None:
        """Tests appending without reallocation."""
        array: DynBanking = DynBanking()
        for i in range(8):
            array.append(i)

        expected: DynArray = DynArray()
        for i in range(8):
            expected.append(i)

        self.assertEqual(16, array.capacity,
            "Appending resized an array when it's not needed.")
        self.assertTrue(equal(expected, array),
            "Appending without resize is incorrect.")

    def test_banking_append_resize(self) -> None:
        """Tests appending with reallocation."""
        array: DynBanking = DynBanking()
        for i in range(17):
            array.append(i)

        expected: DynArray = DynArray()
        for i in range(17):
            expected.append(i)

        self.assertEqual(32, array.capacity,
            "Appending didn't resize an array correctly.")
        self.assertTrue(equal(expected, array),
            "Appending with resize is incorrect.")

    def test_banking_append_large(self) -> None:
        """Tests appending on a large array."""
        array: DynBanking = DynBanking()
        for i in range(1025):
            array.append(i)

        expected: DynArray = DynArray()
        for i in range(1025):
            expected.append(i)

        self.assertEqual(2048, array.capacity,
            "Appending didn't resize a large array correctly.")
        self.assertTrue(equal(expected, array),
            "Appending to a large array is incorrect.")

    # Tests for the multidimensional array (ex 6.*)
    def test_multidim_init(self) -> None:
        """Simple test for thr initialization of the array."""
        dim_sizes: tuple[int, ...] = (3, 2, 1)
        array: MultiDimArray = MultiDimArray(len(dim_sizes), dim_sizes)

        self.assertEqual(3, len(array), "Dim 1 length is incorrect.")
        self.assertEqual(2, len(array[0]), "Dim 2 length is incorrect.")
        self.assertEqual(1, len(array[0][0]), "Dim 3 length is incorrect.")

        for n in range(6):
            i: int = n // (dim_sizes[1] * dim_sizes[2])
            j: int = (n % (dim_sizes[1] * dim_sizes[2])) // dim_sizes[2]
            k: int = n % dim_sizes[2]
            array[i][j][k] = n

        collector: list[int] = []
        for n in range(6):
            i = n // (dim_sizes[1] * dim_sizes[2])
            j = (n % (dim_sizes[1] * dim_sizes[2])) // dim_sizes[2]
            k = n % dim_sizes[2]
            collector.append(array[i][j][k])

        self.assertEqual([0, 1, 2, 3, 4, 5], collector,
            "Initialization of the array is incorrect.")

    def test_multidim_resize(self) -> None:
        """Simple test for the resizing of dimensions."""
        dim_sizes: tuple[int, ...] = (3, 2, 1)
        array: MultiDimArray = MultiDimArray(len(dim_sizes), dim_sizes)

        for n in range(6):
            i: int = n // (dim_sizes[1] * dim_sizes[2])
            j: int = (n % (dim_sizes[1] * dim_sizes[2])) // dim_sizes[2]
            k: int = n % dim_sizes[2]
            array[i][j][k] = n

        # Set dimension sizes to: (2, 3, 5)
        array.dimension_size(1, 2)
        array.dimension_size(2, 3)
        array.dimension_size(3, 5)

        dim_sizes = (2, 3, 5)
        for n in range(30):
            i = n // (dim_sizes[1] * dim_sizes[2])
            j = (n % (dim_sizes[1] * dim_sizes[2])) // dim_sizes[2]
            k = n % dim_sizes[2]
            if array[i][j][k] is None:
                array[i][j][k] = -n

        collector: list[int] = []
        for n in range(30):
            i = n // (dim_sizes[1] * dim_sizes[2])
            j = (n % (dim_sizes[1] * dim_sizes[2])) // dim_sizes[2]
            k = n % dim_sizes[2]
            collector.append(array[i][j][k])

        expected: list[int] = [  0,  -1,  -2,  -3, -4,
                                 1,  -6,  -7,  -8, -9,
                               -10, -11, -12, -13, -14,

                                 2, -16, -17, -18, -19,
                                 3, -21, -22, -23, -24,
                               -25, -26, -27, -28, -29]

        self.assertEqual(expected, collector,
            "Resizing of dimensions is incorrect.")


if __name__ == '__main__':
    unittest.main()



