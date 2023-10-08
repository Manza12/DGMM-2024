import sys

from core import *
from core.morphology import greyscale_trimming, reconstruction_dilation
from core.parameters import DEVICE, TIME_RESOLUTION

from procedures.io import load_or_compute
from procedures.plot_pipeline import plot_compare


# Paths
output_folder = Path('.')

arrays_folder = output_folder / Path('arrays')
images_folder = output_folder / Path('images')
arrays_folder.mkdir(parents=True, exist_ok=True)
images_folder.mkdir(parents=True, exist_ok=True)

# Start
start_full = time.time()
print('Horizontal thinning ...')

# Load input spectrogram
spectrogram = load_or_compute('vertical_threshold', arrays_folder, {'vertical_threshold': True},
                              lambda: print('Not found'))

# Morphology
MIN_LENGTH_SINUSOIDS = 0.1  # seconds

min_length_bins = int(MIN_LENGTH_SINUSOIDS / TIME_RESOLUTION)
iterations = min_length_bins // 2

start = time.time()
spectrogram_trimming = greyscale_trimming(spectrogram, iterations, 'h', verbose=True)
torch.cuda.synchronize(DEVICE)
print('Time to trimming: %.3f seconds' % (time.time() - start))

start = time.time()
spectrogram_reconstruction = reconstruction_dilation(spectrogram_trimming, spectrogram)
torch.cuda.synchronize(DEVICE)
print('Time to reconstruction: %.3f seconds' % (time.time() - start))

# End
end_full = time.time()
print('Total time: %.3f s' % (end_full - start_full))
sys.stdout.close()

# Plots
plot_compare(spectrogram, spectrogram_reconstruction, 'vertical_filtered', 'Vertical filtered', images_folder)
plt.show()
