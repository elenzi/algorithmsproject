import copy

from algorithmsproject.airportatlas import AirportAtlas
from algorithmsproject.route import Route
from algorithmsproject.travelplan import TravelPlan
import itertools


class GreedySearch:
    """Exhaustively searches for the shortest path."""

    def __init__(self, travel_plan: TravelPlan):
        self.travel_plan = travel_plan

    def search(self):
        """Find the shortest path"""
        print('Initiating search.....')
        middle = [airport for airport in self.travel_plan.airports
                  if airport.code != self.travel_plan.start_airport.code]

        # print(f'len(middle) = {len(middle)}')
        # print(f'len(self.travel_plan.airports) = {len(self.travel_plan.airports)}')
        print("Possible routes: ")
        assert len(middle) < len(self.travel_plan.airports), f'{len(middle)} {len(self.travel_plan.airports)}'
        permutations = itertools.permutations(middle, r=len(middle))
        route_collection = []
        for p in permutations:
            # Here p refers to a partial route
            # route is a queue, why did you use a queue
            route = Route()
            route.enqueue(self.travel_plan.start_airport)
            for airport in p:
                route.enqueue(airport)
            route.enqueue(self.travel_plan.start_airport)
            route_collection.append(route)

        # Let's look into our route collection
        min_cost = None
        cheapest_route = None

        atlas = AirportAtlas()

        for r in route_collection:
            try:
                cost = atlas.compute_cost(r, self.travel_plan.aircraft)

                # print('Route collection', r, r.size())
                if min_cost is None:
                    # print('\tSetting initial minimum cost')
                    min_cost = cost
                    cheapest_route = r
                    continue

                if cost < min_cost:
                    # print('\tFound a new minimum cost')
                    min_cost = cost
                    cheapest_route = r
            except ValueError:
                raise

        # We're done searching
        return cheapest_route, min_cost
