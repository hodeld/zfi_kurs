import numpy as np

arr = np.array([[1, 2, 4], [3, 4, 5]])  # 1 argument
print(arr)
arr.sum(axis=1)
arr2 = np.where(arr < 3, 1, 0)
print(arr2)
arr3 = arr - arr2
print(arr3)
arr3_t = np.transpose(arr3)
print(arr3_t)
arr.shape
arr.size
np.zeros((3, 4))
np.ones((2,3,4))
arr_range = np.arange(10)
np.tile(arr_range, (4, 1))