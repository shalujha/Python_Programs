import numpy as np
# if you want to generate an array within a given range then go for arrange function
a=np.arange(10) # it returns an array having numbers from 0 to 9
print(a)
# shuffle is a function in random function of numpy module that shuffles the contents of a sequence
# to replicate the result or to start the series of random numbers in the same order we should seed the value
np.random.seed(1)
np.random.shuffle(a)
print(a)
# we can also generate an array of random numbers by passing shape as a parameter
# returns values from a standard normal distributions
print(np.random.rand(2,3))
print(np.random.randint(5,10,3)) # it will return 3 random values within the range 5 and 10
# randomly pick one element from array
print(np.random.choice([1,2,3,4,5]))