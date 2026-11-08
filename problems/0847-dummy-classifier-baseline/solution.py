import numpy as np
from collections import Counter
import math

def dummy_classifier(y_train, n_test, strategy, constant=None):
    classes = sorted(set(y_train))
    if strategy == "most_frequent":
        counts = Counter(y_train)
        prediction = min(classes, key=lambda c: (-counts[c], c))
        return [prediction] * n_test

    elif strategy == "constant":
        return [constant] * n_test

    elif strategy == "uniform":
        k = len(classes)
        return [classes[i % k] for i in range(n_test)]

    elif strategy == "stratified":
        counts = Counter(y_train)
        n_train = len(y_train)

        allocations = {
            c: math.floor(n_test * counts[c] / n_train)
            for c in classes
        }

        remaining = n_test - sum(allocations.values())

        # Sort by descending fractional remainder, then ascending class label
        remainders = sorted(
            classes,
            key=lambda c: (
                -(n_test * counts[c] / n_train - allocations[c]),
                c
            )
        )

        for c in remainders[:remaining]:
            allocations[c] += 1

        return [
            c
            for c in classes
            for _ in range(allocations[c])
        ]

    else:
        raise ValueError(f"Unknown strategy: {strategy}")