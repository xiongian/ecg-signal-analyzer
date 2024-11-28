import numpy as np
from scipy.signal import butter, filtfilt

def low_pass_filter(signal, cutoff=0.1, fs=500, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, signal)
    return y

def normalize_signal(signal):
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal))

def calculate_heart_rate(time, peaks):
    rr_intervals = np.diff(time[peaks])
    heart_rate = 60 / np.mean(rr_intervals)
    return heart_rate