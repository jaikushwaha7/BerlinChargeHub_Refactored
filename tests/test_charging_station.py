import unittest
from src.search_management.model.charging_station import ChargingStation
from src.search_management.value_objects.latitude import Latitude
from src.search_management.value_objects.longitude import Longitude
from src.search_management.value_objects.postal_code import InvalidPostalCodeException
from src.search_management.value_objects.postal_code import PostalCode

class TestChargingStation(unittest.TestCase):

    def test_valid_charging_station(self):
        postal_code = PostalCode("12345")
        latitude = Latitude(52.5200)
        longitude = Longitude(13.4050)
        station = ChargingStation(postal_code, latitude, longitude)
        self.assertEqual(station.postal_code.value, "12345")
        self.assertAlmostEqual(station.latitude.value, 52.5200)
        self.assertAlmostEqual(station.longitude.value, 13.4050)

    def test_invalid_postal_code(self):
        with self.assertRaises(InvalidPostalCodeException):
            ChargingStation("1234", Latitude(52.5200), Longitude(13.4050))

    def test_latitude_conversion(self):
        postal_code = PostalCode("12345")
        latitude = 52.5200
        longitude = Longitude(13.4050)
        station = ChargingStation(postal_code, latitude, longitude)
        self.assertIsInstance(station.latitude, Latitude)
        self.assertAlmostEqual(station.latitude.value, 52.5200)

    def test_longitude_conversion(self):
        postal_code = PostalCode("12345")
        latitude = Latitude(52.5200)
        longitude = 13.4050
        station = ChargingStation(postal_code, latitude, longitude)
        self.assertIsInstance(station.longitude, Longitude)
        self.assertAlmostEqual(station.longitude.value, 13.4050)
