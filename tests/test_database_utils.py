# import unittest
# from src.utils.database_utils import hash_password
# from unittest.mock import patch
#
#
# class TestHashPassword(unittest.TestCase):
#
#     def test_hash_password_returns_string(self):
#         # Arrange
#         test_password = "password123"
#         # Act
#         result = hash_password(test_password)
#         # Assert
#         self.assertIsInstance(result, str)
#
#     def test_hash_password_consistency(self):
#         # Arrange
#         test_password = "password123"
#         # Act
#         hash1 = hash_password(test_password)
#         hash2 = hash_password(test_password)
#         # Assert
#         self.assertEqual(hash1, hash2)
#
#     def test_hash_password_differing_inputs(self):
#         # Arrange
#         password1 = "password123"
#         password2 = "differentPassword123"
#         # Act
#         hash1 = hash_password(password1)
#         hash2 = hash_password(password2)
#         # Assert
#         self.assertNotEqual(hash1, hash2)
#
#     @patch("src.utils.database_utils.hashlib.sha256")
#     def test_hash_password_uses_sha256(self, mock_sha256):
#         # Arrange
#         test_password = "password123"
#         mock_sha256.return_value.hexdigest.return_value = "mocked_hash"
#         # Act
#         result = hash_password(test_password)
#         # Assert
#         mock_sha256.assert_called()
#         self.assertEqual(result, "mocked_hash")
#
#     @patch("src.utils.database_utils.hashlib.sha256")
#     def test_hash_password_salt_applied(self, mock_sha256):
#         # Arrange
#         test_password = "password123"
#         mock_sha256.return_value.hexdigest.return_value = "mocked_hash"
#         # Act
#         hash_password(test_password)
#         # Assert
#         mock_sha256.assert_called_once_with()
#         call_args = mock_sha256.return_value.update.call_args[0][0]
#         self.assertIn(b"streamlit-heatmap-salt", call_args)
#         self.assertIn(test_password.encode(), call_args)
#
#
# if __name__ == "__main__":
#     unittest.main()
