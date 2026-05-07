import numpy as np


def clean_data(data):
    """Convert input to clean 1D numeric array."""

    data = np.asarray(data, dtype=float)
    data = np.ravel(data)
    data = data[np.isfinite(data)]

    return data


def standardize(data):
    """Standardize data."""

    mean = np.mean(data)
    std = np.std(data)

    scaled = (data - mean) / std

    return scaled, mean, std
