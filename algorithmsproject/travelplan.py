

class TravelPlan:

    def __init__(self):
        self.airports = set()
        # A Set is an unordered collection data type that is iterable,
        # mutable, and has no duplicate elements.
        # The major advantage of using a set, as opposed to a list,
        # is that it has a highly optimized method for checking whether a
        # specific element is contained in the set.
        self.start_airport = None
        self.end_airport = None
        self.aircraft = None

    def add_airport(self, airport):
        self.airports.add(airport)

    def set_start_airport(self, airport):
        self.start_airport = airport
        self.end_airport = airport
        self.airports.add(airport)

    def add_aircraft(self, aircraft):
        self.aircraft = aircraft

    def __repr__(self):
        intermediary = ' - '.join([str(s) for s in self.airports
                                   if s.code != self.start_airport.code])
        return f'{self.start_airport} > {intermediary} > {self.end_airport}'


