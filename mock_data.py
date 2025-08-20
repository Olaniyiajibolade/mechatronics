import pandas as pd

mock_car_file = r"c:\Users\Hello\Downloads\archive\car_performance_dataset.csv"
try:
    mock_data = pd.read_csv(mock_car_file)
    print(mock_data.describe())
except FileNotFoundError:
    print("Error: file not found")

print(mock_data.head())
