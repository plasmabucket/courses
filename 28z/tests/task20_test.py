"""Tests for task 20."""

import unittest
import task20


class Task20Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_scenario(self) -> None:
        """Tests solution on a scenario of a real use case."""
        task20.BastShoe("2 1000")
        task20.BastShoe("2 1000")
        task20.BastShoe("4")
        task20.BastShoe("2 1000")

        self.assertEqual("Hello~",          task20.BastShoe("1 Hello~"),"Failure. Step №1")
        self.assertEqual("Hello~, You!",    task20.BastShoe("1 , You!"),"Failure. Step №2")
        self.assertEqual("Hello~, You!++",  task20.BastShoe("1 ++"),    "Failure. Step №3")
        self.assertEqual("Hello~, You!",    task20.BastShoe("2 2"),     "Failure. Step №4")
        self.assertEqual("Hello~, You!++",  task20.BastShoe("4"),       "Failure. Step №5")
        self.assertEqual("Hello~, You!",    task20.BastShoe("4"),       "Failure. Step №6")
        self.assertEqual("Hello~, You!*",   task20.BastShoe("1 *"),     "Failure. Step №7")
        self.assertEqual("Hello~, You!",    task20.BastShoe("4"),       "Failure. Step №8")
        self.assertEqual("Hello~, You!",    task20.BastShoe("4"),       "Failure. Step №9")
        self.assertEqual("Hello~, You!",    task20.BastShoe("4"),       "Failure. Step №10")
        self.assertEqual(",",               task20.BastShoe("3 6"),     "Failure. Step №11")
        self.assertEqual("",                task20.BastShoe("2 100"),   "Failure. Step №12")
        self.assertEqual("Hello~",          task20.BastShoe("1 Hello~"),"Failure. Step №13")
        self.assertEqual("Hello~, You!",    task20.BastShoe("1 , You!"),"Failure. Step №14")
        self.assertEqual("Hello~, You!++",  task20.BastShoe("1 ++"),    "Failure. Step №15")
        self.assertEqual("Hello~, You!",    task20.BastShoe("4"),       "Failure. Step №16")
        self.assertEqual("Hello~",          task20.BastShoe("4"),       "Failure. Step №17")
        self.assertEqual("Hello~, You!",    task20.BastShoe("5"),       "Failure. Step №18")
        self.assertEqual("Hello~",          task20.BastShoe("4"),       "Failure. Step №19")
        self.assertEqual("Hello~, You!",    task20.BastShoe("5"),       "Failure. Step №20")
        self.assertEqual("Hello~, You!++",  task20.BastShoe("5"),       "Failure. Step №21")
        self.assertEqual("Hello~, You!++",  task20.BastShoe("5"),       "Failure. Step №22")
        self.assertEqual("Hello~, You!++",  task20.BastShoe("5"),       "Failure. Step №23")
        self.assertEqual("Hello~, You!",    task20.BastShoe("4"),       "Failure. Step №24")
        self.assertEqual("Hello~",          task20.BastShoe("4"),       "Failure. Step №25")
        self.assertEqual("Hell",            task20.BastShoe("2 2"),     "Failure. Step №26")
        self.assertEqual("Hello~",          task20.BastShoe("4"),       "Failure. Step №27")
        self.assertEqual("Hell",            task20.BastShoe("5"),       "Failure. Step №28")
        self.assertEqual("Hell",            task20.BastShoe("5"),       "Failure. Step №29")
        self.assertEqual("Hell",            task20.BastShoe("5"),       "Failure. Step №30")

    def test_history_reset(self) -> None:
        """Tests if history resets when modifying the string after undo."""
        task20.BastShoe("2 1000")
        task20.BastShoe("2 1000")
        task20.BastShoe("4")
        task20.BastShoe("2 1000")

        self.assertEqual("str1",            task20.BastShoe("1 str1"),  "Failure. Step №1")
        self.assertEqual("str1 str2",       task20.BastShoe("1  str2"), "Failure. Step №2")
        self.assertEqual("str1",            task20.BastShoe("4"),       "Failure. Step №3")
        self.assertEqual("str1 str3",       task20.BastShoe("1  str3"), "Failure. Step №4")
        self.assertEqual("str1 str3 str4",  task20.BastShoe("1  str4"), "Failure. Step №5")
        self.assertEqual("str1 str3",       task20.BastShoe("4"),       "Failure. Step №6")
        self.assertEqual("str1",            task20.BastShoe("4"),       "Failure. Step №7")

    def test_incorrect_command(self) -> None:
        """Tests how the incorrect command is handled."""
        task20.BastShoe("2 1000")
        task20.BastShoe("2 1000")
        task20.BastShoe("4")
        task20.BastShoe("2 1000")

        task20.BastShoe("1 str1")
        self.assertEqual("str1", task20.BastShoe("6"), "Incorrect commands are unhandled.")
        self.assertEqual("str1", task20.BastShoe("12"), "Double-digit commands are unhandled.")


if __name__ == '__main__':
    unittest.main()



