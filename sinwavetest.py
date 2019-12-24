import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# Create sine wave
sampling_rate = 44100
frequency = 1000
num_samples = 88200
sine_wave = []
for x in range(num_samples):
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
    
# Save sine wave as Wav file
amplitude = 8000
file = "test1.wav"
wav_file=wave.open(file, 'w')
nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h',int(s*amplitude)))
wav_file.close()

# Plot sine wave
plt.plot(sine_wave[:300])
plt.show()