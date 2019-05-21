import numpy as np
a=np.array([1,2,3,4]) # this is basically used to create or initialise an array 
print(a)
print(type(a))
print(a.shape) # this attribute gives dimensions of array
b=np.array([[1],[2],[3],[4]]) # this is basically 2-d array
print(b)
print(type(b))
print(b.shape)
c=np.array([[1,2,3],[4,5,6]])
print(c)
print(c.shape)
print(c[1][1])
print(b[2][0])
# indexing starts from 0
# we can create array pf zeroes or ones or any custom arrays
d=np.zeros((3,3))
e=np.ones((4,4))
# array of some constant
f=np.full((3,2),5)
print(d)
print(e)
print(f)
# we can also make identity matrix-size/square matrix
g=np.eye(5)
print(g)
# we can also make random matrix
randomMatrix=np.random.random((2,3))
print(randomMatrix)
print(randomMatrix[:,1])
# we can updatethe matrix elements
randomMatrix[1,1:3]=1
print(randomMatrix)
# set some rows and columns with any value
h=np.zeros((3,3),dtype=np.int64)
h[1,:]=5
h[:,-1]=7
print(h)
# datatypes in python
print(h.dtype)
# bydefault array is a float
 # mathematical Operations on arrays
i=np.array([[1,2],[3,4]])
j=np.array([[1,2],[3,4]])
print(i+j) # element wise addition
# or
print(np.add(i,j)) # both methods will give same result
print(np.subtract(i,j)) # same for all 3
print(i-j)
print(np.multiply(i,j))
print(i*j)
print(np.divide(i,j))
print(i/j)
print(np.sqrt(i)) # can also be used to find square root
# matrix multiplication/ Dot product
print(i)
print(j)
print(i.dot(j))
print(np.dot(i,j))
# multiplication(dot product) of vectors-scalar
k=np.array([1,2,3,4])
l=np.array([1,2,3,4])
print(np.dot(k,l))
print(k)
print(sum(k)) # gives sum of all values of k
print(np.sum(k)) # same function as sum
print(i)
print(np.sum(i,axis=0)) # sums along the column
print(np.sum(i,axis=1)) # sums along the row
# stacking of array
print(k)
print(l)
print(np.stack((k,l),axis=1)) # it will be stacked along column in seperate array  k is in ist column and l is in second column
# and when axis =0, same thing happen but along row
# reshaping of array
m=np.array([[4,5,6],[7,8,9]])
print(m)
m=m.reshape(1,6)
m=m.reshape(6,1)
# if you dont want to calculate no of columns for that specific row then simply write it as -1
# and vice versa
m=m.reshape(6,-1)
print(m)