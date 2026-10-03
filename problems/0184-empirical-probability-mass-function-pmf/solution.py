from collections import Counter

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    if not samples:
        return []
    counts = Counter(samples)
    total = len(samples)
    return [
        (value, count / total)
        for value, count in sorted(counts.items())
    ]