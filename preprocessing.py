import pandas as pd



def block_maxima(data, block_size=None, freq=None):
    """
    Extract block maxima.

    Parameters
    ----------
    data : pandas Series
        Time-indexed series.

    block_size : int
        Integer grouping size.

    freq : str
        Pandas resample frequency.
    """

    if freq is not None:
        return data.resample(freq).max().dropna()

    if block_size is not None:
        grouped = [
            data.iloc[i:i+block_size].max()
            for i in range(0, len(data), block_size)
        ]

        return pd.Series(grouped).dropna()

    raise ValueError("Specify block_size or freq")
