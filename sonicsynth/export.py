import numpy as np
import soundfile as sf

def export_audio(waveform, filename, format, sample_rate=44100):
    """
    Exports the synthesized audio waveform to the specified audio file format.

    Args:
        waveform (numpy.ndarray): The audio waveform as a NumPy array.
        filename (str, optional): The output filename.
        format (str, optional): The audio file format.
        sample_rate (int, optional): The sample rate in Hz. Defaults to 44100.

    Raises:
        ValueError: If the specified format is not supported.

    Returns:
        None
    """
    try:
        sf.write(file=filename, data=waveform, format=format, samplerate=sample_rate)
    except ValueError:
        raise ValueError("Specified format is not supported.")

def set_channels(waveform, num_channels):
    """
    Set the number of channels for a waveform.

    Args:
        waveform (ndarray): The waveform array.
        num_channels (int): The desired number of channels.

    Returns:
        ndarray: The waveform with the specified number of channels.

    Raises:
        ValueError: If the number of channels is not a positive integer.

    """
    if not isinstance(num_channels, int) or num_channels <= 0:
        raise ValueError("Number of channels must be a positive integer.")

    # Reshape the waveform array to the specified number of channels
    return np.reshape(waveform, (-1, num_channels))