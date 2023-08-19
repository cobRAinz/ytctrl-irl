#!/usr/bin/env python3
#import noisereduce as nr
import argparse
import wavio
import sounddevice as sd
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)
filename = "output.wav"
duration = 30
index = 0
samplerate = 44100
channels=2

buffer = numpy.empty((samplerate * duration, channels), dtype=numpy.int16)

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    print(outdata.shape)
    outdata[:, 0] = indata[:, 0]
    #outdata[:, 1] = 0
    global index
    buffer[index:index+frames] = indata * (2**15)  # Convert float to int16
    index += frames
    #print(len(buffer[buffer != 0]))

try:
    with sd.Stream(device=(None, None), channels=2, callback=callback):
        print('#' * 80)
        print('press Return to quit')
        print('#' * 80)
        #input()
        while True:
            if input() == "q":
                wavio.write(filename, buffer[:index], samplerate, sampwidth=2)
                print("written")
except Exception as e:
    print(e)
