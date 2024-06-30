import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import IsolationForest

# Load dataset
data = pd.read_csv('synthetic_city_data.csv')

# Handle missing values
data.fillna(method='ffill', inplace=True)

# Use the same features as the previous model
features = data[['Temperature', 'Humidity', 'Rainfall', 'Water_Flow', 'Electricity_Reading', 'Waste_Level']]


# Normalize the data
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)


# Train Isolation Forest model
iso_forest = IsolationForest(contamination=0.01)
iso_forest.fit(features_scaled)

# Predict anomalies
anomalies = iso_forest.predict(features_scaled)
data['Anomaly'] = anomalies

# Identify anomaly indices
anomaly_indices = data[data['Anomaly'] == -1].index
print(f'Anomaly Indices: {anomaly_indices}')
