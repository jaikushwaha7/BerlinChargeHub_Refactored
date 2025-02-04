import unittest
from unittest.mock import patch, MagicMock

from src.pages.infrastructure.core.UI import create_electric_charging_residents_heatmap


class TestCreateElectricChargingResidentsHeatmap(unittest.TestCase):

    @patch('src.utils.database_utils.verify_user')
    @patch('src.pages.infrastructure.core.UI.st')
    @patch('src.pages.infrastructure.core.UI.merge_geo_dataframes')
    def test_heatmap_user_not_logged_in(self, mock_merge_geo_dataframes, mock_st, mock_verify_user):
        # Mock session state
        mock_st.session_state = MagicMock()
        mock_st.session_state.logged_in = False
        mock_st.session_state.username = None

        # Mock stop behavior
        mock_st.stop = MagicMock(side_effect=RuntimeError("Stop called"))

        # Mock inputs
        mock_st.text_input.side_effect = ["test_user", "test_pass"]
        mock_st.form_submit_button.return_value = True
        mock_verify_user.return_value = False
        mock_merge_geo_dataframes.return_value = MagicMock()

        df_charging_stations = MagicMock()
        df_population = MagicMock()
        df_lstat2 = MagicMock()

        with self.assertRaises(RuntimeError):
            create_electric_charging_residents_heatmap(df_charging_stations, df_population, df_lstat2)

    @patch('src.utils.database_utils.verify_user')
    @patch('src.pages.infrastructure.core.UI.st')
    @patch('src.pages.infrastructure.core.UI.folium')
    @patch('src.pages.infrastructure.core.UI.merge_geo_dataframes')
    @patch('src.pages.infrastructure.core.UI.folium_static')
    def test_heatmap_logged_in_renders_map(self, mock_folium_static, mock_merge_geo_dataframes,
                                             mock_folium, mock_st, mock_verify_user):
        # Mock authentication
        mock_verify_user.return_value = True
        mock_st.session_state = MagicMock()
        mock_st.session_state.logged_in = True
        mock_st.session_state.username = 'test_user'
        # Set return_value for text_input to avoid side_effect exhaustion
        mock_st.text_input.return_value = "12345"  # Valid postal code

        # Mock map components
        mock_merge_geo_dataframes.return_value = MagicMock()
        mock_st.sidebar.radio.return_value = "Residents"
        mock_folium.Map.return_value = MagicMock()

        df_charging_stations = MagicMock()
        df_population = MagicMock()
        df_lstat2 = MagicMock()

        create_electric_charging_residents_heatmap(df_charging_stations, df_population, df_lstat2)

        mock_folium.Map.assert_called_once()
        mock_folium_static.assert_called_once()

if __name__ == '__main__':
    unittest.main()