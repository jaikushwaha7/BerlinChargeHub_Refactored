import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.rating_management.application.charging_station_rate import ChargeStationRating


class TestChargeStationRating(unittest.TestCase):

    @patch("src.rating_management.application.charging_station_rate.st")
    @patch("src.rating_management.application.charging_station_rate.sqlite3")
    def test_save_rating(self, mock_sqlite3, mock_st):
        # Setup
        mock_st.session_state = MagicMock()  # Use MagicMock for session state
        mock_st.session_state.username = "test_user"  # Set the username attribute
        mock_conn = MagicMock()
        mock_sqlite3.connect.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        # Execution
        rating_instance = ChargeStationRating()
        rating_instance.save_rating("Station_A", 5)

        # Assertions
        mock_sqlite3.connect.assert_called_once_with("heatmap_app.db")
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO ratings (station_id, username, rating, timestamp) VALUES (?, ?, ?, ?)",
            ("Station_A", "test_user", 5, unittest.mock.ANY)  # Use unittest.mock.ANY for timestamp
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()
        mock_st.success.assert_called_once_with("Rating submitted for station: Station_A")

    @patch("src.rating_management.application.charging_station_rate.st")
    @patch("src.rating_management.application.charging_station_rate.sqlite3")
    def test_display_average_rating_with_existing_ratings(self, mock_sqlite3, mock_st):
        # Setup
        mock_conn = MagicMock()
        mock_sqlite3.connect.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [4.2]  # Example average rating from the database

        # Execution
        rating_instance = ChargeStationRating()
        avg_rating = rating_instance.display_average_rating("Station_A")

        # Assertions
        mock_sqlite3.connect.assert_called_once_with("heatmap_app.db")
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "SELECT AVG(rating) FROM ratings WHERE station_id = ?",
            ("Station_A",)
        )
        mock_conn.close.assert_called_once()
        mock_st.info.assert_called_once_with("Average rating for station Station_A: 4.20")
        self.assertEqual(avg_rating, 4.2)

    @patch("src.rating_management.application.charging_station_rate.st")
    @patch("src.rating_management.application.charging_station_rate.sqlite3")
    def test_display_average_rating_no_ratings(self, mock_sqlite3, mock_st):
        # Setup
        mock_conn = MagicMock()
        mock_sqlite3.connect.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [None]  # Simulate no ratings in the database

        # Execution
        rating_instance = ChargeStationRating()
        avg_rating = rating_instance.display_average_rating("Station_A")

        # Assertions
        mock_sqlite3.connect.assert_called_once_with("heatmap_app.db")
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "SELECT AVG(rating) FROM ratings WHERE station_id = ?",
            ("Station_A",)
        )
        mock_conn.close.assert_called_once()
        mock_st.info.assert_called_once_with("No ratings yet for station: Station_A")
        self.assertIsNone(avg_rating)


if __name__ == "__main__":
    unittest.main()

