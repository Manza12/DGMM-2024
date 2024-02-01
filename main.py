import sys

from core import *
from core.layers import apply_stft_layer
from core.parameters import TIME_RESOLUTION, FREQUENCY_PRECISION, WINDOW

from procedures.io import load_or_compute, write_signals, take_excerpt
from procedures.morphological_pipeline import apply_morphology
from procedures.plot_pipeline import plot_all
from procedures.synthesis import synthesize_signals

import settings as run_settings

# Parameters
name = 'piano'
settings = getattr(run_settings, name)
load_any = True
log = False

components = {
    'input': True,
    'noise': True,
    'sinusoids': True,
    'transient': True,
    'output': True,
    'denoised': False,
}

operations = {
    'processing': True,
    'synthesis': True,
    'signals': True,
    'plots': True,
}

layer_name = 'stft_layer_%d_ms_%d_Hz_%s' % (TIME_RESOLUTION * 1000, FREQUENCY_PRECISION, WINDOW)
if load_any:
    load = {
        # STFT Layer
        layer_name: True,

        # Input
        'spectrogram': True,
        'closing': True,
        'reconstruction_erosion': True,

        # Noise
        'white_noise': True,
        'opening': True,
        'filtered_noise': True,

        # Sinusoids
        'vertical_thin': True,
        'vertical_top_hat': True,
        'vertical_threshold': True,

        'horizontal_filtered': False,
        'lines_sinusoids': False,
        'sinusoids': False,

        # Transient
        'horizontal_thin': True,
        'horizontal_top_hat': True,
        'horizontal_threshold': True,

        'vertical_filtered': False,
        'lines_transient': False,
        'transient': False,
    }
else:
    load = {}

# Paths
project_folder = Path('.')

data_folder = project_folder / Path('data')

audio_folder = data_folder / Path('audio')
objects_folder = data_folder / Path('objects')

results_folder = project_folder / Path('results')

output_folder = results_folder / Path(name + '_%dms_%dHz' % (TIME_RESOLUTION * 1000, FREQUENCY_PRECISION))

arrays_folder = output_folder / Path('arrays')
images_folder = output_folder / Path('images')

paths = {
    'project_folder': project_folder,
    'results_folder': results_folder,
    'output_folder': output_folder,
    'arrays_folder': arrays_folder,
    'images_folder': images_folder,
    'audio_folder': audio_folder,
    'objects_folder': objects_folder,
}

paths['objects_folder'].mkdir(parents=True, exist_ok=True)
paths['output_folder'].mkdir(parents=True, exist_ok=True)
paths['arrays_folder'].mkdir(parents=True, exist_ok=True)
paths['images_folder'].mkdir(parents=True, exist_ok=True)

# Log
if log:
    log_path = paths['output_folder'] / 'log.txt'
    sys.stdout = open(log_path, 'w')

# Start
start_full = time.time()
print('Analyzing ' + name + '...\n')

# Read wav file
print('Getting input...')

paths['file_path'] = paths['audio_folder'] / (name + '.wav')

start = settings.get('start', 0.)
end = settings.get('end', None)
x = take_excerpt(paths['file_path'], start, end)

# Apply STFT layer
spectrogram = load_or_compute('spectrogram', paths['arrays_folder'], load, lambda: apply_stft_layer(x))

# Morphology
spectrograms = {'input': spectrogram}
parameters = settings.get('parameters', {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    })
if operations['processing']:
    print('\nProcessing...')
    apply_morphology(spectrograms, paths, load, components, parameters)

# Synthesis
signals = {'input': x}
lines = {}
if operations['synthesis']:
    print('\nSynthesis...')
    synthesize_signals(lines, signals, spectrograms, paths, load, components)

    # Write signals
    write_signals(signals, paths, components)

# End
end_full = time.time()
print('Total time: %.3f s' % (end_full - start_full))
sys.stdout.close()

# Plots
if operations['plots']:
    plot_all(lines, spectrograms, components, paths, settings)
