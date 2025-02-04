import pandas as pd
import pytest
from src.search_management.application.charging_station_search import SearchService
from src.search_management.events.station_search_performed import StationSearchPerformed
from src.search_management.model.charging_station import ChargingStation

class TestSearchService:

    def setup_method(self):
        self.search_service = SearchService()
        self.sample_df = pd.DataFrame({
            "PLZ": [10115, 10117, 10119],
            "Breitengrad": ["52.532", "52.520", "52.515"],
            "Längengrad": ["13.388", "13.400", "13.428"],
            "Number": [5, 3, 2]
        })

    def test_valid_postal_code(self):
        stations, search_summary = self.search_service.search_by_postal_code(self.sample_df, "10115")
        assert len(stations) == 1
        assert isinstance(stations[0], ChargingStation)
        assert stations[0].postal_code.value == "10115"
        assert isinstance(search_summary, StationSearchPerformed)
        assert search_summary.postal_code == "10115"
        assert search_summary.stations_found == 5

    def test_invalid_postal_code_non_numeric(self):
        with pytest.raises(ValueError):
            stations, search_summary = self.search_service.search_by_postal_code(self.sample_df, "abcde")

    def test_invalid_postal_code_empty(self):
        with pytest.raises(ValueError):
            stations, search_summary = self.search_service.search_by_postal_code(self.sample_df, None)

    def test_no_stations_found(self):
        stations, search_summary = self.search_service.search_by_postal_code(self.sample_df, "99999")
        assert stations == []
        assert search_summary.stations_found == 0
