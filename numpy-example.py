import numpy as np


print(np.__version__)

list1 = [10, 20, 30, 40, 50, 60]
print(list1)

array = np.array(list1)
print(array)

np_array = np.array([10, 20, 30, 40, 50, 60])
print('np_array'+str(np_array))

print(array + 15)

print(np_array.shape)
print(array.shape)
print(array.dtype)

np_array = np.array([10, 20, 30, 40, 50, 60], dtype=complex)
print(np_array)

np_array = np.array([10, 20, 30, 40, 50, 60], ndmin=2)
print(np_array)

