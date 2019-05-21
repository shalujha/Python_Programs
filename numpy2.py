# Some more numpy functions
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(np.min(a)) # returns minimum element from 2D array
# specify axis for the direction
print(np.min(a,axis=0)) # returns minimum element along the axis
print(np.min(a,axis=1))
b=np.array([1,2,3,4,5])
m=sum(b)/5
print(m)
print(np.mean(b))
print(np.mean(a,axis=0)) # along column
print(np.mean(a,axis=1)) # along row
c=np.array([5,4,2,3,1])
print(np.median(c))
# weights
w=np.array([1,5,4,2,0])
print(np.average(c,weights=w))
# standard deviation
u=np.mean(w)
my_std=np.sqrt(np.mean(abs(w-u)**2))
print(my_std)
# inbuilt function of std
print(np.std(w))
# variance
print(my_std**2)
print(np.var(w))


