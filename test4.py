import soundcard as sc
import numpy as np
import scipy.io.wavfile as wav

samplerate = 44100
duration = 5  # seconds
frames = samplerate * duration

# Get mic and loopback devices
microphones = sc.all_microphones(include_loopback=True)

mic_device = None
loopback_device = None

for mic in microphones:
    if mic.isloopback and loopback_device is None:
        loopback_device = mic
    elif not mic.isloopback and mic.name.lower().startswith("built-in") and mic_device is None:
        mic_device = mic

if mic_device is None or loopback_device is None:
    raise RuntimeError("Mic or system audio (loopback) device not found.")

print(f"Using mic: {mic_device.name}")
print(f"Using system audio: {loopback_device.name}")

# Record simultaneously
print("Recording mic and system audio...")
mic_audio = mic_device.record(numframes=frames, samplerate=samplerate)
sys_audio = loopback_device.record(numframes=frames, samplerate=samplerate)

# Option 1: Save them separately
wav.write("mic_audio.wav", samplerate, mic_audio)
wav.write("system_audio.wav", samplerate, sys_audio)

# Option 2: Combine into stereo file: [Left: mic, Right: system]
stereo_audio = np.stack([mic_audio[:, 0], sys_audio[:, 0]], axis=1)
wav.write("combined_stereo.wav", samplerate, stereo_audio)

print("Done. Files saved:")
print("  mic_audio.wav")
print("  system_audio.wav")
print("  combined_stereo.wav")
