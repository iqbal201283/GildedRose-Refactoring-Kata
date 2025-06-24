import sounddevice as sd
import soundfile as sf
import numpy as np

samplerate = 44100
duration = 100  # seconds
channels = 1

# Replace with actual names from `pactl list short sources`
# mic_source = 'alsa_input.pci-0000_00_1f.3.analog-stereo'
# loopback_source = 'alsa_output.pci-0000_00_1f.3.analog-stereo.monitor'
loopback_source = 'alsa_input.pci-0000_00_1f.3.analog-stereo'
# Set default input device for mic
# sd.default.device = (mic_source, None)
# sd.default.device = ('4', None)  # or use actual index from `query_devices()`
# You can also use the index instead of name
device_name = "alsa_output.pci-0000_00_1f.3.analog-stereo.monitor"

sd.default.device = (None, device_name)  # (input_device, output_device)

print("Recording mic...")
# mic_audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels)
mic_audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels)

sd.wait()

# Set default input device for system audio
sd.default.device = (None, loopback_source)

print("Recording system audio...")
system_audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels)
sd.wait()

# Save individual files
sf.write("mic_audio.wav", mic_audio, samplerate)
sf.write("system_audio.wav", system_audio, samplerate)

# Optionally mix both
mixed = mic_audio + system_audio
sf.write("mixed_audio.wav", mixed, samplerate)

print("Done. Saved all files.")
