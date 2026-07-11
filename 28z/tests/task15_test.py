"""Tests for task 15."""

import unittest
import random
import task15


class Task15Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        self.assertTrue(task15.TankRush(3, 4, "1234 2345 0987",
                                        2, 2, "34 98"),
                        "Solution is incorrect.")

    def test_null(self) -> None:
        """Tests solution on the smallest map."""
        self.assertTrue(task15.TankRush(1, 1, "0",
                                        1, 1, "0"),
                        "Couldn't determine a sub-map of a smallest map.")
        self.assertFalse(task15.TankRush(1, 1, "0",
                                         1, 1, "1"),
                         "Couldn't determine that a sub-map isn't in a map.")

    def test_big_map(self) -> None:
        """Tests solution on a map of big size."""
        height: int = 100
        width: int = 100
        map_str: str = (("0" * width + " ") * (height // 2)
                        + ("1" + "0" * (width - 1) + " ")
                        + ("0" * width + " ") * (height // 2 - 2)
                        + ("0" * width))
        self.assertTrue(task15.TankRush(height, width, map_str,
                                        height, width, map_str),
                        "Solution failed on a big map.")
        not_map: str = (("0" * width + " ") * (height - 1) + ("0" * width))
        self.assertFalse(task15.TankRush(height, width, map_str,
                                         height, width, not_map),
                         "Solution failed on a big map.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 10000 runs
        for i in range(10000):
            # Create a matrix of chars
            height: int = random.randint(1, 50)
            width: int = random.randint(1, 50)
            map_list: list[list[str]] = []
            for j in range(height):
                map_row: list[str] = []
                for k in range(width):
                    map_row.append(str(random.randint(0, 9)))
                map_list.append(map_row)
            # Transform the matrix into a single string
            map_str: str = ""
            for row in map_list:
                map_str += "".join(row) + " "
            map_str = map_str.rstrip()

            # Get a submatrix from the main one
            sub_height: int = random.randint(1, height)
            sub_width: int = random.randint(1, width)
            submap_list: list[list[str]] = []
            entry_y: int = random.randint(0, height - sub_height)
            entry_x: int = random.randint(0, width - sub_width)
            for j in range(entry_y, entry_y + sub_height):
                submap_row: list[str] = []
                for k in range(entry_x, entry_x + sub_width):
                    submap_row.append(map_list[j][k])
                submap_list.append(submap_row)
            # Transform the submatrix into a single string
            submap_str: str = ""
            for row in submap_list:
                submap_str += "".join(row) + " "
            submap_str = submap_str.rstrip()

            # Redact the submap to make it not match the map
            expected: bool = True
            if random.randint(0, 1) == 0:
                expected = False
                ind: int = random.randint(0, len(submap_str) - 1)
                while submap_str[ind] == " ":
                    ind = random.randint(0, len(submap_str) - 1)
                sub_list: list[str] = list(submap_str)
                sub_list[ind] = "*"
                submap_str = "".join(sub_list)

            self.assertEqual(expected,
                             task15.TankRush(height, width, map_str,
                                             sub_height, sub_width, submap_str),
                             f"Solution failed on random data. Run №{i}")


if __name__ == '__main__':
    unittest.main()



