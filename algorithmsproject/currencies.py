class Currency:
    """A Class to get country currency"""

    def __init__(self, code: str, country_name: str=''):
        self.code = code  # Alphabetic code that uniquely identifies this currency
        self.to_rate = 0
        self.from_rate = 0
        self.country_name = country_name

    def __repr__(self):
        return f'Code {self.code}, to_euro: {self.to_rate}'
