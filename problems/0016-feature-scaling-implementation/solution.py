import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	mean = np.mean(data, axis=0)
	std = np.std(data, axis=0)
	std[std==0] = 1
	standardized_data = (data - mean) / std

	min_val = np.min(data, axis=0)
	max_val = np.max(data, axis=0)
	ranges = max_val - min_val
	ranges[ranges==0] = 1
	normalized_data = (data - min_val) / ranges 

	return standardized_data, normalized_data