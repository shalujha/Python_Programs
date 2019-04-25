n=int(input())
list=[]
for i in range(n):
    list.append(input())
def distinctElements(list):
    distinct=0
    for m in range(len(list)):
        flag=0
        for p in range(m+1,len(list)):
            if list[m]==list[p]:
                flag=1
                break
        if flag==0:
            distinct+=1
    return distinct
def occurences(list):
    d={}
    for c in list:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d
print(distinctElements(list))
a=occurences(list)
for c in a:
    print(a[c],end=' ')


    




