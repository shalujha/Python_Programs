import functools
nums=[1,2,3,467,78,6]
evens=list(filter(lambda x:x%2==0,nums)) # filter some values from a given list
# if we want to change every values of  a list then we will use map
doubles=list(map(lambda x:x*2,evens))
sum=functools.reduce(lambda a,b:a+b,doubles)
print(sum)
print(doubles)
print(evens)