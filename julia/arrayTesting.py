import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array(['one', 'two', 'three'])
arr3 = np.array([1, 2, 3, 4, 5], dtype = 'S')

print(arr[0,:], arr[1,:])
print()
print(arr[:1, 1:2])
print()
print(arr.dtype)
print(arr2.dtype)
print(arr3.dtype)
#arr3 is converting the data type of the array from integers to strings