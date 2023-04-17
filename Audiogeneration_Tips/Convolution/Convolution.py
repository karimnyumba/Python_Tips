import numpy as np
from scipy.signal import convolve

# Generate an example audio signal
duration = 2  # seconds
frequency = 440  # Hz
sampling_rate = 44100  # Hz
t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)

# Generate an impulse response for convolution (e.g., for reverberation)
impulse_response = np.random.rand(44100) - 0.5  # Random impulse response

# Apply convolution to the audio signal
convolved_audio_data = convolve(audio_data, impulse_response, mode='full')