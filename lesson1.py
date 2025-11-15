import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
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
vehicle_data = vehicle_data.dropna(axis=0) # for handling missing values
# y = vehicle_data.price
vehicle_features = [
    "Fuel_Efficiency",
    "Engine_Performance",
    "Acceleration",
    "Car_Brand",
    "Model",
]
X = vehicle_data[vehicle_features]
model = DecisionTreeRegressor(random_state=1)
