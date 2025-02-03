import unittest
from src.rating_management.model.rating import Rating
from src.rating_management.value_objects.address import Address
from src.rating_management.value_objects.stars import Stars
from src.rating_management.value_objects.user import User
from src.search_management.value_objects.postal_code import PostalCode


class TestRating(unittest.TestCase):
    def test_valid_rating(self):
        user = User(user_id="12345")
        address = Address(address="123 Main St")
        stars = Stars(stars=5)
        postal_code = PostalCode(value="12345")
        rating = Rating(user_id=user, station_address=address, stars=stars, station_postal_code=postal_code)
        self.assertEqual(rating.user_id.user_id, "12345")
        self.assertEqual(rating.station_address.address, "123 Main St")
        self.assertEqual(rating.stars.stars, 5)
        self.assertEqual(rating.station_postal_code.value, "12345")

    def test_invalid_postal_code(self):
        user = User(user_id="98765")
        address = Address(address="456 Side Rd")
        stars = Stars(stars=3)
        with self.assertRaises(Exception):  # Expecting an InvalidPostalCodeException
            postal_code = PostalCode(value="1234")
            Rating(user_id=user, station_address=address, stars=stars, station_postal_code=postal_code)
