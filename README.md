Intelligent Log Anomaly Detector

## Overview

The **Intelligent Log Anomaly Detector** is a machine learning–based system that automatically detects abnormal system behavior from log-derived metrics and explains the probable root cause of each anomaly. It is designed to simulate how modern IT monitoring and AIOps tools identify failures before they escalate.

This project uses **Isolation Forest**, an unsupervised ML algorithm, to learn normal system behavior and flag deviations such as CPU spikes, memory overuse, or error surges.

---

## Problem Statement

Modern systems generate massive logs, making manual monitoring inefficient and error-prone. Traditional threshold-based monitoring often fails to detect subtle anomalies or explain *why* an anomaly occurred.

This project addresses:

* Automatic anomaly detection without labeled data
* Root cause explanation for detected anomalies
* Simple, reproducible pipeline suitable for real-world systems

---

## Objectives

* Detect anomalies in system metrics using machine learning
* Identify the root cause of anomalies (CPU, memory, errors)
* Visualize anomalies for better interpretability
* Build a modular, GitHub-ready project structure

---

## Tech Stack

* **Language:** Python 3.11
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib
* **ML Algorithm:** Isolation Forest
* **Version Control:** Git & GitHub

---

## Project Structure

```
Intelligent_Log_Anomaly_Detector/
│
├── data/
│   └── system_logs.csv
│
├── src/
│   ├── anomaly_detector.py
│   └── visualize_anomalies.py
│
├── results/
│   └── result_plot.png
│
├── .gitignore
├── README.md
```

---

## Methodology

1. **Data Loading** – System metrics (CPU, memory, error count) are loaded from CSV logs
2. **Feature Selection** – Relevant numerical metrics are extracted
3. **Model Training** – Isolation Forest learns normal behavior patterns
4. **Anomaly Detection** – Outliers are flagged as anomalies
5. **Root Cause Analysis** – Rule-based logic explains why the anomaly occurred
6. **Visualization** – Anomalies are plotted for analysis

---

## Sample Output

Each log entry is classified as:

* `1` → Normal behavior
* `-1` → Anomalous behavior

Example root cause output:

* High CPU usage
* High memory usage
* Spike in system errors

---

## Results

The system successfully:

* Identified abnormal CPU and memory spikes
* Flagged error surges as anomalies
* Provided human-readable explanations

Visualization output is saved in the `results/` folder.

---

## How to Run

```bash
# Install dependencies
pip install pandas numpy scikit-learn matplotlib

# Run anomaly detection
python src/anomaly_detector.py

# Visualize results
python src/visualize_anomalies.py
```

---

## Future Enhancements

* Real-time log streaming (Kafka / MQTT)
* Deep learning–based anomaly detection
* Dashboard integration (Grafana / Streamlit)
* Automated alerting system

---

## Author

**Modhika B**
Electronics and Communication Engineering

---

## License

This project is for academic and learning purposes.
