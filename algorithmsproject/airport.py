class Airport(object):
    """Represents an airport"""

    def __init__(self, airport_name: str, country: str, code: str, latitude: float, longitude: float):
        self.name = airport_name  # Name of airport. May or may not contain the City name.
        self.country = country  # Name of airport. May or may not contain the City name.
        self.code = code  # 3-letter IATA code
        self.latitude = latitude  # Latitude Decimal degrees, usually to six significant digits. Negative is South, positive is North.
        self.longitude = longitude  # Longitude Decimal degrees, usually to six significant digits.Negative is West, positive is East.

    def get_currency(self):
        # TODO Implement me!
        pass

    def get_current_rates(self):
        # TODO Implement me!
        pass

    def __repr__(self):
        return f'{self.code}'
