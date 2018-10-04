import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[1][1])
print(a[1][0:2])

x=np.array([[1,1],[2,2]])
y=np.array([[3,3],[4,4]])
z=x*y
print(z)
z=np.dot(x,y)
print(z)

#similar functionality as NP1D, just use [[][]] to make it a 2D array