import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])
print(type(data["temp"]))

#Series is a 1-dimensonal and DataFrames are the 2-dimensional

data_dict = data.to.dict() #used to print the data in the form of dictionary
print(data_dict)

temp_list = data["temp"].to_list() #prints the result in the form of list
print(temp_list)
print(len(temp_list))

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean()) #used to print the mean of the list
print(data["temp"].max()) #prints the maximum of the temp

#Get data in columns
print(data["conditon"])
print(data.condition)

#Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int((9*monday.temp/5) + 32)
print(monday.temp)

#Create a dataframe from scratch

data_dicts = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
create = pandas.DataFrame(data_dicts)
print(create)
data.to_csv("new_data.csv") #to convert the data into csv file