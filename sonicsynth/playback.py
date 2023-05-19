import pyaudio
import numpy as np

class Playback:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def open_stream(self):
        self.stream = self.audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.sample_rate,
            output=True
        )

    def close_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()

    def play(self, waveform):
        self.open_stream()
        self.stream.write(waveform.astype(np.float32).tostring())
        self.close_stream()

    def stop(self):
        self.close_stream()
        self.audio.terminate()