import numpy as np

def compute_cross_product(arr1, arr2):
    return np.cross(arr1, arr2)

print(compute_cross_product(np.array([1,2]), np.array([2,2])))