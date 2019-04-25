# iteration Protocol in Python
# some Terminologies:
# iteration: Repition of a process
# iterable: a python object which supports iteration
# iterator: a python object to support iteration over a iterable
x=[1,2,3]
x_iter=iter(x)
#print(type(x_iter))
for i in range(len(x)):
    print(next(x_iter))
# iterable protocol is a fancy term which means how iterators actually work in python
# 1.for a class object to be iterable :
# can be Passed to iter functionto get an iterator for them
# for any iterator:
# can be Passed to next function which gives their next item or stop iteration
# Return themselves when Passed through iter function
# lets make our Range class:
class YRange():
    # this method tells whats the range user want and i is the no of iteration done yet
    def __init__(self,n):
        self.i=0
        self.n=n
    # this method makes our class iterable
    def __iter__(self):
        return self
    # this method should be implemented by iterator
    def __next__(self):
        if self.i<self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration()
for x in YRange(5):
    print(x)
y=YRange(5) # it returns iterable object
print(type(y))
y_iter=iter(y) # it return iterator object
print(type(y_iter))
# hence we can see that both iterable and iterator are of same type in this case
# this is the iterable class
class Zrange():
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return zrange_iter(self.n)
# this is the iterator class
class zrange_iter():
    def __init__(self,n):
        self.i=0
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration()
for x in Zrange(5):
    print(x**2)

