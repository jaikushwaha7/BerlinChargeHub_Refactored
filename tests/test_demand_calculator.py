from src.demand_management.application.demand_calculator import DemandCalculator
from unittest import TestCase
from src.demand_management.aggregates.num_of_charging_stations import NumberOfChargingStation

class TestDemandCalculator(TestCase):

    def test_calculate_demand_valid_inputs(self):
        population = 1000
        usage_rate = 50
        number_of_stations = 5
        postal_code = "12345"
        result = DemandCalculator.calculate_demand(population, usage_rate, number_of_stations, postal_code)
        self.assertEqual(result, 100)

    def test_calculate_demand_population_zero(self):
        population = 0
        usage_rate = 50
        number_of_stations = 5
        postal_code = "12345"
        with self.assertRaises(ValueError):
            DemandCalculator.calculate_demand(population, usage_rate, number_of_stations, postal_code)

    def test_calculate_demand_negative_population(self):
        population = -500
        usage_rate = 50
        number_of_stations = 5
        postal_code = "12345"
        with self.assertRaises(ValueError):
            DemandCalculator.calculate_demand(population, usage_rate, number_of_stations, postal_code)

    def test_calculate_demand_usage_rate_zero(self):
        population = 1000
        usage_rate = 0
        number_of_stations = 5
        postal_code = "12345"
        with self.assertRaises(ValueError):
            DemandCalculator.calculate_demand(population, usage_rate, number_of_stations, postal_code)

    def test_calculate_demand_negative_usage_rate(self):
        population = 1000
        usage_rate = -10
        number_of_stations = 5
        postal_code = "12345"
        with self.assertRaises(ValueError):
            DemandCalculator.calculate_demand(population, usage_rate, number_of_stations, postal_code)

    def test_calculate_demand_number_of_stations_zero(self):
        population = 1000
        usage_rate = 50
        number_of_stations = 0
        postal_code = "12345"
        with self.assertRaises(ValueError):
            DemandCalculator.calculate_demand(population, usage_rate, number_of_stations, postal_code)

    def test_calculate_demand_number_of_stations_negative(self):
        population = 1000
        usage_rate = 50
        number_of_stations = -1
        postal_code = "12345"
        with self.assertRaises(ValueError):
            DemandCalculator.calculate_demand(population, usage_rate, number_of_stations, postal_code)

    def test_demand_formula_latex_string(self):
        calculator = DemandCalculator()
        formula = calculator.demand_formula_latex()
        expected_formula = r"Demand  Score: \frac{{\text{{population}} \cdot \text{{usage\_rate}}}}{{100 \cdot \text{{number\_of\_stations}}}}"
        self.assertEqual(formula, expected_formula)

    def test_demand_calculator_str_method(self):
        calculator = DemandCalculator()
        self.assertEqual(str(calculator), calculator.demand_formula_latex())