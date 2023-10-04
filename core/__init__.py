import time
import numpy as np
import scipy.io.wavfile as wav
import numbers
import warnings
import torch
import pickle
import nnMorpho.greyscale_operators as greyscale
import nnMorpho.binary_operators as binary
import nnAudio.features.stft as stft
import nnAudio.features.cqt as cqt
import torch.nn.functional as func
import scipy.signal.windows as win
import scipy.ndimage as image
import scipy.signal as sig
import scipy.fft as fft
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import matplotlib as mpl
import matplotlib.widgets as wid
from typing import Union, List, Optional, Tuple
from pathlib import Path

_ = [wav, np, numbers, warnings, torch, stft, cqt, pickle, plt, tick, mpl, wid, func, win, greyscale, image,
     sig, fft, binary, time]
_ = [Union, List, Optional, Tuple, Path]
