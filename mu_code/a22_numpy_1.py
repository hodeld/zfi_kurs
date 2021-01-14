import numpy as np
import itertools

arr = np.array([[1, 2, 4], [3, 4, 5]])  # 1 argument
print(arr)
arr.sum(axis=1)
arr2 = np.where(arr < 3, 1, 0)
print(arr2)
arr3 = arr - arr2
print(arr3)
arr3_t = np.transpose(arr3)
print(arr3_t)
arr.shape()