import numpy as np
from statistics import multimode

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data = np.asarray(data, dtype=float)
    if data.size == 0:
        raise ValueError("Dataset must not be empty.")
    if not np.all(np.isfinite(data)):
        raise ValueError("Dataset must contain only finite numbers.")
    mean = np.mean(data)
    median = np.median(data)
    modes = multimode(data.tolist())
    mode = modes[0] 
    variance = np.var(data, ddof=0)
    standard_deviation = np.sqrt(variance)
    percentile_25 = np.percentile(data, 25)
    percentile_50 = np.percentile(data, 50)
    percentile_75 = np.percentile(data, 75)
    iqr = percentile_75 - percentile_25

    return {
        "mean": float(mean),
        "median": float(median),
        "mode": mode,
        "variance": float(variance),
        "standard_deviation": float(standard_deviation),
        "25th_percentile": float(percentile_25),
        "50th_percentile": float(percentile_50),
        "75th_percentile": float(percentile_75),
        "interquartile_range": float(iqr)
    }