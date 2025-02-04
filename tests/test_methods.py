import unittest

import geopandas as gpd
import pandas as pd
import pytest
from src.pages.infrastructure.core.methods import sort_by_plz_add_geometry
from shapely.geometry import Point

class TestSortByPlzAddGeometry(unittest.TestCase):

    def test_invalid_geocode_key(self):
        dfr = pd.DataFrame({
            "PLZ": [12345],
            "value": [10]
        })
        dfg = gpd.GeoDataFrame({
            "geocode": [12345],
            "geometry": [Point(1, 2)]
        }, geometry="geometry")  # Explicitly set geometry column
        pdict = {"geocode": "invalid_key"}

        with pytest.raises(KeyError):
            sort_by_plz_add_geometry(dfr, dfg, pdict)
