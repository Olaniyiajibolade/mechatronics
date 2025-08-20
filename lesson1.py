import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

melbourne_csv_file_path = "C:/Users/Hello/Downloads/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_csv_file_path)
melbourne_data_features = [
    "Rooms",
    "Bathroom",
    "Landsize",
    "Longitude",
    "Latitude",
]

# print(melbourne_data.describe())
print("Head Details")
# print(melbourne_data.head())
# print(melbourne_data.isnull().sum())
print(melbourne_data_features[2])


# Vehicle Perforamnce Analyser
# Project 1

try:
    vehicle_performance_file = "path to csv file"
    vehicle_data = pd.read_csv(vehicle_performance_file)
    print("file loaded successfully")
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path")
    exit()

# viewing the data for the structure
print(vehicle_data.head())

# data cleaning
pd.to_datetime()  # for easier plotting
