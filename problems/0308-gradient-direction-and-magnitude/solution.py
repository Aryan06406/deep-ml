import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	mag = np.sqrt(sum(x**2 for x in gradient))
	if mag == 0:
		direction = [0.0]*len(gradient)
		descent_direction = [0.0]*len(gradient)
	else:
		direction = [g/mag for g in gradient]
		descent_direction = [-g/mag for g in gradient]
	return {
		'magnitude': float(mag),
		'direction': direction,
		'descent_direction': descent_direction
	}		