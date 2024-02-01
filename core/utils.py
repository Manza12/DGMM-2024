from . import *

from .parameters import EPS, FS


def to_db(x):
    return 20 * np.log10(x + EPS)


def from_db(x):
    return np.power(10, x / 20)


def get_duration(data):
    return len(data) / FS
