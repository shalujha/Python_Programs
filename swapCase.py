x=input().split(" ")
list=[]
for i in range(len(x)):
    list.append(x[i])
#print(list)
ans=[]
for j in range(len(list)):
    str=""
    for c in list[j]:
        if c.isupper():
            str+=c.lower()
        elif c.islower():
            str+=c.upper()
        else:
            str+=c
    ans.append(str)
print(*ans,end=' ')


