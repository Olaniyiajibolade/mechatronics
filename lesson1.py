import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------#
# Vehicle Perforamnce Analyser
# Project 1
# ------#
try:
    vehicle_performance_file = (
        r"c:\Users\Hello\Downloads\archive\car_performance_dataset.csv"
    )
    vehicle_data = pd.read_csv(vehicle_performance_file)
    print("file loaded successfully")
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path")
# viewing the data for the structure
# print(vehicle_data.describe())
print(vehicle_data.head())
# pd.to_datetime()  # for easier plotting
vehicle_features = [
    "Fuel_Efficiency",
    "Engine_Performance",
    "Acceleration",
    "Car_Brand",
    "Model",
]
