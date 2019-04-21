n=int(input())
flag=0
for i in range(1,n+1):
    if n%i==0:
        flag+=1
if flag==2:
    print("Prime")
else:
    print("Not Prime")