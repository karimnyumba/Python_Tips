import numpy as np

audio_data = np.array([-0.5, 0.2, 0.8, -0.3, 0.6])

# Normalize the audio signal
max_amplitude = max(np.abs(audio_data))
audio_data_normalized = list(map(lambda x: x / max_amplitude, audio_data))