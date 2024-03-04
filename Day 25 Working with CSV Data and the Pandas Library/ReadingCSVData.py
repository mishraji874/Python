"""with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)"""

"""import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempreature = []
    #for row in data:
    #    print(row)
    for row in data:
        if row[1] != "temp":
            tempreature.append(int(row[1]))
    print(tempreature) """

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])