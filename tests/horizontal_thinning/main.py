import sys

from core import *
from core.morphology import elementary_greyscale_sequential_thinning
from core.parameters import DEVICE

from procedures.io import load_or_compute
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
print('Horizontal thinning of ' + name + '...\n')

# Load input spectrogram
spectrogram = load_or_compute('reconstruction_erosion', arrays_folder, {'reconstruction_erosion': True},
                              lambda: print('Not found'))

x_thin = torch.clone(spectrogram)
count = 0
verbose_it_step = 10
start = time.time()
while True:
    if count % verbose_it_step == 0:
        print("it:", count)
        plot_compare(spectrogram, x_thin, 'horizontal_thinning_%d' % count, 'Horizontal thinning', images_folder)
        plt.show()

    x_out = elementary_greyscale_sequential_thinning(x_thin, 'h', alpha=0)

    if torch.all(torch.eq(x_out, x_thin)):
        break
    else:
        x_thin = x_out
    count += 1

print("Iterations needed for stability:", count)

torch.cuda.synchronize(DEVICE)
print('Time to apply horizontal thinning: %.3f seconds' % (time.time() - start))


# End
end_full = time.time()
print('Total time: %.3f s' % (end_full - start_full))
sys.stdout.close()

# Plots
plot_compare(spectrogram, x_thin, 'horizontal_thinning', 'Horizontal thinning', images_folder)
plt.show()
