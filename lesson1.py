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
    print("File Loaded Successfully")
except FileNotFoundError:
    print(
        f"Error: The {vehicle_performance_file} file was not found. Please check the file path"
    )
    exit()  # does not run the code below if there is an error
vehicle_features = [
    "Fuel_Efficiency",
    "Engine_Performance",
    "Acceleration",
    "Car_Brand",
    "Model",
]
# print(vehicle_data[vehicle_features])
