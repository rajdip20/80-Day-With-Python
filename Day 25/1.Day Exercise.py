# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas
data = pandas.read_csv("weather-data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)


# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)


# print(data["temp"].mean())
# print(data["temp"].max())


# Get Data in Columns
# print(data["condition"])
# print(data.condition)


# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# print(int(monday.temp)*(9/5)+32)    # Convert Celsius to Fahrenheit of Monday's Temp


# Create a dataframe from scratch
data_dict = {
    "students": ["Priyanshu", "Joy", "Rajdip"],
    "scores": [67, 56, 82]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
