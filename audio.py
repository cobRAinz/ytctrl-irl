import pyaudio
import wave
from pynput import keyboard
import time

pressed = False
def on_press(key):
    global pressed
    print("AHHHH")
    pressed = True

listener = keyboard.Listener(
    on_press=on_press)

listener.start()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output_p_test.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

while not pressed:
    time.sleep(1)
    data = stream.read(CHUNK)
    frames.append(data)

print(len(frames))
print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

