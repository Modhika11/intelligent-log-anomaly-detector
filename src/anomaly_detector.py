import pandas as pd
from pathlib import Path
from sklearn.ensemble import IsolationForest

# -----------------------------
# Load data safely
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR.parent / "data" / "system_logs.csv"

data = pd.read_csv(data_path)
print(data.head())

# -----------------------------
# Feature selection
# -----------------------------
features = data[['cpu_usage', 'memory_usage', 'error_count']]

# -----------------------------
# Train Isolation Forest
# -----------------------------
model = IsolationForest(
    n_estimators=100,
    contamination=0.2,
    random_state=42
)

model.fit(features.values)

# -----------------------------
# Predict anomalies
# -----------------------------
data['anomaly'] = model.predict(features.values)

# -----------------------------
# Explain anomalies (RULE ENGINE)
# -----------------------------
def explain_anomaly(row):
    reasons = []

    if row['cpu_usage'] > 85:
        reasons.append("High CPU usage")

    if row['memory_usage'] > 80:
        reasons.append("High memory usage")

    if row['error_count'] > 5:
        reasons.append("Spike in system errors")

    if not reasons:
        return "Normal system behavior"

    return " & ".join(reasons)

# -----------------------------
# Apply explanation ONLY to anomalies
# -----------------------------
data['root_cause'] = data.apply(
    lambda row: explain_anomaly(row) if row['anomaly'] == -1 else "Normal",
    axis=1
)

# -----------------------------
# Final output
# -----------------------------
print(data[['cpu_usage', 'memory_usage', 'error_count', 'anomaly', 'root_cause']])
