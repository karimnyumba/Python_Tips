import numpy as np
from scipy.signal import resample

# Generate an example audio signal
duration = 2  # seconds
frequency = 440  # Hz
sampling_rate = 44100  # Hz
t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)

# Define the target sampling rate for resampling
target_sampling_rate = 22050  # Hz

# Resample the audio signal to the target sampling rate
resampled_audio_data = resample(audio_data, int(duration * target_sampling_rate))