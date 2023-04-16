import numpy as np

duration = 2  # seconds
frequency = 440  # Hz
sampling_rate = 44100  # Hz
amplitude = 0.5  # Amplitude (0 to 1)
fade_in_duration = 0.5  # seconds

# Generate the audio data as a numpy array
t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
audio_data = amplitude * np.sin(2 * np.pi * frequency * t)

# Generate a linear ramp for the fade-in effect
fade_in_samples = int(fade_in_duration * sampling_rate)
fade_in_ramp = np.linspace(0, 1, fade_in_samples)

# Apply the fade-in effect using broadcasting
audio_data[:fade_in_samples] *= fade_in_ramp