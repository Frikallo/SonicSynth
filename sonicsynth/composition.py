import numpy as np

def mix_tracks(*waveforms, volume=1.0, panning=0.0):
    """
    Mix multiple audio tracks.

    Args:
        *waveforms (ndarray): Variable number of input waveforms.
        volume (float): Overall volume level for the mixed tracks. Default is 1.0.
        panning (float): Panning value for the mixed tracks. Range: -1.0 (left) to 1.0 (right). Default is 0.0.

    Returns:
        ndarray: The mixed waveform.

    """
    # Ensure all waveforms have the same length
    waveform_length = min(len(waveform) for waveform in waveforms)
    
    # Adjust the panning for stereo mixing
    panning = np.clip(panning, -1.0, 1.0)
    left_volume = np.sqrt(0.5 * (1.0 - panning))
    right_volume = np.sqrt(0.5 * (1.0 + panning))
    
    mixed_waveform = np.zeros(waveform_length)
    
    for waveform in waveforms:
        waveform = adjust_track_volume(waveform, volume)
        waveform = pan_track(waveform, left_volume, right_volume)
        mixed_waveform += waveform[:waveform_length]
    
    return mixed_waveform


def adjust_track_volume(waveform, volume):
    """
    Adjusts the volume of a track represented by a waveform.

    Args:
        waveform (numpy.ndarray): The waveform of the track.
        volume (float or numpy.ndarray): The volume adjustment factor(s).

    Returns:
        numpy.ndarray: The waveform with adjusted volume.
    """
    return waveform * volume


def pan_track(waveform, left_volume, right_volume):
    """
    Pan an audio track.

    Args:
        waveform (ndarray): The input waveform.
        left_volume (float): The volume level for the left channel.
        right_volume (float): The volume level for the right channel.

    Returns:
        ndarray: The waveform with panning applied.

    """
    left_channel = waveform * left_volume
    right_channel = waveform * right_volume
    return np.column_stack((left_channel, right_channel)).flatten()


def apply_track_timing(waveform, time_shift):
    """
    Apply timing adjustments to an audio track.

    Args:
        waveform (ndarray): The input waveform.
        time_shift (int): The time shift in number of samples.

    Returns:
        ndarray: The waveform with timing adjustments.

    """
    return np.roll(waveform, time_shift)

