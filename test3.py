import soundcard as sc
import numpy as np
import scipy.io.wavfile as wav

samplerate = 44100
duration = 30  # seconds

# Step 1: Get all microphones including loopbacks
mics = sc.all_microphones(include_loopback=True)

# Step 2: Choose the default speaker's loopback mic
loopback_mic = None
for mic in mics:
    if mic.isloopback:
        loopback_mic = mic
        break

if loopback_mic is None:
    raise RuntimeError("No loopback device found. Make sure you're using PulseAudio or PipeWire.")

# Step 3: Record from loopback
print(f"Recording from: {loopback_mic.name}")
audio_data = loopback_mic.record(samplerate=samplerate, numframes=samplerate * duration)

# Step 4: Save to WAV file
wav.write("system_audio.wav", samplerate, audio_data)
print("Recording complete. Saved to system_audio.wav")
