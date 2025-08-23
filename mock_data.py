import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")  # style for the graph

mock_car_file = r"c:\Users\Hello\Downloads\archive\car_performance_dataset.csv"
try:
    mock_data = pd.read_csv(mock_car_file)
    # print(mock_data.describe())
except FileNotFoundError:
    print("Error: file not found")

# print(mock_data.head())
# Timestamp, Speed (km/h), Engine RPM, Fuel Consumption (L/100km), and Engine Load (%)

avg_fuel = mock_data["Fuel_Efficiency"].mean()
avg_acceleration = mock_data["Acceleration"].mean()

max_acceleration = mock_data["Fuel_Efficiency"].max()
# avg_price = mock_data["Price"].mean()
print(f"Average fuel: {avg_fuel: .2f} L/100km")
print(f"Average acceleration: {avg_acceleration: .2f}")
print(f"max acceleration: {max_acceleration}")

# Histogram
plt.figure(figsize=(10, 5))
sns.histplot(mock_data["Fuel_Efficiency"], bins=20, kde=True)
plt.title("Distribution of Fuel Efficiency")
plt.xlabel("Fuel Efficiency")
plt.ylabel("Usage")
plt.show()

# put exceptions if there is no coresponding data
# lets try something

# graph
plt.figure(figsize=(12, 6))
plt.plot(mock_data["Acceleration"], label="Acceleration")
plt.plot(mock_data["Fuel_Efficiency"], label="Fuel_Efficiency")
plt.title("Vehicle Acceleration and Fuel Eficiency Over Time")
plt.xlabel("m/s(square)")
plt.ylabel("fuel")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# scatter plot
plt.figure(figsize=(12, 6))
sns.scatterplot(data=mock_data, x="Acceleration", y="Fuel_Efficiency")
plt.title("fuel eficiency vs acceleration")
plt.show()

#  understanding the graph is prority
# make a 'dashboard' for the data visualization
