# with open("weather_data.csv","r") as f:
#     data = f.readlines()
# import csv
# with open("weather_data.csv","r") as f:
#     data = csv.reader(f)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# #data_dict = data.to_dict()
# # # print(data_dict)
# # temp_list = data["temp"].max()
#
# # Monday = data[data.day == "Monday"]
# # new_temp = Monday.temp * (9 / 5) + 32
# # print(Monday.temp)
# # print(new_temp)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
GFur = len(data[data["Primary Fur Color"] == "Gray"])
RFur = len(data[data["Primary Fur Color"] == "Gray"])
BFur = len(data[data["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [GFur, RFur, BFur]

}
Fur = pandas.DataFrame(data_dict)
print(Fur)
Fur.to_csv("Squirrel_fur_colors.csv")






