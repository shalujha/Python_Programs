l=input()
a=list(l)
sum=0
for i in range(len(a)):
    sum+=int(a[i])
    if sum>0:
        print(a[i])
    else:
        break


