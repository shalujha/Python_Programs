import math
a=int(input())
b=int(input())
c=int(input())
d=((b*b)-(4*a*c))
if d>0:
    print("real and distinct")
if d==0:
    print("real and equal")
if d<0:
    print("imaginary")
root1=int((-b+math.sqrt(d))/(2*a))
root2=int((-b-math.sqrt(d))/(2*a))
print('{} {}'.format(root2,root1))