from random import shuffle
import numpy as np
from multiprocessing import Pool

# Calculate sum matrix
def get_sum_matrix(A, B):
    n_rows = A.shape[0]
    n_cols = A.shape[1]
    sum_matrix = np.zeros((n_rows, n_cols))
    for i in range(n_rows):
        for j in range(n_cols):
            sum_matrix[i][j] = A[i][j] + B[i][j]
    return sum_matrix

def inverse(A):
    """
    Calculate the inverse of a matrix A (NxN)
    return A^-1
    """
    # check if A is square
    n_rows = A.shape[0]
    n_cols = A.shape[1]
    assert n_rows == n_cols, "Matrix A is not square"
    # check if A is invertible
    # det = np.linalg.det(A)
    # assert det != 0, "Matrix A is not invsertible"
    # calculate the inverse
    inv = np.linalg.inv(A)
    return inv

def inverse_of_sum(A, B):
    return inverse(get_sum_matrix(A, B))

if __name__ == '__main__':    
    A = np.array( [[1, 2, 1], [2, 1, 1], [1, 1, 1]])
    B = np.array([[3, -2, 1], [2, 4, 1], [3, 6, 1]])
    C = np.array([[6, 2, 1], [2, 1, 0], [2, 6, -2]])
    D = np.array([[2, -4, 1], [7, -7, 5], [2, -2, 1]])
    
    process = Pool(processes=6)
    params = [(A, B), (A, C), (A, D), (B, C), (B, D), (C, D)]
    shuffle(params)
    results = process.starmap(inverse_of_sum, params)
    process.close()
    