n=int(input())
list=[]
for i in range(n):
    score=int(input())
    list.append(score)
for j in range(len(list)):
    if list[j]>=38 and (list[j]+(5-(list[j]%5))-list[j])<3:
        print(list[j]+(5-(list[j]%5)))
    else:
        print(list[j])
