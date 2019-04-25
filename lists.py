n=int(input())
list=[]
for i in range(n):
    x=input().split(" ")
    if x[0]=='insert':
        list.insert(int(x[1]),int(x[2]))
    if x[0]=='print':
        print(list)
    if x[0]=='remove':
        list.remove(int(x[1]))
    if x[0]=='append':
        list.append(int(x[1]))
    if x[0]=='sort':
        list.sort()
    if x[0]=='pop':
        list.pop()
    if x[0]=='reverse':
        list.reverse()




