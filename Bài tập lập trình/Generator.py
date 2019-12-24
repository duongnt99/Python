import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
import math as m

# Calculate frequency in octave
frequencyDo = 440 * m.pow(2,(-8/12))
frequencyDo1 = 440 * m.pow(2,(-7/12))
frequencyRe = 440 * m.pow(2,(-6/12))
frequencyMi = 440 * m.pow(2,(-5/12))
frequencyFa = 440 * m.pow(2,(-4/12))
frequencyFa1 = 440 * m.pow(2,(-3/12))
frequencySon = 440 * m.pow(2,(-2/12))
frequencySon1 = 440 * m.pow(2,(-1/12)) 
frequencyLa = 440 * m.pow(2,(0/12)) 
frequencySi = 440 * m.pow(2,(1/12)) 
frequencySi1 = 440 * m.pow(2,(2/12)) 
frequencyDo2 = 440 * m.pow(2,(3/12)) 

# Create sine wave
sampling_rate = 44100
num_samples = 88200

sine_waveDo = []
sine_waveDo1 = []
sine_waveRe = []
sine_waveMi = []
sine_waveFa = []
sine_waveFa1 = []
sine_waveSon = []
sine_waveSon1 = []
sine_waveLa = []
sine_waveSi = []
sine_waveSi1 = []
sine_waveDo2 = []

for x in range(num_samples):
    sine_waveDo.append(np.sin(2 * np.pi * frequencyDo * x * 1/sampling_rate))
    sine_waveDo1.append(np.sin(2 * np.pi * frequencyDo1 * x * 1/sampling_rate))
    sine_waveRe.append(np.sin(2 * np.pi * frequencyRe * x * 1/sampling_rate))
    sine_waveMi.append(np.sin(2 * np.pi * frequencyMi * x * 1/sampling_rate))
    sine_waveFa.append(np.sin(2 * np.pi * frequencyFa * x * 1/sampling_rate))
    sine_waveFa1.append(np.sin(2 * np.pi * frequencyFa1 * x * 1/sampling_rate))
    sine_waveSon.append(np.sin(2 * np.pi * frequencySon * x * 1/sampling_rate))
    sine_waveSon1.append(np.sin(2 * np.pi * frequencySon1 * x * 1/sampling_rate))
    sine_waveLa.append(np.sin(2 * np.pi * frequencyLa * x * 1/sampling_rate))
    sine_waveSi.append(np.sin(2 * np.pi * frequencySi * x * 1/sampling_rate))
    sine_waveSi1.append(np.sin(2 * np.pi * frequencySi1 * x * 1/sampling_rate))
    sine_waveDo2.append(np.sin(2 * np.pi * frequencyDo2 * x * 1/sampling_rate))

# Save sine wave Do as Wav file
amplitude = 8000
file1 = "Do.wav"
file2 = "Do1.wav"
file3 = "Re.wav"
file4 = "Mi.wav"
file5 = "Fa.wav"
file6 = "Fa1.wav"
file7 = "Son.wav"
file8 = "Son1.wav"
file9 = "La.wav"
file10 = "Si.wav"
file11 = "Si1.wav"
file12 = "Do2.wav"

wav_file1=wave.open(file1, 'w')
wav_file2=wave.open(file2, 'w')
wav_file3=wave.open(file3, 'w')
wav_file4=wave.open(file4, 'w')
wav_file5=wave.open(file5, 'w')
wav_file6=wave.open(file6, 'w')
wav_file7=wave.open(file7, 'w')
wav_file8=wave.open(file8, 'w')
wav_file9=wave.open(file9, 'w')
wav_file10=wave.open(file10, 'w')
wav_file11=wave.open(file11, 'w')
wav_file12=wave.open(file12, 'w')

nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2

wav_file1.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file2.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file3.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file4.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file5.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file6.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file7.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file8.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file9.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file10.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file11.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
wav_file12.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

for s in sine_waveDo:
    wav_file1.writeframes(struct.pack('h',int(s*amplitude)))
wav_file1.close()

for s in sine_waveDo1:
    wav_file2.writeframes(struct.pack('h',int(s*amplitude)))
wav_file2.close()

for s in sine_waveRe:
    wav_file3.writeframes(struct.pack('h',int(s*amplitude)))
wav_file3.close()

for s in sine_waveMi:
    wav_file4.writeframes(struct.pack('h',int(s*amplitude)))
wav_file4.close()

for s in sine_waveFa:
    wav_file5.writeframes(struct.pack('h',int(s*amplitude)))
wav_file5.close()

for s in sine_waveFa1:
    wav_file6.writeframes(struct.pack('h',int(s*amplitude)))
wav_file6.close()

for s in sine_waveSon:
    wav_file7.writeframes(struct.pack('h',int(s*amplitude)))
wav_file7.close()

for s in sine_waveSon1:
    wav_file8.writeframes(struct.pack('h',int(s*amplitude)))
wav_file8.close()

for s in sine_waveLa:
    wav_file9.writeframes(struct.pack('h',int(s*amplitude)))
wav_file9.close()

for s in sine_waveSi:
    wav_file10.writeframes(struct.pack('h',int(s*amplitude)))
wav_file10.close()

for s in sine_waveSi1:
    wav_file11.writeframes(struct.pack('h',int(s*amplitude)))
wav_file11.close()

for s in sine_waveDo2:
    wav_file12.writeframes(struct.pack('h',int(s*amplitude)))
wav_file12.close()

