import unittest

from src.demand_management.value_objects.postal_code_population import PostalCodePopulation


class TestPostalCodePopulation(unittest.TestCase):

    def test_population_initialization(self):
        """Test that PostalCodePopulation initializes with the correct value."""
        population = PostalCodePopulation(5000)
        self.assertEqual(population.value(), 5000)

    def test_population_zero(self):
        """Test initialization with zero value."""
        population = PostalCodePopulation(0)
        self.assertEqual(population.value(), 0)

    def test_population_large_value(self):
        """Test initialization with a very large value."""
        population = PostalCodePopulation(10 ** 9)
        self.assertEqual(population.value(), 10 ** 9)


if __name__ == "__main__":
    unittest.main()
