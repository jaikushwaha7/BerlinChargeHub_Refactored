import unittest
from src.utils.database_utils import hash_password
from unittest.mock import patch


class TestHashPassword(unittest.TestCase):

    def test_hash_password_returns_string(self):
        # Arrange
        test_password = "password123"
        # Act
        result = hash_password(test_password)
        # Assert
        self.assertIsInstance(result, str)

    def test_hash_password_consistency(self):
        # Arrange
        test_password = "password123"
        # Act
        hash1 = hash_password(test_password)
        hash2 = hash_password(test_password)
        # Assert
        self.assertEqual(hash1, hash2)

    def test_hash_password_differing_inputs(self):
        # Arrange
        password1 = "password123"
        password2 = "differentPassword123"
        # Act
        hash1 = hash_password(password1)
        hash2 = hash_password(password2)
        # Assert
        self.assertNotEqual(hash1, hash2)

if __name__ == "__main__":
    unittest.main()
