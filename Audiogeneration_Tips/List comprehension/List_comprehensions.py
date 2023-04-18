import numpy as np

duration = 2  # seconds
frequency = 440  # Hz
sampling_rate = 44100  # Hz
amplitude = 0.5  # Amplitude (0 to 1)

# Generate the audio data as a list using a list comprehension
t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
audio_data = [amplitude * np.sin(2 * np.pi * frequency * t_i) for t_i in t]