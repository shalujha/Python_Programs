#iterator or iterable is an object in python that can be iterated upon
# returns single object one by one so that we can perform task over it
# list,tuples are some example of iterable object
lists=[1,2,[1,2],3,4]
for x in lists:
    print(x)
name='shalini'
for char in name:
    print(char)
d={"name":"shalini","last_name":"jha","marks":"80"}
for i in d:
    print(i)  # i will get keys of dictionary
# so we can see it(the value which we get after iteration) depends upon the type of objects on which i m iterating upon
for line in open("something.txt",'r'):
    print(line) # i m printing the line in every line from the file something.txt
# iterators not only work with loops , it works with join. join basically iterates over iterable object and joins the items by the specified string
print('.'.join(['a','b','c']))
a=list('shalini') # it takes iterable object and iterates on it
print(a)
b=[1,2,3,4]
print(sum(b))



