from algorithmsproject.airportatlas import AirportAtlas
from algorithmsproject.bruteforce import BruteForce
from algorithmsproject.greedysearch import GreedySearch
from algorithmsproject.travelplan import TravelPlan
from algorithmsproject.dijkstra import Graph


class EconomicRoutesApp:

    """Class to keep a cache of each"""
    def __init__(self):
        self.cache_airport = {}  # Dictionary of airports indexed by their code
        self.cache_aircraft = {}  # Dictionary of aircraft indexed by their code
        self.cache_currency = {}  # Dictionary of currencies indexed by their code
        self.travel_plans = []

    def load_all_data(self):
        """Load all input data from the input folder."""
        atlas = AirportAtlas()
        self.cache_airport = atlas.load_airports()
        self.cache_aircraft = atlas.load_aircraft()
        self.cache_currency = atlas.load_currency()

    def read_test_data(self, path_to_test_data):
        """Read test file with sample routes"""

        print(f'Reading routes from {path_to_test_data}')
        with open('./input/test.csv') as fp:
            lines = fp.readlines()
            for line in lines:
                print(f'Route: {line}')
                tokens = line.strip().split(',')
                airport_codes = tokens[:-1]
                aircraft_code = tokens[-1]
                travel_plan = TravelPlan()
                for airport_code in airport_codes:
                    travel_plan.add_airport(
                        self.cache_airport[airport_code]
                    )
                travel_plan.set_start_airport(
                    self.cache_airport[tokens[0]]
                )

                travel_plan.add_aircraft(
                    self.cache_aircraft[aircraft_code]
                )
                self.travel_plans.append(travel_plan)


    def find_economic_routes(self):
        """Finds the most economic routes"""

        for travel_plan in self.travel_plans:
            try:
                print('=' * 80)
                print(f'Finding routes for {travel_plan}')
                search_algorithm = BruteForce(travel_plan)
                # search_algorithm = GreedySearch(travel_plan)
                cheapest_route, cost = search_algorithm.search()

                print(f'Cheapest route is {cheapest_route} with cost of € {round(cost, 2)}')
                print('*' * 80, '\n')
            except ValueError as e:
                print(e)


def main():
    # read the input file into classes/structures
    application = EconomicRoutesApp()
    application.load_all_data()

    path_to_test_data = './input/test.csv'
    application.read_test_data(path_to_test_data)
    application.find_economic_routes()

    # read flight plan from test.csv
    # for each flight plan,
    #       compute shortest path
    #       print shortest path
    # finish


if __name__ == '__main__':
    main()
