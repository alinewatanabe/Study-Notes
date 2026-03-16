import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_gray_count = len(data[data["Primary Fur Color"] == "Gray"])
data_cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
data_black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [data_gray_count, data_cinnamon_count, data_black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("data_Fur_Color.csv")