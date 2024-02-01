from core import *
from core.layers import apply_stft_layer
from core.synthesis import synthesize_noise_mask, synthesize_white_noise, synthesize_sinusoids, synthesize_transient
from core.processing import get_lines, filter_lines
from core.utils import get_duration, to_db

from .io import load_or_compute


def synthesize_noise_signal(signals, spectrograms, paths, load):
    print('\nSynthesis - Noise')

    n = signals['input'].size

    # White noise
    white_noise = load_or_compute('white_noise', paths['arrays_folder'], load, lambda: synthesize_white_noise(n))

    white_noise_stft = apply_stft_layer(white_noise, verbose=True, output_format='Complex', input_name='white noise')

    # Noise
    filtered_noise = load_or_compute('filtered_noise', paths['audio_folder'], load,
                                     lambda: synthesize_noise_mask(white_noise_stft, spectrograms['opening'],
                                                                   verbose=True),
                                     extension='.wav')

    signals['white_noise'] = white_noise
    signals['filtered_noise'] = filtered_noise

    spectrogram_white_noise = to_db(np.sqrt(np.abs(white_noise_stft)**2))
    spectrogram_filtered_noise = apply_stft_layer(filtered_noise, verbose=True, input_name='filtered noise')

    spectrograms['white_noise'] = spectrogram_white_noise
    spectrograms['filtered_noise'] = spectrogram_filtered_noise


def synthesize_sinusoids_signal(lines, signals, spectrograms, paths, load):
    print('\nSynthesis - Sinusoids')

    lines_sinusoids = load_or_compute('lines_sinusoids', paths['arrays_folder'], load,
                                      lambda: get_lines(spectrograms['horizontal_filtered'], 'time'))
    filtered_lines = filter_lines(lines_sinusoids, 1)
    lines['sinusoids'] = lines_sinusoids
    lines['filtered_sinusoids'] = filtered_lines

    sinusoids = load_or_compute('sinusoids', paths['audio_folder'], load,
                                lambda: synthesize_sinusoids(filtered_lines), extension='.wav')

    signals['sinusoids'] = sinusoids

    spectrogram_sinusoids = apply_stft_layer(sinusoids, verbose=True, input_name='sinusoids')

    spectrograms['sinusoids'] = spectrogram_sinusoids


def synthesize_transient_signal(lines, signals, spectrograms, paths, load):
    print('\nSynthesis - Transient')

    lines_transient = load_or_compute('lines_transient', paths['arrays_folder'], load,
                                      lambda: get_lines(spectrograms['vertical_filtered'], 'frequency'))
    filtered_lines = filter_lines(lines_transient, 0)
    lines['transient'] = lines_transient
    lines['filtered_transient'] = filtered_lines

    duration = get_duration(signals['input'])
    transient = load_or_compute('transient', paths['audio_folder'], load,
                                lambda: synthesize_transient(filtered_lines, duration), extension='.wav')

    signals['transient'] = transient

    spectrogram_transient = apply_stft_layer(transient, verbose=True, input_name='transient')

    spectrograms['transient'] = spectrogram_transient


def synthesize_output_signal(signals, spectrograms):
    filtered_noise = signals.get('filtered_noise', np.zeros_like(signals['input']))
    sinusoids = signals.get('sinusoids', np.zeros_like(signals['input']))
    transient = signals.get('transient', np.zeros_like(signals['input']))

    print('\nSynthesis - Output')
    output_size = max(len(filtered_noise), len(sinusoids), len(transient))
    denoised_size = max(len(sinusoids), len(transient))

    output = np.zeros(output_size, dtype=np.float32)
    denoised = np.zeros(denoised_size, dtype=np.float32)

    output[:filtered_noise.size] += filtered_noise
    output[:sinusoids.size] += sinusoids
    denoised[:sinusoids.size] += sinusoids
    output[:transient.size] += transient
    denoised[:transient.size] += transient

    signals['output'] = output
    signals['denoised'] = denoised

    spectrogram_output = apply_stft_layer(output, verbose=True, input_name='output')
    spectrogram_denoised = apply_stft_layer(denoised, verbose=True, input_name='denoised')

    spectrograms['output'] = spectrogram_output
    spectrograms['denoised'] = spectrogram_denoised


def synthesize_signals(lines, signals, spectrograms, paths, load, components):
    if components['noise']:
        synthesize_noise_signal(signals, spectrograms, paths, load)
    if components['sinusoids']:
        synthesize_sinusoids_signal(lines, signals, spectrograms, paths, load)
    if components['transient']:
        synthesize_transient_signal(lines, signals, spectrograms, paths, load)
    if components['output']:
        synthesize_output_signal(signals, spectrograms)
