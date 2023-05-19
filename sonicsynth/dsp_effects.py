import numpy as np

def apply_low_pass_filter(waveform, cutoff_frequency):
    """
    Apply a low-pass filter to a waveform.

    Args:
        waveform (ndarray): The input waveform.
        cutoff_frequency (float): The cutoff frequency of the filter.

    Returns:
        ndarray: The filtered waveform.

    """
    spectrum = np.fft.fft(waveform)
    frequencies = np.fft.fftfreq(len(waveform))
    spectrum[frequencies > cutoff_frequency] = 0
    return np.real(np.fft.ifft(spectrum))


def apply_high_pass_filter(waveform, cutoff_frequency):
    """
    Apply a high-pass filter to a waveform.

    Args:
        waveform (ndarray): The input waveform.
        cutoff_frequency (float): The cutoff frequency of the filter.

    Returns:
        ndarray: The filtered waveform.

    """
    spectrum = np.fft.fft(waveform)
    frequencies = np.fft.fftfreq(len(waveform))
    spectrum[frequencies < cutoff_frequency] = 0
    return np.real(np.fft.ifft(spectrum))


def apply_band_pass_filter(waveform, center_frequency, bandwidth):
    """
    Apply a band-pass filter to a waveform.

    Args:
        waveform (ndarray): The input waveform.
        center_frequency (float): The center frequency of the filter.
        bandwidth (float): The bandwidth of the filter.

    Returns:
        ndarray: The filtered waveform.

    """
    spectrum = np.fft.fft(waveform)
    frequencies = np.fft.fftfreq(len(waveform))
    spectrum[np.abs(frequencies - center_frequency) > bandwidth / 2] = 0
    return np.real(np.fft.ifft(spectrum))


def apply_delay(waveform, delay_time, feedback, sample_rate=44100):
    """
    Apply a delay effect to a waveform.

    Args:
        waveform (ndarray): The input waveform.
        delay_time (float): The delay time in seconds.
        feedback (float): The amount of feedback.
        sample_rate (int): The sample rate of the waveform in Hz. Defaults to 44100.

    Returns:
        ndarray: The delayed waveform.

    """
    num_samples = int(delay_time * sample_rate)
    delay_buffer = np.zeros(num_samples)
    output = np.zeros(len(waveform))
    
    for i in range(len(waveform)):
        output[i] = waveform[i] + feedback * delay_buffer[0]
        delay_buffer = np.roll(delay_buffer, 1)
        delay_buffer[0] = output[i]
    
    return output


def apply_reverb(waveform, decay_time, mix, sample_rate=44100):
    """
    Apply a reverb effect to a waveform.

    Args:
        waveform (ndarray): The input waveform.
        decay_time (float): The decay time in seconds.
        mix (float): The wet/dry mix ratio.
        sample_rate (int): The sample rate of the waveform in Hz. Defaults to 44100.

    Returns:
        ndarray: The reverberated waveform.

    """
    num_samples = int(decay_time * sample_rate)
    reverb = np.zeros(num_samples)
    output = np.zeros(len(waveform))
    
    for i in range(len(waveform)):
        output[i] = waveform[i] + mix * reverb[0]
        reverb = np.roll(reverb, 1)
        reverb[0] = output[i] * (1 - mix)
    
    return output


def apply_modulation(waveform, modulation_frequency, modulation_type, sample_rate=44100):
    """
    Apply a modulation effect to a waveform.

    Args:
        waveform (ndarray): The input waveform.
        modulation_frequency (float): The modulation frequency.
        modulation_type (str): The modulation type ('amplitude' or 'frequency').
        sample_rate (int): The sample rate of the waveform in Hz. Defaults to 44100.

    Returns:
        ndarray: The modulated waveform.

    """
    time = np.arange(len(waveform)) / sample_rate
    modulation = np.sin(2 * np.pi * modulation_frequency * time)
    
    if modulation_type == 'amplitude':
        return waveform * modulation
    elif modulation_type == 'frequency':
        return waveform * np.cos(2 * np.pi * modulation_frequency * time)
    else:
        raise ValueError("Invalid modulation type. Supported types are 'amplitude' and 'frequency'.")