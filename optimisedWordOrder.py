n=int(input())
list=[]
for i in range(n):
    list.append(input())
d={}
for c in list:
    if c not in d:
        d[c]=1
    else:
        d[c]+=1
print(len(d))
for i in d:
    print(d[i],end=' ')
    
