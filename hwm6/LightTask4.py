#######################################################################################################################
# Light. Task 4
# Создать csv файл с данными о машине.
#######################################################################################################################
# In this task I used an example of data related to cars in JSON-format from the site (partially) to make this task
# closer to the reality
# https://github.com/vega/vega/blob/master/docs/data/cars.json
#######################################################################################################################
import csv
from datetime import datetime
def getKeysList(jsonData):
    keys = []
    firstItem = jsonData[0]
    for key in firstItem:
        keys.append(key)
    return keys


def getValsList(jsonData):
    vals = []
    for item in jsonData:
        rowVals = []
        for key in item.keys():
            rowVals.append(item[key])
        vals.append(rowVals)
    return vals


# cars data in json format

cars = [
   {
      "Name": "chevrolet chevelle malibu",
      "Miles_per_Gallon": 18,
      "Cylinders": 8,
      "Displacement": 307,
      "Horsepower": 130,
      "Weight_in_lbs": 3504,
      "Acceleration": 12,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "buick skylark 320",
      "Miles_per_Gallon": 15,
      "Cylinders": 8,
      "Displacement": 350,
      "Horsepower": 165,
      "Weight_in_lbs": 3693,
      "Acceleration": 11.5,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "plymouth satellite",
      "Miles_per_Gallon": 18,
      "Cylinders": 8,
      "Displacement": 318,
      "Horsepower": 150,
      "Weight_in_lbs": 3436,
      "Acceleration": 11,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "amc rebel sst",
      "Miles_per_Gallon": 16,
      "Cylinders": 8,
      "Displacement": 304,
      "Horsepower": 150,
      "Weight_in_lbs": 3433,
      "Acceleration": 12,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "ford torino",
      "Miles_per_Gallon": 17,
      "Cylinders": 8,
      "Displacement": 302,
      "Horsepower": 140,
      "Weight_in_lbs": 3449,
      "Acceleration": 10.5,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "ford galaxie 500",
      "Miles_per_Gallon": 15,
      "Cylinders": 8,
      "Displacement": 429,
      "Horsepower": 198,
      "Weight_in_lbs": 4341,
      "Acceleration": 10,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "chevrolet impala",
      "Miles_per_Gallon": 14,
      "Cylinders": 8,
      "Displacement": 454,
      "Horsepower": 220,
      "Weight_in_lbs": 4354,
      "Acceleration": 9,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "plymouth fury iii",
      "Miles_per_Gallon": 14,
      "Cylinders": 8,
      "Displacement": 440,
      "Horsepower": 215,
      "Weight_in_lbs": 4312,
      "Acceleration": 8.5,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "pontiac catalina",
      "Miles_per_Gallon": 14,
      "Cylinders": 8,
      "Displacement": 455,
      "Horsepower": 225,
      "Weight_in_lbs": 4425,
      "Acceleration": 10,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "amc ambassador dpl",
      "Miles_per_Gallon": 15,
      "Cylinders": 8,
      "Displacement": 390,
      "Horsepower": 190,
      "Weight_in_lbs": 3850,
      "Acceleration": 8.5,
      "Year": "1970-01-01",
      "Origin": "USA"
   },
   {
      "Name": "citroen ds-21 pallas",
      "Miles_per_Gallon": "",
      "Cylinders": 4,
      "Displacement": 133,
      "Horsepower": 115,
      "Weight_in_lbs": 3090,
      "Acceleration": 17.5,
      "Year": "1970-01-01",
      "Origin": "Europe"
   },
   {
      "Name":"chevrolet chevelle concours (sw)",
      "Miles_per_Gallon": "",
      "Cylinders": 8,
      "Displacement": 350,
      "Horsepower": 165,
      "Weight_in_lbs": 4142,
      "Acceleration": 11.5,
      "Year": "1970-01-01",
      "Origin": "USA"
   }
]

start = datetime.now()

forCSVarray = []

# form the first row of the keys
keys = getKeysList(cars)
forCSVarray.append(keys)

# prepare all rows with car data since the second row
vals = getValsList(cars)
forCSVarray.extend(vals)

# check our-self
# print(forCSVarray)

# write to a csv file the whole list of cars data
with open('jsonToCSV.csv', 'w') as f:
    csvWriter = csv.writer(f, delimiter='\t')
    csvWriter.writerows(forCSVarray)

stop = datetime.now()
time_for_roport = stop - start
print("\nTotal time for reporting:")
print(time_for_roport, '\n')

# open the created file and read car data
with open('jsonToCSV.csv', 'r') as f:
    csvReader = csv.reader(f, delimiter='\t')
    for line in csvReader:
        if len(line) != 0:
            print(line)