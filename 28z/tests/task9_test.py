"""Tests for task 9."""

import unittest
import random
import math
import task9


class Task9Tests(unittest.TestCase):
    """Class for unit tests."""

    def test_regression(self) -> None:
        """Tests solution correctness on a known case."""
        string: str = "отдай мою кроличью лапку"
        encrypted: str = "омоюу толл дюиа акчп йрьк"
        decrypted: str = "отдаймоюкроличьюлапку"
        self.assertEqual(encrypted, task9.TheRabbitsFoot(string, True),
                         "Encryption algorithm is incorrect.")
        self.assertEqual(decrypted, task9.TheRabbitsFoot(encrypted, False),
                         "Decryption algorithm is incorrect.")

    def test_null(self) -> None:
        """Tests solution on strings of size 0 and 1."""
        # Empty string
        self.assertEqual("", task9.TheRabbitsFoot("", True),
                         "Encryption of a string of size 0 is unhandled.")
        self.assertEqual("", task9.TheRabbitsFoot("", False),
                         "Decryption of a string of size 0 is unhandled.")
        # One-character long string
        self.assertEqual("1", task9.TheRabbitsFoot("1", True),
                         "Encryption of a string of size 1 is unhandled.")
        self.assertEqual("1", task9.TheRabbitsFoot("1", False),
                         "Decryption of a string of size 1 is unhandled.")

    def test_random(self) -> None:
        """Tests solution on random data."""
        # Make 1000 runs
        for i in range(10000):
            length: int = random.randint(1, 1000)  # Length of a string
            string: str = ""
            for j in range(length):
                string += (str(random.randint(0, 9)))
            # Determine matrix dimensions
            m_dim: int = math.floor(math.sqrt(length))
            n_dim: int = math.ceil(math.sqrt(length))
            if m_dim * n_dim < length:
                m_dim += 1
            # Create a matrix of characters
            string_fit: str = string
            if length < m_dim * n_dim:
                string_fit += "!" * (m_dim * n_dim - length)
            matrix: list[str] = []
            for j in range(m_dim):
                matrix.append(string_fit[j * n_dim : (j+1) * n_dim])
            # Create encrypted string
            encrypted_string: str = ""
            for j in range(n_dim):
                for k in range(m_dim):
                    encrypted_string += matrix[k][j]
                encrypted_string += " "
            encrypted_string = encrypted_string.replace("!", "").rstrip()
            self.assertEqual(encrypted_string, task9.TheRabbitsFoot(string, True),
                             f"Encryption failed on random data. Run №{i}")
            self.assertEqual(string, task9.TheRabbitsFoot(encrypted_string, False),
                             f"Decryption failed on random data. Run №{i}")


if __name__ == '__main__':
    unittest.main()



