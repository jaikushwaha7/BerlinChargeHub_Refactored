import unittest

import folium
import pandas as pd
from src.visualization_helper.mapping import mapping_residents


class TestMappingResidents(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame for testing
        self.df_population = pd.DataFrame({
            'PLZ': ['10115', '10243', '10365'],
            'Einwohner': [10000, 20000, 15000],
            'geometry': [
                {'type': 'Polygon',
                 'coordinates': [[[13.0, 52.5], [13.1, 52.5], [13.1, 52.6], [13.0, 52.6], [13.0, 52.5]]]},
                {'type': 'Polygon',
                 'coordinates': [[[13.2, 52.5], [13.3, 52.5], [13.3, 52.6], [13.2, 52.6], [13.2, 52.5]]]},
                {'type': 'Polygon',
                 'coordinates': [[[13.4, 52.5], [13.5, 52.5], [13.5, 52.6], [13.4, 52.6], [13.4, 52.5]]]}
            ]
        })
        self.folium_map = folium.Map(location=[52.5, 13.4], zoom_start=10)

    def test_mapping_residents_returns_correct_types(self):
        color_map, updated_map = mapping_residents(self.df_population, self.folium_map)
        self.assertIsInstance(color_map, object)  # LinearColormap instance
        self.assertIsInstance(updated_map, folium.Map)

    def test_mapping_residents_applies_color_gradient(self):
        color_map, _ = mapping_residents(self.df_population, self.folium_map)
        population_values = self.df_population['Einwohner']
        expected_colors = [
            color_map(population) for population in population_values
        ]
        for idx, row in self.df_population.iterrows():
            self.assertEqual(
                color_map(row['Einwohner']),
                expected_colors[idx]
            )

    def test_mapping_residents_handles_empty_dataframe(self):
        empty_df = pd.DataFrame(columns=['PLZ', 'Einwohner', 'geometry'])
        color_map, updated_map = mapping_residents(empty_df, self.folium_map)
        self.assertIsInstance(color_map, object)  # LinearColormap instance
        self.assertIsInstance(updated_map, folium.Map)


if __name__ == '__main__':
    unittest.main()
