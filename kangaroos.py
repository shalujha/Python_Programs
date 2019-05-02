x=input().split(" ")
x1=x[0]
v1=x[1]
x2=x[2]
v2=x[3]
if (x2>x1 and v2>v1) or (x1>x2 and v1>v2):
    print("No")
else:
    while True:
        x1+=v1
        x2+=v2
        if x1==x2:
            print("Yes")
            break
            