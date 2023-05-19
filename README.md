# SonicSynth

SonicSynth is an audio synthesis library that provides a high-level interface for generating and manipulating various types of sounds. It allows users to create custom sound waves, apply digital signal processing (DSP) effects, and export the synthesized audio data to various audio file formats.

## Key Features

- **Sound Wave Generation**: Generate different types of sound waves, such as sine, square, triangle, and sawtooth waves, with control over frequency, amplitude, and phase.
- **Envelope Generation**: Create amplitude envelopes, including ADSR (Attack, Decay, Sustain, Release), to shape the volume contour of sounds over time.
- **Digital Signal Processing (DSP) Effects**: Apply filters, delays, reverbs, modulation effects, and more to manipulate the synthesized audio.
- **Multi-track Composition**: Combine multiple sound waves or synthesized audio segments to create multi-track compositions, with control over volume, panning, and timing.
- **Real-time Audio Playback**: Listen to the synthesized audio in real-time, facilitating interactive sound design and experimentation.
- **Audio Export**: Export the synthesized audio data to common audio file formats such as WAV, MP3, and OGG.
- **Comprehensive Documentation and Examples**: Detailed documentation and examples are provided to help users quickly get started and explore SonicSynth's capabilities.

## Installation

You can install SonicSynth using `pip`:

```shell
pip install sonicsynth
```

## Usage
```python
import sonicsynth

# Generate a sine wave
waveform = sonicsynth.generate_sine_wave(frequency=440, amplitude=0.5, duration=2)

# Apply a low-pass filter
filtered_wave = sonicsynth.apply_low_pass_filter(waveform, cutoff_frequency=1000)

# Create a multi-track composition
track1 = sonicsynth.mix_tracks(waveform, filtered_wave, volume=0.8, panning=0.5)

# Play the synthesized audio
player = sonicsynth.Playback(44100)
player.play(track1)

# Export the audio to a WAV file
sonicsynth.export_audio(track1, filename="output.wav", format="wav")
```

