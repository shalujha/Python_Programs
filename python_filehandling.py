# There are six file handling modes:
# Read Only(r)  data camn be read only
# Read and write(r+)   read as well as write (over write on existing data)
# Write Only(w)
# Write and Read(w+)
# Append(a)  in this case cursor or file handler will point at end of file
# Append and read(a+)
# file handler is positioned at the beginning in every cases
# in every case, file is created if it doesnt exists
# first: read only
f = open("Test.txt",'r') # f is basically a file handler
print(f.read())    
f.close()
# second: write only
f=open("test.txt",'w')
content=["Hello World\n"]
l=content*3
f.writelines(l) # difference between write and writelines is write is used to giving parameters in the form of list wheras writeline is used when we give multiple lines as argument
f.close()
# Reading From a file
f=open("Test.txt",'r')
# print(f.read()) # read reads everything
# print(f.readline()) # it reads only first line
print(type(f.readlines())) # it returns the list
# Reading using WITH OPEN
with open("Test.txt",'r') as f:
   # f.close()
    print(f.closed) # it checks whether the file is closed or not , it returns the boolean value
    print(f.read()) # if the file is closed and then also we want to read file then io exception will occur
# Automatically closes the file which ensures a cleanup is always there
print(f.closed)
# if i dont want the file handler to start from beginning and start from somewhere else then we use seek function
with open("Test.txt",'r') as f:
    f.seek(5)
    print(f.read())



