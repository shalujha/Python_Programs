l=input()
a=list(l)
print(a)
print(type(a[0]))
sum=0
for c in range(len(a)):
    sum+=int(a[c])
print(sum)
