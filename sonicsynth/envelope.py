import numpy as np

def generate_adsr_envelope(attack, decay, sustain, release):
    """
    Generate an ADSR envelope.

    Parameters:
    - attack (int): The duration of the attack phase in samples.
    - decay (int): The duration of the decay phase in samples.
    - sustain (float): The sustain level between 0.0 and 1.0.
    - release (int): The duration of the release phase in samples.

    Returns:
    - numpy.ndarray: The generated ADSR envelope as a NumPy array of amplitude values.
    """
    total_duration = attack + decay + release

    # Time points for each phase
    attack_time = np.arange(attack)
    decay_time = np.arange(attack, attack + decay)
    release_time = np.arange(attack + decay, total_duration)

    # Amplitude values for each phase
    attack_amplitude = attack_time / attack
    decay_amplitude = (1 - sustain) * (1 - (decay_time - attack) / decay) + sustain
    sustain_amplitude = np.full(total_duration - attack - decay, sustain)
    release_amplitude = sustain * (1 - (release_time - attack - decay) / release)

    envelope = np.concatenate((attack_amplitude, decay_amplitude, sustain_amplitude, release_amplitude))

    return envelope

def generate_linear_decay_envelope(duration):
    """
    Generate a linear decay envelope.

    Parameters:
    - duration (int): The duration of the decay in samples.

    Returns:
    - numpy.ndarray: The generated linear decay envelope as a NumPy array of amplitude values.
    """
    time = np.arange(duration)
    envelope = 1 - time / duration

    return envelope

def generate_exponential_decay_envelope(duration, decay_factor):
    """
    Generate an exponential decay envelope.

    Parameters:
    - duration (int): The duration of the decay in samples.
    - decay_factor (float): The decay factor between 0.0 and 1.0.

    Returns:
    - numpy.ndarray: The generated exponential decay envelope as a NumPy array of amplitude values.
    """
    time = np.arange(duration)
    envelope = decay_factor ** (time / duration)

    return envelope

def generate_custom_envelope(time_points, amplitude_points):
    """
    Generate a custom envelope based on time and amplitude points.

    Parameters:
    - time_points (list): A list of time points in samples.
    - amplitude_points (list): A list of corresponding amplitude points.

    Returns:
    - numpy.ndarray: The generated custom envelope as a NumPy array of amplitude values.
    """
    envelope = np.repeat(amplitude_points, time_points)

    return envelope