import csv
import pandas

# def parseFile(input):
#     N, instructions = None, []
#     with open(input, 'r') as f:
#         N = int(f.readline())
#         for line in f.readlines():
#             instructions.append(line)
#     return N


with open('../input/airport.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    airports =[]
    for row in readCSV:
        key =row[4]
        # airports = {key: row[6], key: row[7]}
        airports = { key: (row[6], row[7]) }

    print(airports)

# airports = pandas.read_csv("../input/aircraft.csv", header=None, dtype=str)

# print(airports)
