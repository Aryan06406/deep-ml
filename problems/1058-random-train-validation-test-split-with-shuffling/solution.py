import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n = data.shape[0]
    indices = np.random.default_rng(seed).permutation(n)
    train_end = int(n * train_frac)
    val_end = train_end + int(n * validation_frac)
    train = data[indices[:train_end]]
    val = data[indices[train_end:val_end]]
    test = data[indices[val_end:]]

    return [train, val, test]