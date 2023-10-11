# DGMM 2024
## Mathematical Morphology Applied to Feature Extraction in Music Spectrograms
### Gonzalo Romero-García
The code is organised in the following way:
- `core/` contains the source code.
- `data/` contains the data used in the experiments. The subfolder `audio/` contains the input audio files and the subfolder `objects/` constains the STFT layers with different time and frequency resolutions.
- `procedures/` contains the procedures used to apply the morphological pipeline, synthesize and plot.
- `results/` contains the results obtained in the experiments.
- `tests` contains some tests to check the code.
- `main.py` is the main script that should be run to execute the pipeline and plot the outputs. The input audio is encoded in the variable `name`.
- `settings.py` is a file with the settings used for each audio sample for running the code.

If you want to change the parameters used for the computations, see the file `core/parameters.py`.

If you want to ear an audio sample, go to `results` and find the name of the sample. Inside its folder, there are the `arrays`, the `audio` and the `images`. In the audio folder there are six different files:
- `input.wav` is the original audio sample.
- `sinusoids.wav` is the output of the sinusoidal component.
- `transients.wav` is the output of the transient component.
- `filtered_noise.wav` is the output of the noise component.
- `denoised.wav` is the sum of sinusoids and transient. 
- `output.wav` is the sum of sinusoids, transient and noise.