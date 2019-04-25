# simple functions or iterators that are used to create iterators
class fib():  #this class is both iterator as well as iterable class
    def __init__(self):
        self.prev=0
        self.curr=1
    def __iter__(self):
        return self # we are returning self because this is also an iterator class
    def __next__(self):
        value=self.curr
        self.curr+=self.prev
        self.prev=value
        return value
f=iter(fib())
print(next(f))
print(next(f))
print(next(f))
# if any function has a keyword yield then it is a generator function
def fibonacci():
    prev,curr=0,1
    while True:
        yield curr
        prev,curr=curr,curr+prev
print(type(fibonacci())) # it is of generator type
gen=fibonacci()
print(next(gen))
print(next(gen))
print(next(gen))

    