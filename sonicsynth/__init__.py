from .wave_generator import (generate_cosine_wave, generate_sine_wave, generate_square_wave, generate_triangle_wave, generate_sawtooth_wave, generate_custom_wave)
from .envelope import (generate_adsr_envelope, generate_exponential_decay_envelope, generate_linear_decay_envelope, generate_custom_envelope)
from .dsp_effects import (apply_band_pass_filter, apply_high_pass_filter, apply_low_pass_filter, apply_delay, apply_reverb, apply_modulation)
from .composition import (adjust_track_volume, apply_track_timing, mix_tracks, pan_track)
from .playback import Playback
from .export import (export_audio, set_channels)

__version__ = '1.0.0'