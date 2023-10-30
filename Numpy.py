import numpy as np
'''
print([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) #Print a list of lists

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9,10,11,12]])
print(a.shape)

a = np.array([1, 2, 3])
a = np.append(a, 4)
print(a)


a = np.array([[1,2,3],
              [4,5,6]])
b = np.array([[7,8,9],
              [10,11,12]])
print(np.append(a, b, axis = 0))

print(a.T)


a = np.array([[1,2],
              [4,5]])

from numpy.linalg import inv
print(inv(a))


print(np.arange(0,10,2)) # [0,10) step = 2
print(np.arange(15))  # [0,15)  step = 1
a = np.arange(9)
print(a.reshape(3,3))


print(np.zeros((3, 4)))
print(np.ones((3, 4)))


from numpy.random import rand, randn
print(rand(3, 4))

a = np.array([20, 30, 40, 50])
b = np.array([20, 30, 40, 50])
print(a - b)
print(a - 10)
print(a > 20)
print(a[[0, 2]])

'''

a = np.array([[ 0,  1,  2,  3,  4],
              [ 5,  6,  7,  8,  9],
              [10, 11, 12, 13, 14]])
print(a)
print(a[:,0])
print(a[0:2, 3:4])
print(a[[0, 1], 0])
b = np.array([[1],[2],[3],[4],[5]])
print(a @ b)
print(a.min())
print(a.mean(axis=0))
print(a.mean(axis=1))
