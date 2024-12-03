import pytest
from unittest.mock import MagicMock
from fuel_gauge import FuelGauge

class TestFuelGaugeErrorRaising:
    def setup_method(self):
        self.fuel_gauge = FuelGauge()
        self.fuel_gauge.main = MagicMock()
        self.invalid_split = ["1-10", "1 10", "1.5 2"]
        self.division_zero = ["1/0", "10/0", "2/0"]
        self.str_input = ["cat/dog", "dog/cat", "cat/1", "1/cat"]
    
    def test_fuel_gauge_value_error_for_invalid_split(self):
        for invalid_input in self.invalid_split:
            self.fuel_gauge.gauge_to_fuel(invalid_input)
            self.fuel_gauge.main.assert_called_once()
            self.fuel_gauge.main.reset_mock()
    def test_fuel_gauge_zero_division_error(self):
        for input in self.division_zero:
            self.fuel_gauge.gauge_to_fuel(input)
            self.fuel_gauge.main.assert_called_once()
            self.fuel_gauge.main.reset_mock()

    def test_fuel_gauge_for_str_inputs(self):
        for input in self.str_input:
            self.fuel_gauge.gauge_to_fuel(input)
            self.fuel_gauge.main.assert_called_once()
            self.fuel_gauge.main.reset_mock()