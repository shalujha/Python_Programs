n=int(input())
# print([i for i in range(1,n+1) if n%i is 0],sep=',')
list=[]
for i in range(1,n+1):
    if n%i==0:
        list.append(i)
print(*list,sep=',')