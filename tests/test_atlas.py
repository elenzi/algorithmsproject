from algorithmsproject.airport import airportAtlas

# Testing airportAtlas to check load data is working
ifile = "../input/airport.csv"
inputCSV = airportAtlas(ifile)



distence = airportAtlas.great_circle_distance(34.565853, 69.212328, 34.210017, 62.2283)
print(distence)
