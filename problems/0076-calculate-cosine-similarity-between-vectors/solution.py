import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	if len(v1) != len(v2):
		raise ValueError("Length of both vectors must be same.")
	dot_product = v1 @ v2
	mag_1 = np.linalg.norm(v1)
	mag_2 = np.linalg.norm(v2)
	if mag_1 == 0 or mag_2 == 0:
		raise ValueError("Cosine similarity is undefined for zero vectors.")
	return dot_product / (mag_1 * mag_2)		