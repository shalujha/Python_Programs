n=int(input())
list=[]
for i in range(n):
    score=int(input())
    list.append(score)
def nextMultiple(a):
    if a%5==0:
        return 0
    else:
        ans=a%5
        return a+(5-ans)
for i in range(len(list)):
    if list[i]>=38 and nextMultiple(list[i])-list[i]<3:
        print(nextMultiple(list[i]))
    else:
        print(list[i])
    
