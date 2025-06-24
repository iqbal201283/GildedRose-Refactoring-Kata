import sounddevice as sd

samplerate = 44100
duration = 5  # seconds
channels = 1

# You can also use the index instead of name
device_name = "alsa_output.pci-0000_00_1f.3.analog-stereo.monitor"

sd.default.device = (None, device_name)  # (input_device, output_device)

print("Recording system audio...")
system_audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels)
sd.wait()
import soundfile as sf
sf.write("system_audio.wav", system_audio, samplerate)
print("Done.")
