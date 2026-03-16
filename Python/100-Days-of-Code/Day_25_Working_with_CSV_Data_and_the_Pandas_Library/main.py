# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

temp_list = data["temp"].to_list()

all = data["temp"].sum()
leng = len(temp_list)
avarage = all/leng
print(avarage)

av = data["temp"].mean()
max_temp = data["temp"].max()
print(max_temp)

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.condition == "Sunny"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Dwight", "Jim", "Angela", "Kevin"],
    "scores": [76, 70, 65, 40]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
