import pandas as pd

melbourne_csv_file_path = "C:/Users/Hello/Downloads/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_csv_file_path)
melbourne_data_features = [
    "Rooms",
    "Bathroom",
    "Landsize",
    "Longitude",
    "Latitude",
]

print(melbourne_data.describe())


print(pd.DataFrame({"Yes": [20, 10], "No": [30, 19]}))
