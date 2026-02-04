import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load data
BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR.parent / "data" / "system_logs.csv"

data = pd.read_csv(data_path)

# Recompute anomaly labels (lightweight, no retraining logic reuse here)
from sklearn.ensemble import IsolationForest

features = data[['cpu_usage', 'memory_usage', 'error_count']]

model = IsolationForest(
    n_estimators=100,
    contamination=0.2,
    random_state=42
)

model.fit(features.values)
data['anomaly'] = model.predict(features.values)

# Split normal vs anomalies
normal = data[data['anomaly'] == 1]
anomaly = data[data['anomaly'] == -1]

# Plot
plt.figure()
plt.scatter(normal['cpu_usage'], normal['memory_usage'], label='Normal')
plt.scatter(anomaly['cpu_usage'], anomaly['memory_usage'], label='Anomaly')
plt.xlabel('CPU Usage')
plt.ylabel('Memory Usage')
plt.title('System Log Anomaly Detection')
plt.legend()
plt.show()
