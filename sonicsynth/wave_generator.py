import numpy as np

def generate_cosine_wave(frequency, amplitude, duration, sample_rate=44100):
    """
    Generate a cosine waveform with the given frequency, amplitude, and duration.

    Args:
        frequency (float): The frequency of the waveform in Hz.
        amplitude (float): The amplitude of the waveform.
        duration (float): The duration of the waveform in seconds.
        sample_rate (int): The sample rate of the waveform in Hz. Defaults to 44100.

    Returns:
        ndarray: An array representing the generated waveform.
    """
    # Time axis
    t = np.linspace(0, duration, int(sample_rate * duration))
    # Cosine wave
    cosine_wave = np.cos(2 * np.pi * frequency * t)
    # Scale the waveform by the desired amplitude
    cosine_wave *= amplitude
    return cosine_wave

def generate_sine_wave(frequency, amplitude, duration, sample_rate=44100):
    """
    Generate a sine waveform with the given frequency, amplitude, and duration.

    Args:
        frequency (float): The frequency of the waveform in Hz.
        amplitude (float): The amplitude of the waveform.
        duration (float): The duration of the waveform in seconds.
        sample_rate (int): The sample rate of the waveform in Hz. Defaults to 44100.

    Returns:
        ndarray: An array representing the generated waveform.
    """
    # Time axis
    t = np.linspace(0, duration, int(sample_rate * duration))
    # Sine wave
    sine_wave = np.sin(2 * np.pi * frequency * t)
    # Scale the waveform by the desired amplitude
    sine_wave *= amplitude
    return sine_wave

def generate_square_wave(frequency, amplitude, duration, sample_rate=44100):
    """
    Generate a square waveform with the given frequency, amplitude, and duration.

    Args:
        frequency (float): The frequency of the waveform in Hz.
        amplitude (float): The amplitude of the waveform.
        duration (float): The duration of the waveform in seconds.
        sample_rate (int): The sample rate of the waveform in Hz. Defaults to 44100.

    Returns:
        ndarray: An array representing the generated waveform.
    """
    # Time axis
    t = np.linspace(0, duration, int(sample_rate * duration))
    # Square wave
    square_wave = np.sign(np.sin(2 * np.pi * frequency * t))
    # Scale the waveform by the desired amplitude
    square_wave *= amplitude
    return square_wave

def generate_triangle_wave(frequency, amplitude, duration, sample_rate=44100):
    """
    Generate a triangle waveform with the given frequency, amplitude, and duration.

    Args:
        frequency (float): The frequency of the waveform in Hz.
        amplitude (float): The amplitude of the waveform.
        duration (float): The duration of the waveform in seconds.
        sample_rate (int): The sample rate of the waveform in Hz. Defaults to 44100.

    Returns:
        ndarray: An array representing the generated waveform.
    """    
    # Time axis
    t = np.linspace(0, duration, int(sample_rate * duration))
    # Triangle wave
    triangle_wave = 2 * np.abs((2 * frequency * t) % 2 - 1) - 1
    # Scale the waveform by the desired amplitude
    triangle_wave *= amplitude
    return triangle_wave

def generate_sawtooth_wave(frequency, amplitude, duration, sample_rate=44100):    
    """
    Generate a sawtooth waveform with the given frequency, amplitude, and duration.

    Args:
        frequency (float): The frequency of the waveform in Hz.
        amplitude (float): The amplitude of the waveform.
        duration (float): The duration of the waveform in seconds.
        sample_rate (int): The sample rate of the waveform in Hz. Defaults to 44100.

    Returns:
        ndarray: An array representing the generated waveform.
    """
    # Time axis
    t = np.linspace(0, duration, int(sample_rate * duration))
    # Sawtooth wave
    sawtooth_wave = 2 * (frequency * t - np.floor(0.5 + frequency * t))
    # Scale the waveform by the desired amplitude
    sawtooth_wave *= amplitude
    return sawtooth_wave

def generate_custom_wave(waveform, frequency, amplitude, duration, sample_rate=44100):
    """
    Generate a custom waveform with the given frequency, amplitude, and duration.

    Args:
        waveform (array-like): An array-like object representing the custom waveform.
        frequency (float): The frequency of the waveform in Hz.
        amplitude (float): The amplitude of the waveform.
        duration (float): The duration of the waveform in seconds.
        sample_rate (int): The sample rate of the waveform in Hz. Defaults to 44100.

    Returns:
        ndarray: An array representing the generated waveform.
    """
    num_samples = int(duration * sample_rate)
    
    # Calculate the number of cycles required to generate the desired duration
    num_cycles = int(frequency * duration)

    # Repeat the waveform table to cover the desired duration
    waveform = np.tile(waveform, num_cycles)

    # Adjust the length of the waveform to match the desired duration
    waveform = waveform[:num_samples]

    # Scale the waveform by the desired amplitude
    waveform *= amplitude

    return waveform