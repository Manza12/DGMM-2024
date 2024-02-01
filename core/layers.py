from .utils import to_db
from .parameters import *


def apply_stft_layer(signal, verbose=True, output_format='Magnitude', input_name='signal'):
    start = time.time()
    _, _, spectrogram_complex = sig.stft(signal, fs=FS,
                                         window=WINDOW,
                                         nperseg=WIN_LENGTH,
                                         noverlap=N_OVERLAP,
                                         nfft=N_FFT)

    if output_format == 'Magnitude':
        spectrogram = np.sqrt(np.abs(spectrogram_complex)**2)
        spectrogram = to_db(spectrogram)
    else:
        spectrogram = spectrogram_complex

    if verbose:
        print('Time to apply STFT to %s: %.3f seconds' % (input_name, time.time() - start))

    return spectrogram
