"""
Found on http://milkandtang.com/blog/2013/02/16/making-noise-in-python/

(sudo zypper install python-PyAudio # for python2)

python3-PyAudio from software.opensuse.org
"""

import math
import numpy
import pyaudio
import time
import threading

class SineNote:
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.play_tone(10, 0.2) # to avoid premature termination of sound
        self.stream.close()
        self.pa.terminate()

    def _sine(self, frequency, length, rate):
        length = int(length * rate)
        factor = float(frequency) * (math.pi * 2) / rate
        return numpy.sin(numpy.arange(length) * factor)

    def _play_tone(self, stream, frequency=440, length=1, rate=44100):
        chunks = []
        chunks.append(self._sine(frequency, length, rate))
        chunk = numpy.concatenate(chunks) * 0.25
        self.stream.write(chunk.astype(numpy.float32).tostring())

    def play_tone(self, frequency=440, length=1):
        self._play_tone(self.stream, frequency, length)

def aprint(text):
    #t = threading.Thread(target=print, args=(text))
    #t.start()
    #print(text)
    pass

if __name__ == '__main__':

    with SineNote() as sn:
        # sn.play_tone()

        for x in range(0, 30):
            sn.play_tone(500 * (x % 15), 0.05)

        freq = { 'G4': 391.995, 'G#4': 415.305,
            'A4': 440,
            'A#4': 466.164, 'B4': 493.883, 'C5': 523.251, 'C#5': 554.365,
            'D5': 500, 'D#5': 500, 'E5': 500, 'F5': 500, 'F#5': 500, 'G5': 500, 'G#5': 500, # todo
            'A5': 880,
            'A#5': 500, # todo
            'B5': 987.767, 'C6': 1046.50, 'C#6': 1108.73, 'D6': 1174.66, 'D#6': 1244.51, 'E6': 1318.51, 'F6': 1396.91, 'F#6': 1479.98, 'G6': 1567.98, 'G#6': 1661.22,
            'A6': 1760.00
        }

        # http://www.answers.com/Q/What_are_the_notes_for_Tetris_on_piano
        tetris_line1 = 'E6 B5 C6 D6 C6 B5 A5 A5 C6 E6 D6 C6 B5 C6 D6 E6 C6 A5 A5'
        tetris_line2 = 'D6 F6 A6 G6 F6 E6 C6 E6 D6 C6 B5 B5 C6 D6 E6 C6 A5 A5'

        tetris_line1 = 'E6:1 B5:2 C6:2 D6:1 C6:2 B5:2 A5:1 A5:2 C6:2 E6:1 D6:2 C6:2 B5:1 C6:2 D6:2 E6:1 C6:2 A5:2 A5:2'
        tetris_line2 = 'D6:1 F6:2 A6:1 G6:2 F6:2 E6:1 C6:2 E6:2 D6:2 C6:2 B5:1 B5:2 C6:2 D6:2 E6:2 C6:2 A5:2 A5:1'

        for n in (tetris_line1 + ' ' + tetris_line2).split():

            # print(n) # http://stackoverflow.com/questions/14601666/alsa-ways-to-prevent-underrun-for-speaker
            aprint(n)

            (t, w) = n.split(':')
            w = float(w)
            sn.play_tone(freq[t], 0.4 * 1/w)
            sn.play_tone(0.1, 0.02)
            #time.sleep(0.5) # http://stackoverflow.com/questions/14189253/pyaudio-behavior-during-time-sleep

        #sn.play_tone()
