from src.demand_management.model.demand_score import DemandScore
from src.demand_management.value_objects.score import Score
from src.search_management.value_objects.postal_code import PostalCode
from unittest import TestCase


class TestDemandScore(TestCase):
    def test_demand_score_is_number(self):
        # Create a DemandScore instance with valid data
        demand_score_instance = DemandScore(
            demand_score=Score(50),  # Use Score class for demand_score
            postal_code=PostalCode("12345")  # Use PostalCode class for postal_code
        )

        # Test that demand_score is a number (int or float)
        self.assertIsInstance(demand_score_instance.demand_score.value, (int, float), "demand_score must be a number")

    def test_demand_score_not_infinite(self):
        # Create a DemandScore instance with valid data
        demand_score_instance = DemandScore(
            demand_score=Score(50),  # Use Score class for demand_score
            postal_code=PostalCode("12345")  # Use PostalCode class for postal_code
        )

        # Test that demand_score is not infinite
        self.assertNotEqual(demand_score_instance.demand_score.value, float('inf'),
                            "demand_score must not be positive infinity")
        self.assertNotEqual(demand_score_instance.demand_score.value, float('-inf'),
                            "demand_score must not be negative infinity")