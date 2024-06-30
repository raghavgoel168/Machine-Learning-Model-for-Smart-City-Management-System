import matplotlib.pyplot as plt
import seaborn as sns
from Resource_Forecasting_Model import predictions, data, y_test
from Anomaly_Detection_Model import anomalies

data['Anomaly'] = anomalies

# Resource Forecasting Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Set a theme for the plot
sns.set_theme()

for resource, y_pred in predictions.items():
    plt.figure(figsize=(10, 6))
    
    # Use a different color for each line
    colors = ['blue', 'green', 'red']
    resources = ['Water_Usage', 'Electricity_Usage', 'Waste_Collection']
    actual_color = colors[resources.index(resource)]
    predicted_color = 'orange' if actual_color != 'orange' else 'purple'
    
    plt.plot(y_test[:, resources.index(resource)], label='Actual', color=actual_color, linewidth=2)
    plt.plot(y_pred, label='Predicted', color=predicted_color, linewidth=2)
    
    plt.title(f'{resource} Prediction', fontsize=20, fontweight='bold')
    plt.xlabel('Time', fontsize=14)
    plt.ylabel(resource, fontsize=14)
    
    # Add a grid for better readability
    plt.grid(True)
    
    # Increase the size of the legend and move it outside the plot
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
    
    plt.show()


plt.figure(figsize=(15, 7))

# Define a custom palette
custom_palette = {1: 'skyblue', -1: 'red'}

for i, resource in enumerate(['Water_Usage', 'Electricity_Usage', 'Waste_Collection'], start=1):
    plt.subplot(1, 3, i)
    sns.scatterplot(x=data.index, y=data[resource], hue=data['Anomaly'], palette=custom_palette, s=60, edgecolor=None)
    
    plt.title(f'{resource.replace("_", " ")}', fontsize=16, fontweight='bold')
    plt.xlabel('Time', fontsize=12)
    plt.ylabel(f'{resource.replace("_", " ")}', fontsize=12)
    
    # Remove the top and right spines for a cleaner look
    sns.despine()

plt.tight_layout()
plt.show()
