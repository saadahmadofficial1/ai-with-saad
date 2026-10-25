"""Text to speech with Kokoro (ONNX). Usage: python speak.py "Your script here" """
import sys
import soundfile as sf
from kokoro_onnx import Kokoro

text = " ".join(sys.argv[1:]) or "This free AI voice sounds human."
kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
audio, sample_rate = kokoro.create(text, voice="am_michael", speed=1.05, lang="en-us")
sf.write("voice.wav", audio, sample_rate)
print("Saved voice.wav")
