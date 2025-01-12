import numpy as np

def reconstruct_matrix(U, S, V):
    return np.dot(np.dot(U, S), V)