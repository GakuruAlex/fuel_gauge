class FuelGauge:
    def gauge_to_fuel(self, fuel: str) -> int:
        """_Convert the gauge display to percentage of fule remaining_

        Args:
            fuel (str): _A fraction of fule as displayed on the gauge_

        Returns:
            int: _Percentage of fuel remaining_
        Example:
            >>> gauge_to_fuel("1/4")
            25
            >>> gauge_to_fuel("1/2")
            50
        """
        try:
            num, denom = fuel.split("/")
        except ValueError:
            return self.main()
        else:
            if type(num) == float or type(denom) == float:
                raise ValueError
            try:
                if int(denom) == 0:
                    raise ZeroDivisionError
                else:
                    if int(num) > int(denom):
                        print("Numerator greater than denominator. Try again!")
                        return self.main()
            except ValueError:
                print(f"One or both inputs not integers! Try again.")
                return self.main()
            except ZeroDivisionError:
                print(f"Erro! Division by zero")
                return self.main()
            else:
                return round(int(num) / int(denom) * 100)
                
    def fuel_output(self, fuel: int) -> str:
        """_Convert fuel to str to output on the screen_

        Args:
            fuel (int): _percentage of remaining fuel_

        Returns:
            str: _Str to output
        Example:
            >>> fuel_output(25)
                "25%"
            >>> fuel_output(1)
                "E"
            >>> fuel_output(100)
                "F"
        """
        if fuel <= 1:
            return "E"
        elif fuel >= 99:
            return "F"
        else:
            return f"{fuel}%"
    
    def main(self):
        gauge = input("Fraction: ")
        percentage = self.gauge_to_fuel(gauge)
        output = self.fuel_output(percentage)
        print(f"{output}")

if __name__ == "__main__":
    fuelgauge = FuelGauge()
    fuelgauge.main()
            