x=int(input())
y=int(input())
z=int(input())
n=int(input())
large=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                list=[]
                list.append(i)
                list.append(j)
                list.append(k)
                large.append(list)
print(large)

