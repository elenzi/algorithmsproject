class Aircraft:
    __MIN_FUEL = 100

    def __init__(self, flight_number="", code: str = None, units: str = None, range_max: int = None):
        # Confirm what columns should be implemented for this Aircraft class.
        self.code = code
        self.units = units
        self.range_max = int(range_max)
        self.flight_number = flight_number
        self.__fuel = 0
        self.__fuelCheck = False
        self.__maxFuel = self.__MIN_FUEL

    def get_maximum_range(self):
        """Gets the maximum range of this aircraft in Kilometers"""
        if self.units == 'metric':
            return self.range_max
        else:
            return self.range_max * 1.6  # Confirm how to convert from imperial distance to metric.

    def fuel_check(self):
        if self.__fuel < self.__MIN_FUEL:
            print("[", self.flight_number, "] Fuel Check Failed: Current fuel below safe limit:", self.__fuel,
                  " less than ", self.__MIN_FUEL)
            self.__fuelCheck = False
        else:
            print("[", self.flight_number, "] Fuel Check Complete. Current Fuel Level :", self.__fuel)
            self.__fuelCheck = True
        return self.__fuelCheck

    def take_off(self):
        if self.fuel_check():
            print("[", self.flight_number, "] Cleared for take off! Fasten your seat-belt!")
        else:
            print("[", self.flight_number, "] Take off failed: complete pre-flight fuel check and refuel first.")
            print(self.fuel_check())

    def print_fuel_level(self):
        print("Current fuel", self.__fuel)

    def add_fuel(self, volume):
        unusedFuel = 0
        if volume < 0:
            print("No syphoning fuel!!")
        elif self.__fuel + volume <= self.__maxFuel:
            self.__fuel = self.__fuel + volume
        elif self.__fuel + volume > self.__maxFuel:
            self.__fuel = self.__maxFuel
            unusedFuel = volume - self.__fuel
        return unusedFuel

    def __repr__(self):
        return f'{self.code}'
