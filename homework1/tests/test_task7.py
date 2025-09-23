import numpy as np
from task7 import matrix_multiply

# mult a 2x2
def test_matrix_multiply_2x2():
    # input two 2x2 matrixes
    a = [[1, 2], [3, 4]]
    b = [[2, 0], [1, 2]]
    # Expected answer
    expected = np.array([[4, 4], [10, 8]])
    np.testing.assert_array_equal(matrix_multiply(a, b), expected)
# mult a 2x3 by 3x2
def test_matrix_multiply_2x3_3x2():
    # input two a 2x3 & 3x2 matrixe
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    # Expected answer
    expected = np.array([[58, 64], [139, 154]])
    # Compare to expected to see if function works properly
    np.testing.assert_array_equal(matrix_multiply(a, b), expected)
