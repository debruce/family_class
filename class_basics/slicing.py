import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 2*np.pi, num=500)

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(x, np.sin(x), color='green')
# ax.plot(x[0:250], -np.sin(x)[0:250], color='red')
# plt.show()

data_as_list = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9, 10, 11123.4556, 12 ],
    [ 13, 14, 15, 16 ]
]


data_as_array= np.array(data_as_list,dtype=np.float64)
np.set_printoptions(suppress=True)
print(data_as_array.shape)
print(data_as_array.dtype)

print(data_as_list)
print()
print(data_as_array)
print()
print(f"first slice from list of lists =\n{data_as_list[0:4:2]}")
print()
print(f"first+second slice from list of lists =\n{data_as_list[0:2][0:2]}")
print()
print(f"slice from 2d array = \n{data_as_array[0:3,0:2]}")

# dinv = np.linalg.inv(d)

# print(d)
# print()
# print(dinv)

# p = d * dinv
# print()
# print(p)

# # print(data)

# # print(d.shape)
# # print(d.dtype)
# # print(d)
