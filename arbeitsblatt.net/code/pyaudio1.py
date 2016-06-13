"""
Found on http://milkandtang.com/blog/2013/02/16/making-noise-in-python/

sudo zypper install python-PyAudio # for python2

python3-PyAudio from software.opensuse.org



"""
import math
import numpy
import pyaudio


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def play_tone(stream, frequency=440, length=1, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))

    chunk = numpy.concatenate(chunks) * 0.25

    stream.write(chunk.astype(numpy.float32).tostring())


if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)

    play_tone(stream)

    for x in range(0, 45):
        play_tone(stream, 500 * (x % 15), 0.05)

    play_tone(stream)

    stream.close()
    p.terminate()


