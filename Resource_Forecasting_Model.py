import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Load dataset
data = pd.read_csv('synthetic_city_data.csv')

# Handle missing values
data.fillna(method='ffill', inplace=True)

# Feature and target variables
features = data[['Temperature', 'Humidity', 'Rainfall', 'Water_Flow', 'Electricity_Reading', 'Waste_Level']]
targets = data[['Water_Usage', 'Electricity_Usage', 'Waste_Collection']]

# Normalize the data
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)
targets_scaled = scaler.fit_transform(targets)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, targets_scaled, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Train Linear Regression model for each resource
models = {}
predictions = {}
errors = {}

for resource in ['Water_Usage', 'Electricity_Usage', 'Waste_Collection']:
    model = LinearRegression()
    model.fit(X_train, y_train[:, ['Water_Usage', 'Electricity_Usage', 'Waste_Collection'].index(resource)])
    models[resource] = model
    y_pred = model.predict(X_test)
    predictions[resource] = y_pred
    mae = mean_absolute_error(y_test[:, ['Water_Usage', 'Electricity_Usage', 'Waste_Collection'].index(resource)], y_pred)
    rmse = np.sqrt(mean_squared_error(y_test[:, ['Water_Usage', 'Electricity_Usage', 'Waste_Collection'].index(resource)], y_pred))
    errors[resource] = {'MAE': mae, 'RMSE': rmse}

# Display errors
for resource, error in errors.items():
    print(f'{resource} - MAE: {error["MAE"]}, RMSE: {error["RMSE"]}')

  



