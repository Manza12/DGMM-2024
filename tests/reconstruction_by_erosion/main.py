import sys

from core import *
from core.layers import create_stft_layer, apply_stft_layer
from core.morphology import erosion_geodesic
from core.processing import apply_closing_transient
from core.parameters import DEVICE

from procedures.io import load_or_compute, take_excerpt
from procedures.plot_pipeline import plot_compare

import settings as run_settings

# Parameters
name = 'anastasia'
settings = getattr(run_settings, name)
paper = False

# Paths
project_folder = Path('..') / Path('..')

data_folder = project_folder / Path('data')

audio_folder = data_folder / Path('audio')
objects_folder = data_folder / Path('objects')

output_folder = Path('.')

arrays_folder = output_folder / Path('arrays')
images_folder = output_folder / Path('images')
arrays_folder.mkdir(parents=True, exist_ok=True)
images_folder.mkdir(parents=True, exist_ok=True)

# Start
start_full = time.time()
print('Reconstruction by erosion of ' + name + '...\n')

# Read wav file
print('Getting input...')

file_path = audio_folder / (name + '.wav')

start = settings['start']
end = settings['end']
x = take_excerpt(file_path, start, end)

# Create STFT layer
stft_layer = load_or_compute('stft_layer', objects_folder, {}, create_stft_layer)

# Apply STFT layer
spectrogram = load_or_compute('spectrogram', arrays_folder, {}, lambda: apply_stft_layer(x, stft_layer))

# Morphology - reconstruction by erosion
# spectrogram_reconstruction_erosion = apply_reconstruction_by_erosion(spectrogram)

# marker = torch.clone(spectrogram)
marker = apply_closing_transient(spectrogram)
# marker[200: 400, 500: 1000] = 0
x_recons = torch.clone(marker)

verbose_it_step = 100
count = 0
start = time.time()
while True:
    x_out = erosion_geodesic(x_recons, spectrogram)

    if count % verbose_it_step == 0:
        print("it:", count)

        # plot_compare(spectrogram, x_out, 'reconstruction_erosion', 'Reconstruction by erosion', images_folder)
        # plt.show()

    if torch.all(torch.eq(x_out, x_recons)):
        break
    else:
        x_recons = x_out
    count += 1

torch.cuda.synchronize(DEVICE)
print('Time to apply reconstruction by erosion: %.3f seconds' % (time.time() - start))
print('Count =', count)


# End
end_full = time.time()
print('Total time: %.3f s' % (end_full - start_full))
sys.stdout.close()

# Plots
plot_compare(spectrogram, marker, 'closing', 'Closing', images_folder)
plot_compare(marker, x_out, 'reconstruction_erosion', 'Reconstruction by erosion', images_folder)
plot_compare(spectrogram, x_out, 'input_output', 'Output', images_folder)
plt.show()
