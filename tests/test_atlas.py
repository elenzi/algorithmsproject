from algorithmsproject.airport import airportAtlas
import unittest
from algorithmsproject.airport import Airport

# Testing airportAtlas to check load data is working
ifile = "../input/airport.csv"
inputCSV = airportAtlas(ifile)



distence = airportAtlas.great_circle_distance(34.565853, 69.212328, 34.210017, 62.2283)
print(distence)

class TestAirportAtlas(unittest.TestCase):

    def setUp(self):
        self.airport = Airport('Dub', 'Dublin', 4.565853, 69.212328)

    def test_load_data(self):
        self.assertAlmostEquals(self.get)
