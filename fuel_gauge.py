class FuelGauge:
    def gauge_to_fuel(self, fuel: str) -> str:
        """_Convert the gauge display to percentage of fule remaining_

        Args:
            fuel (str): _A fraction of fule as displayed on the gauge_

        Returns:
            str: _Percentage of fuel remaining_
        Example:
            >>> gauge_to_fuel("1/4")
            "25%" 
        """