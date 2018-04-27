import copy
from math import pi, sin, cos, acos
import csv

from algorithmsproject.aircraft import Aircraft
from algorithmsproject.airport import Airport
from algorithmsproject.currencies import Currency
from algorithmsproject.route import Route


class AirportAtlas:

    def __init__(self):
        self.path_to_airport_csv = "./input/airport.csv"
        self.path_to_aircraft_csv = "./input/aircraft.csv"
        self.path_to_country_currency_csv = "./input/countrycurrency.csv"
        self.path_to_currency_rates_csv = "./input/currencyrates.csv"

        # Dictionary of objects 0(1)
        # Key-value relationship mapping
        self.airports = {}
        self.aircraft = {}
        self.currencies = {}

    def load_airports(self):
        """Load airport data from given CSV file.

        The airports are stored in a hash table (or dictionary) to
        facilitate speedy retrievals.

        :return: A dictionary of Airports indexed by their code.
        """

        print(f'Loading airport data from {self.path_to_airport_csv}')

        # try:
        self.airports = {}  # Creates an empty dictionary to store airport objects

        with open(self.path_to_airport_csv) as fp:
            read_csv = csv.reader(fp, delimiter=',')
            for row in read_csv:
                key = row[4]
                self.airports[key] = Airport(airport_name=row[2],
                                             country=row[3],
                                             code=row[4],
                                             latitude=float(row[6]),
                                             longitude=float(row[7]))
        # except IOError as (errno, strerror):
        # print("I/O error({0}): {1}".format(errno, strerror))
        return self.airports

    def get_airport(self, code):
        """ Method to get check if code matches a key in airports dictionary
        and return airport object details """
        if code in self.airports.keys():
            airport = self.airports[code]
            print("Airport details: ", airport)
            return self.airports[code]

    def get_distance(self, code1: str, code2: str):
        # TODO Refactor this method
        # Get airports based on input codes (i.e. `code1` and `code2`).
        airport_from = self.get_airport(code1)
        airport_to = self.get_airport(code2)

        # Use the coordinates of the two airports to compute the distance.
        return self.great_circle_distance(
            airport_from.latitude,
            airport_from.longitude,
            airport_to.latitude,
            airport_to.longitude
        )

    @staticmethod
    def great_circle_distance(latitude1: float, longitude1: float, latitude2: float, longitude2: float):
        """ Method to calculate the distance between airports"""

        assert isinstance(latitude1, float)
        assert isinstance(longitude1, float)
        assert isinstance(latitude2, float)
        assert isinstance(longitude2, float)

        radius_earth = 6371  # in km

        theta1 = longitude1 * (2 * pi) / 360
        theta2 = longitude2 * (2 * pi) / 360
        phi1 = (90 - latitude1) * (2 * pi) / 360
        phi2 = (90 - latitude2) * (2 * pi) / 360
        distence = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * radius_earth
        return distence

    def load_aircraft(self):
        """Load airport data from given CSV file.

        The airports are stored in a hash table (or dictionary) to
        facilitate speedy retrievals.

        :return: A dictionary of Airports indexed by their code.
        """
        print(f'Loading aircraft data from {self.path_to_aircraft_csv}')

        # try:
        self.aircraft = {}  # Creates an empty dictionary to store airport objects

        with open(self.path_to_aircraft_csv) as fp:
            read_csv = csv.DictReader(fp, delimiter=',')
            for row in read_csv:
                key = row['code']
                self.aircraft[key] = Aircraft(
                    code=row['code'],
                    units=row['units'],
                    range_max=row['range']
                )
        return self.aircraft

    def load_currency(self):

        print('Loading currency...')
        self.currencies = {}  # Creates an empty dictionary to store airport objects

        with open(self.path_to_country_currency_csv) as fp:
            read_csv = csv.DictReader(fp, delimiter=',')
            # print("Creating objects")
            for row in read_csv:
                key = row['currency_alphabetic_code'].strip()
                self.currencies[key] = Currency(
                    code=row['currency_alphabetic_code'],
                    country_name=row['name']
                )

        print(f'Loaded {len(self.currencies)} currencies from {self.path_to_country_currency_csv}')

        with open(self.path_to_currency_rates_csv) as fp:
            read_csv = csv.reader(fp, delimiter=',')
            num_failed = 0
            for row in read_csv:
                currency_code = row[1]
                try:
                    currency = self.currencies[currency_code.strip()]
                    currency.to_rate = row[2]
                    currency.from_rate = row[3]
                except KeyError as e:
                    # print('\tERROR: The currency with {} cannot be found in our lookup table'.format(e))
                    num_failed += 1
                    pass
        print(f'Could not process {num_failed} records')

        # print("Currencies: ", self.currencies)
        return self.currencies

    def compute_cost(self, route: Route, aircraft: Aircraft):

        route_copy = copy.deepcopy(route)
        # deepcopy() actually preserves the graphical structure of the original compound data
        total_cost = 0
        total_distance = 0
        airport_from: Airport = None
        airport_to: Airport = None

        while route_copy.size() > 0:
            # print(route_copy)
            airport_to = route_copy.dequeue()

            if airport_from is None:
                airport_from = airport_to
                continue

            if airport_from.code == airport_to.code:
                continue
            else:

                # Compute distance between two airports
                distance = self.great_circle_distance(
                    airport_from.latitude,
                    airport_from.longitude,
                    airport_to.latitude,
                    airport_to.longitude
                )

                if distance > aircraft.get_maximum_range():
                    raise ValueError('Trip not feasible. Try another route.')

                # Find the exchange rate of the airport_from
                exchange_rate = 1
                for currency in self.currencies:
                    if currency.country_name == airport_from.country:
                        exchange_rate = currency.to_rate

                cost = distance * exchange_rate

                total_cost += cost
                total_distance += distance
                airport_from = airport_to

        return total_cost
