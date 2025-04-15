import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from utils import low_pass_filter, normalize_signal, calculate_heart_rate

print("Starting ECG Analyzer...")

# Load data
try:
    data = pd.read_csv('ECG Signal Analyzer/data/sample_ecg.csv')
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Inspect data
print("Inspecting data...")
print(data.head())

# Plot raw data
try:
    plt.figure(figsize=(10, 4))
    plt.plot(data['Time (s)'], data['Voltage (mV)'])
    plt.title('Raw ECG Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (mV)')
    plt.grid()
    plt.savefig('plots/raw_ecg.png')
    plt.show()
    print("Raw ECG plot displayed and saved.")
except Exception as e:
    print(f"Error plotting raw ECG: {e}")
    exit()

# Preprocess the signal
try:
    filtered_signal = low_pass_filter(data['Voltage (mV)'])
    normalized_signal = normalize_signal(filtered_signal)
    print("Signal preprocessed successfully.")
except Exception as e:
    print(f"Error preprocessing signal: {e}")
    exit()

# Plot filtered data
try:
    plt.figure(figsize=(10, 4))
    plt.plot(data['Time (s)'], normalized_signal)
    plt.title('Filtered ECG Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Voltage')
    plt.grid()
    plt.savefig('plots/filtered_ecg.png')
    plt.show()
    print("Filtered ECG plot displayed and saved.")
except Exception as e:
    print(f"Error plotting filtered ECG: {e}")
    exit()

# Detect R-peaks
try:
    peaks, _ = find_peaks(normalized_signal, height=0.5, distance=150)
    plt.figure(figsize=(10, 4))
    plt.plot(data['Time (s)'], normalized_signal)
    plt.plot(data['Time (s)'][peaks], normalized_signal[peaks], 'rx')
    plt.title('R-Peak Detection')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Voltage')
    plt.grid()
    plt.savefig('plots/r_peak_detection.png')
    plt.show()
    print("R-Peak Detection plot displayed and saved.")
except Exception as e:
    print(f"Error detecting R-peaks: {e}")
    exit()

# Calculate heart rate
try:
    heart_rate = calculate_heart_rate(data['Time (s)'], peaks)
    print(f'Average Heart Rate: {heart_rate:.2f} BPM')
except Exception as e:
    print(f"Error calculating heart rate: {e}")
    exit()
