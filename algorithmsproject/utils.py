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
