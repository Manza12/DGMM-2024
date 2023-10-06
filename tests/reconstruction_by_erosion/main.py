import sys

from core import *
from core.morphology import erosion_geodesic
from core.processing import apply_closing
from core.parameters import DEVICE

from procedures.io import load_or_compute
from procedures.plot_pipeline import plot_compare


# Parameters
plot = False

# Paths
output_folder = Path('.')

arrays_folder = output_folder / Path('arrays')
images_folder = output_folder / Path('images')
arrays_folder.mkdir(parents=True, exist_ok=True)
images_folder.mkdir(parents=True, exist_ok=True)

# Start
start_full = time.time()
print('Reconstruction by erosion...')

# Read wav file
print('Getting input...')

# Load input spectrogram
spectrogram = load_or_compute('spectrogram', arrays_folder, {'spectrogram': True},
                              lambda: print('Not found'))

# Morphology - reconstruction by erosion
marker = apply_closing(spectrogram, {})
x_recons = torch.clone(marker)
temp = torch.clone(marker)

verbose_it_step = 10
count = 0
start = time.time()
while True:
    x_out = erosion_geodesic(x_recons, spectrogram)

    if count % verbose_it_step == 0:
        print("it:", count, 'log_diff: %.3f' % torch.log10(torch.sum(torch.abs(x_out - temp))).item())

        if plot:
            plot_compare(temp, x_out, 'reconstruction_erosion', 'Reconstruction by erosion', images_folder)
            plt.show()

        temp = torch.clone(x_out)

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
