# Use pip to install package of your choice and write script
import numpy as np

# Matrix Multiplication
def matrix_multiply(a, b):
    matrix_a = np.array(a)
    matrix_b = np.array(b)
    result = np.dot(matrix_a, matrix_b)
    return result