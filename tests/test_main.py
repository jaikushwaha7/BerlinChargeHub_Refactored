import logging
from unittest import TestCase
from unittest.mock import patch, MagicMock
import pandas as pd
from main import main


class TestMain(TestCase):
    @patch('main.pd.read_csv')
    @patch('main.m2.create_electric_charging_residents_heatmap')
    @patch('main.m1.preprop_resid')
    @patch('main.m1.count_plz_occurrences')
    @patch('main.m1.preprop_lstat')
    @patch('logging.info')
    @patch('logging.error')
    def test_main_success(self, mock_error, mock_info, mock_preprop_lstat, mock_count_plz_occurrences,
                          mock_preprop_resid, mock_streamlit_function, mock_read_csv):
        # Mock with required columns for preprocessing
        mock_read_csv.side_effect = [
            pd.DataFrame({'Postleitzahl': ['12345', '23456']}),
            pd.DataFrame({
                'Postleitzahl': ['12345', '23456'],
                'Bundesland': ['Berlin', 'Berlin'],
                'Breitengrad': [52.52, 52.53],
                'Längengrad': [13.40, 13.41],
                'Nennleistung Ladeeinrichtung [kW]': [50, 75]
            }),
            pd.DataFrame({'Postleitzahl': ['12345', '23456'], 'Einwohner': [5000, 10000]})
        ]

        mock_preprop_lstat.return_value = MagicMock()
        mock_count_plz_occurrences.return_value = MagicMock()
        mock_preprop_resid.return_value = MagicMock()

        main()

        mock_info.assert_any_call("geodata_berlin_plz.csv loaded successfully.")
        mock_info.assert_any_call("Ladesaeulenregister.csv loaded successfully.")
        mock_info.assert_any_call("plz_einwohner.csv loaded successfully.")
        mock_error.assert_not_called()
        mock_streamlit_function.assert_called_once()

    @patch('main.pd.read_csv')
    @patch('logging.error')
    def test_main_lstat_load_error(self, mock_logging_error, mock_read_csv):
        mock_read_csv.side_effect = [
            pd.DataFrame({'PLZ': [12345, 23456]}),  # Changed to PLZ
            Exception("File not found")
        ]

        with self.assertRaises(Exception):
            main()

        mock_logging_error.assert_any_call("Failed to load Ladesaeulenregister.csv: File not found")

    @patch('main.pd.read_csv')
    @patch('logging.error')
    def test_main_geodata_load_error(self, mock_logging_error, mock_read_csv):
        mock_read_csv.side_effect = [Exception("File not found")]

        with self.assertRaises(Exception):
            main()

        mock_logging_error.assert_any_call("Failed to load geodata_berlin_plz.csv: File not found")