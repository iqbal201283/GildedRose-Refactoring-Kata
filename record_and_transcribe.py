import sounddevice as sd
import numpy as np
import whisper
import tempfile
import scipy.io.wavfile

# Settings
samplerate = 16000  # Whisper prefers 16kHz
duration = 5        # seconds of audio per chunk
channels = 1        # mono

model = whisper.load_model("base")

def record_and_transcribe():
    print(f"🎤 Recording for {duration} seconds...")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()

    # Save to a temporary WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as tmpfile:
        scipy.io.wavfile.write(tmpfile.name, samplerate, audio)
        result = model.transcribe(tmpfile.name)
        print("📝 Transcription:", result["text"])

while True:
    try:
        record_and_transcribe()
    except KeyboardInterrupt:
        print("⏹️ Stopped.")
        break
