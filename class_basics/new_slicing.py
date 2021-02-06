import numpy as np

grid1d = np.array([1,2,3,4,5,6])

grid2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

plane1 = [[1,2,3],[4,5,6],[7,8,9]]
plane2 = [[10,20,30],[40,50,60],[70,80,90]]
plane3 = [[100,200,300],[400,500,600],[700,800,900]]
plane4 = [[100,200,300],[400,500,600],[700,800,900]]

grid3d = [plane1, plane2, plane3, plane4]

a3d = np.array(grid3d)
print(a3d)
print(a3d[0,0,:])
print(a3d[1,1,:])