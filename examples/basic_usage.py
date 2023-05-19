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