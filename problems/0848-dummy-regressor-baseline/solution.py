import numpy as np

def dummy_regressor(y_train, n_test, strategy='mean', constant=None, quantile=None):
    y_train = np.asarray(y_train, dtype=float)

    if strategy == 'mean':
        p = np.mean(y_train)

    elif strategy == 'median':
        p = np.median(y_train)

    elif strategy == 'quantile':
        if quantile is None or not 0 <= quantile <= 1:
            raise ValueError("quantile must be between 0 and 1")
        p = np.quantile(y_train, quantile)

    elif strategy == 'constant':
        if constant is None:
            raise ValueError("constant must be provided")
        p = constant

    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    return [float(p)] * n_test