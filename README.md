# Machine Learning Model For Smart City Management System


## Resource Forecasting and Anomaly Detection

This repository contains Python scripts for forecasting resource usage and detecting anomalies in the data. The resources include water usage, electricity usage, and waste collection. 



## Sample Dataset

The dataset used in this project is a time-series data containing daily records of various resource usages. Here is a sample of the dataset:

| Date       | Water_Usage | Electricity_Usage | Waste_Collection | Temperature | Humidity | Rainfall | Water_Flow | Electricity_Reading | Waste_Level |
|------------|-------------|-------------------|------------------|-------------|----------|----------|------------|---------------------|-------------|
| 01-01-2024 | 1307.26     | 470.52            | 27.32            | 24.76       | 68.42    | 3.90     | 102.40     | 197.80              | 14.05       |
| 02-01-2024 | 1322.52     | 415.83            | 27.82            | 25.60       | 50.94    | 3.49     | 120.36     | 193.39              | 17.75       |
| 03-01-2024 | 1352.85     | 561.52            | 30.14            | 25.15       | 49.57    | 2.88     | 92.39      | 217.97              | 15.94       |
| 04-01-2024 | 1272.68     | 448.71            | 26.21            | 32.39       | 44.82    | 0.01     | 98.96      | 211.94              | 13.76       |
| 05-01-2024 | 1301.10     | 499.04            | 23.99            | 14.22       | 49.30    | 0.50     | 102.18     | 223.74              | 14.78       |




## Scripts

### There are three Python scripts in this repository:

1. Resourse_Forecasting_Model.py: This script contains the implementation of the forecasting model for predicting future resource usage.
   
2. Anomaly_Detection_Model.py: This script contains the implementation of the anomaly detection model that identifies unusual patterns in resource usage.
   
3. Visualization.py: This script contains functions for visualizing the actual and predicted resource usage, as well as the detected anomalies.


## Usage
To use these scripts, clone the repository and run the Python scripts in your local environment. Make sure to install the necessary Python libraries mentioned in the **requirements.txt** file.
