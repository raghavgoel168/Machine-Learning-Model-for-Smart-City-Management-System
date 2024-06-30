import pandas as pd
import numpy as np

# Generate date range
dates = pd.date_range(start='2024-01-01', periods=365, freq='D')

# Generate synthetic data
water_usage = np.random.normal(loc=1300, scale=100, size=len(dates))
electricity_usage = np.random.normal(loc=450, scale=50, size=len(dates))
waste_collection = np.random.normal(loc=30, scale=5, size=len(dates))
temperature = np.random.normal(loc=25, scale=5, size=len(dates))
humidity = np.random.normal(loc=60, scale=10, size=len(dates))
rainfall = np.random.exponential(scale=2, size=len(dates))
water_flow = np.random.normal(loc=100, scale=10, size=len(dates))
electricity_reading = np.random.normal(loc=200, scale=20, size=len(dates))
waste_level = np.random.normal(loc=15, scale=2, size=len(dates))

# Create DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Water_Usage': water_usage,
    'Electricity_Usage': electricity_usage,
    'Waste_Collection': waste_collection,
    'Temperature': temperature,
    'Humidity': humidity,
    'Rainfall': rainfall,
    'Water_Flow': water_flow,
    'Electricity_Reading': electricity_reading,
    'Waste_Level': waste_level
})

# Save to CSV
data.to_csv('C:/Users/ragha/OneDrive/Desktop/Hackathons/Machine Learning Model for Smart City Management System/synthetic_city_data.csv', index=False)

print(data.head())
